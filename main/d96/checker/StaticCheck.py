
"""
 * @author nhphung
"""
# from msilib.schema import Binary
from AST import * 
from Visitor import *
# from Utils import Utils
from StaticError import *
from typing import Dict

class StaticChecker:
    pass

class NoneType(Type):
    def __str__(self):
        return "NoneType"

class MethodInfo:
    method: MethodDecl
    retType: Type

    def __init__(self, ast:MethodDecl, c:StaticChecker):
        self.method = ast
        if ast.name.name in ('Constructor', 'Destructor'):
            self.retType = NoneType()
        elif ast.name.name == 'main' and c.environment.currentClass.name == 'Program':
            if type(ast.kind) is Static:
                self.retType = NoneType()
            else:
                raise NoEntryPoint()
        else:
            self.retType = None


class ClassInfo:
    name: str
    attributes: Dict[str,AttributeDecl]
    methods: Dict[str,MethodInfo]
    def __init__(self, name:str):
        self.name = name
        self.attributes = {}
        self.methods = {}


class Environment:
    classList: Dict[str,ClassInfo]
    blocks: List[dict]
    currentClass: ClassInfo
    idKind: List[Kind] # use in Undeclared and Redeclared errors
    currentMethod: MethodInfo
    loopNum: int # use to determine whether Continue and Break statements are in loop or not
    def __init__(self):
        self.classList = {}
        self.blocks = []
        self.idKind = []
        self.loopNum = 0



class StaticChecker(BaseVisitor):

    def __init__(self,ast):
        self.ast = ast
        self.environment = Environment()

    def check(self):
        return self.visit(self.ast,self.environment)

    def visitProgram(self, ast:Program, c:Environment):
        for x in ast.decl:
            self.visit(x,c)
        if 'Program' in c.classList:
            if 'main' in c.classList['Program'].methods:
                return ""
        raise NoEntryPoint()

    def visitClassDecl(self, ast:ClassDecl, c:Environment):
        c.blocks.append({})
        if ast.classname.name in c.classList:
            raise Redeclared(Class(), ast.classname.name)
        if ast.parentname and ast.parentname.name not in c.classList:
            raise Undeclared(Class(), ast.parentname.name)
        c.classList[ast.classname.name] = c.currentClass = ClassInfo(ast.classname.name)
        for x in ast.memlist:
            self.visit(x,c)
        c.blocks.pop()
        if ast.classname.name == 'Program':
            if 'main' not in c.currentClass.methods:
                raise NoEntryPoint()

    def visitAttributeDecl(self, ast:AttributeDecl, c:Environment):
        id = self.visit(ast.decl, c)
        if type(ast.decl) is VarDecl:
            c.currentClass.attributes[ast.decl.variable.name] = ast
        elif type(ast.decl) is ConstDecl:
            c.currentClass.attributes[ast.decl.constant.name] = ast

    def visitMethodDecl(self, ast:MethodDecl, c:Environment):
        c.currentClass.methods[ast.name.name] = c.currentMethod = MethodInfo(ast,self)
        c.idKind.append(Parameter())
        c.blocks.append({})
        for p in ast.param:
            self.visit(p,c)
        c.idKind.pop()
        self.visit(ast.body,c)
        c.blocks.pop()
        if not c.currentMethod.retType:
            c.currentMethod.retType = NoneType()

    def sameTypes(typ1:Type, typ2:Type):
        if type(typ1) is ClassType and type(typ2) is VoidType:
            return True
        elif type(typ1) is ClassType and type(typ2) is ClassType:
            return typ1.classname.name == typ2.classname.name
        elif type(typ1) is ArrayType and type(typ2) is ArrayType:
            return typ1.size == typ2.size and StaticChecker.sameTypes(typ1.eleType, typ2.eleType)
        elif type(typ1) is type(typ2):
            return True

    def visitVarDecl(self, ast:VarDecl, c:Environment):
        if ast.variable.name in c.blocks[-1]:
            raise Redeclared(Attribute() if len(c.blocks) == 1 else Parameter() if type(c.idKind[-1]) is Parameter else Variable(), ast.variable.name)
        c.blocks[-1][ast.variable.name] = ast
        self.visit(ast.varType,c)
        if ast.varInit:
            c.idKind.append(Identifier())
            typ, decl = self.visit(ast.varInit,c)
            c.idKind.pop()
            if decl is ClassDecl: raise Undeclared(Identifier(), ast.varInit.name)
            if not StaticChecker.sameTypes(self.visit(ast.varType,c),typ):
                raise TypeMismatchInStatement(ast)

    def visitConstDecl(self, ast:ConstDecl, c:Environment):
        if ast.constant.name in c.blocks[-1]:
            raise Redeclared(Attribute() if len(c.blocks) == 1 else Constant(), ast.constant.name)
        c.blocks[-1][ast.constant.name] = ast
        self.visit(ast.constType,c)
        if ast.value:
            c.idKind.append(Identifier())
            typ, decl = self.visit(ast.value,c)
            c.idKind.pop()
            if decl is ClassDecl: raise Undeclared(Identifier(), ast.varInit.name)
            if not StaticChecker.sameTypes(self.visit(ast.constType,c),typ):
                raise TypeMismatchInConstant(ast)
            if decl is VarDecl:
                raise IllegalConstantExpression(ast.value)
        else:
            raise IllegalConstantExpression(ast.value)

    def visitIntType(self, ast:IntType, c:Environment):
        return ast

    def visitFloatType(self, ast:FloatType, c:Environment):
        return ast

    def visitBoolType(self, ast:BoolType, c:Environment):
        return ast

    def visitStringType(self, ast:StringType, c:Environment):
        return ast

    def visitArrayType(self, ast:ArrayType, c:Environment):
        self.visit(ast.eleType, c)
        return ast

    def visitClassType(self, ast:ClassType, c:Environment):
        if ast.classname.name in c.classList:
            return ast
        raise Undeclared(Class(), ast.classname.name)

    def visitIntLiteral(self, ast:IntLiteral, c:Environment):
        return IntType(), ConstDecl

    def visitFloatLiteral(self, ast:FloatLiteral, c:Environment):
        return FloatType(), ConstDecl

    def visitStringLiteral(self, ast:StringLiteral, c:Environment):
        return StringType(), ConstDecl

    def visitBooleanLiteral(self, ast:BooleanLiteral, c:Environment):
        return BoolType(), ConstDecl

    def visitNullLiteral(self, ast:NullLiteral, c:Environment):
        return VoidType(), ConstDecl
    
    def visitSelfLiteral(self, ast:SelfLiteral, c:Environment):
        return ClassType(Id(c.currentClass.name)), ConstDecl

    def visitArrayLiteral(self, ast:ArrayLiteral, c:Environment):
        size = len(ast.value)
        if size == 0:
            return ArrayType(0,None), ConstDecl

        typ, decl = self.visit(ast.value[0],c)
        for mem in ast.value:
            t, d = self.visit(mem,c)
            if not StaticChecker.sameTypes(typ,t):
                raise IllegalArrayLiteral(ast)
            if d is VarDecl:
                decl = VarDecl
        return ArrayType(size,typ), decl
    
    def visitId(self, ast:Id, c:Environment):
        for scope in reversed(c.blocks):
            if ast.name in scope:
                decl = scope[ast.name]
                if type(decl) is ConstDecl:
                    return decl.constType, ConstDecl
                elif type(decl) is VarDecl:
                    return decl.varType, VarDecl
        if ast.name in c.classList:
            return c.classList[ast.name], ClassDecl
        raise Undeclared(c.idKind[-1],ast.name)

    def visitBinaryOp(self, ast:BinaryOp, c:Environment):
        c.idKind.append(Identifier())
        left, ld = self.visit(ast.left, c)
        right, rd = self.visit(ast.right, c)
        c.idKind.pop()
        if ld is ClassDecl: raise Undeclared(Identifier(),ast.left.name)
        if rd is ClassDecl: raise Undeclared(Identifier(),ast.right.name)
        d = ConstDecl if ld is ConstDecl and rd is ConstDecl else VarDecl
        if ast.op in ('+','-','*','/'):
            if type(left) is IntType and type(right) is IntType:
                return IntType(), d
            elif type(left) in (IntType, FloatType) and type(right) in (IntType, FloatType):
                return FloatType(), d
        elif ast.op == '%':
            if type(left) is IntType and type(right) is IntType:
                return IntType(), d
        elif ast.op in ('!','&&','||'):
            if type(left) is BoolType and type(right) is BoolType:
                return BoolType(), d
        elif ast.op == '==.':
            if type(left) is StringType and type(right) is StringType:
                return BoolType(), d
        elif ast.op == '+.':
            if type(left) is StringType and type(right) is StringType:
                return StringType(), d
        elif ast.op in ('==','!='):
            if (type(left) is IntType and type(right) is IntType) or (type(left) is BoolType and type(right) is BoolType):
                return BoolType(), d
        elif ast.op in ('<','<=','>','>='):
            if type(left) in (IntType, FloatType) and type(right) in (IntType, FloatType):
                return BoolType(), d
        raise TypeMismatchInExpression(ast)
    
    def visitUnaryOp(self, ast:UnaryOp, c:Environment):
        c.idKind.append(Identifier())
        body, d = self.visit(ast.body, c)
        c.idKind.pop()
        if d is ClassDecl: raise Undeclared(Identifier(),ast.left.name)
        if ast.op in ('-'):
            if type(body) in (IntType, FloatType):
                return type(body)(), d
        elif ast.op in ('!'):
            if type(body) is BoolType:
                return BoolType(), d
        raise TypeMismatchInExpression(ast)

    def checkparatype(method:MethodDecl, param:List[Expr], c:StaticChecker, ast):
        if len(param) != len(method.param):
            if type(ast) is CallExpr: raise IllegalMemberAccess(ast)
            elif type(ast) is NewExpr: raise TypeMismatchInExpression(ast)
            elif type(ast) is CallStmt: raise TypeMismatchInStatement(ast)
        pTyp = [c.visit(p,c.environment)[0] for p in param]
        for i in range(len(param)):
            if not StaticChecker.sameTypes(method.param[i].varType,pTyp[i]):
                if type(ast) is CallExpr: raise IllegalMemberAccess(ast)
                elif type(ast) is NewExpr: raise TypeMismatchInExpression(ast)
                elif type(ast) is CallStmt: raise TypeMismatchInStatement(ast)

    def visitCallExpr(self, ast:CallExpr, c:Environment):
        c.idKind.append(Class() if ast.method.name[0] == '$' else Identifier())
        objTyp, _ = self.visit(ast.obj,c)
        c.idKind.pop()
        if type(objTyp) is ClassInfo:
            if ast.method.name in objTyp.methods:
                methodInfo = objTyp.methods[ast.method.name]
                if type(methodInfo.method.kind) is Static:
                    StaticChecker.checkparatype(methodInfo.method, ast.param, self, ast)
                    return methodInfo.retType, ConstDecl
            else:
                raise Undeclared(Method(), ast.method.name)
        elif type(objTyp) is ClassType:
            if objTyp.classname.name in c.classList:
                classInfo = c.classList[objTyp.classname.name]
                if ast.method.name in classInfo.methods:
                    methodInfo = classInfo.methods[ast.method.name]
                    if type(methodInfo.method.kind) is Instance:
                        StaticChecker.checkparatype(methodInfo.method, ast.param, self, ast)
                        return methodInfo.retType, ConstDecl
                else:
                    raise Undeclared(Method(), ast.method.name)
            else:
                raise Undeclared(Identifier(), objTyp.classname.name)
        raise TypeMismatchInExpression(ast)

    def visitNewExpr(self, ast:NewExpr, c:Environment):
        c.idKind.append(Class())
        classTyp, _ = self.visit(ast.classname,c)
        c.idKind.pop()
        if type(classTyp) is ClassInfo:
            methodInfo = classTyp.methods['Constructor'] if 'Constructor' in classTyp.methods else\
                         MethodInfo(MethodDecl(Instance(),Id('Constructor'),[],Block([])), self)
            StaticChecker.checkparatype(methodInfo.method, ast.param, self, ast)
            return ClassType(Id(ast.classname.name)), ConstDecl
        raise TypeMismatchInExpression(ast)

    def visitFieldAccess(self, ast:FieldAccess, c:Environment):
        c.idKind.append(Class() if ast.fieldname.name[0] == '$' else Identifier())
        objTyp, _ = self.visit(ast.obj,c)
        c.idKind.pop()
        if type(objTyp) is ClassInfo:
            if ast.fieldname.name in objTyp.attributes:
                attribute = objTyp.attributes[ast.fieldname.name]
                if type(attribute.kind) is Static:
                    if type(attribute.decl) is VarDecl:
                        return attribute.decl.varType, VarDecl
                    elif type(attribute.decl) is ConstDecl:
                        return attribute.decl.constType, ConstDecl
            else:
                raise Undeclared(Attribute(), ast.fieldname.name)
        elif type(objTyp) is ClassType:
            if objTyp.classname.name in c.classList:
                classInfo = c.classList[objTyp.classname.name]
                if ast.fieldname.name in classInfo.attributes:
                    attribute = classInfo.attributes[ast.fieldname.name]
                    if type(attribute.kind) is Instance:
                        if type(attribute.decl) is VarDecl:
                            return attribute.decl.varType, VarDecl
                        elif type(attribute.decl) is ConstDecl:
                            return attribute.decl.constType, ConstDecl
                else:
                    raise Undeclared(Attribute(), ast.fieldname.name)
            else:
                raise Undeclared(Identifier(), objTyp.classname.name)
        raise TypeMismatchInExpression(ast)

    def visitArrayCell(self, ast:ArrayCell, c:Environment):
        decl = ConstDecl
        for e in ast.idx:
            t, d = self.visit(e,c)
            if not type(t) is IntType:
                raise TypeMismatchInExpression(ast)
            if d is VarDecl:
                decl = VarDecl
        typ, decl0 = self.visit(ast.arr,c)
        if decl0 is VarDecl:
            decl = VarDecl
        for _ in range(len(ast.idx)):
            if type(typ) is ArrayType:
                typ = typ.eleType
            else:
                raise TypeMismatchInExpression(ast)
        return typ, decl
    
    def visitBlock(self, ast:Block, c:Environment):
        c.blocks.append({})
        for stmt in ast.inst:
            self.visit(stmt,c)
        c.blocks.pop()
    
    def visitAssign(self, ast:Assign, c:Environment):
        c.idKind.append(Identifier())
        lTyp, ld = self.visit(ast.lhs,c)
        rTyp, rd = self.visit(ast.exp,c)
        c.idKind.pop()
        if ld is ConstDecl:
            raise CannotAssignToConstant(ast)
        if not StaticChecker.sameTypes(lTyp, rTyp):
            raise TypeMismatchInStatement(ast)
    
    def visitIf(self, ast:If, c:Environment):
        if type(self.visit(ast.expr,c)[0]) is not BoolType:
            raise TypeMismatchInStatement(ast)
        self.visit(ast.thenStmt,c)
        if ast.elseStmt: self.visit(ast.elseStmt,c)

    def visitFor(self, ast:For, c:Environment):
        c.idKind.append(Identifier())
        idTyp, idDecl = self.visit(ast.id,c)
        c.idKind.pop()
        if type(idTyp) is not IntType:
            raise TypeMismatchInStatement(ast)
        if idDecl is not VarDecl:
            raise CannotAssignToConstant(Assign(ast.id,ast.expr1))
        if type(self.visit(ast.expr1,c)[0]) is not IntType:
            raise TypeMismatchInStatement(ast)
        if type(self.visit(ast.expr2,c)[0]) is not IntType:
            raise TypeMismatchInStatement(ast)
        if ast.expr3:
            if type(self.visit(ast.expr3,c)[0]) is not IntType:
                raise TypeMismatchInStatement(ast)
        c.loopNum += 1
        self.visit(ast.loop,c)
        c.loopNum -= 1

    def visitBreak(self, ast:Break, c:Environment):
        if c.loopNum == 0:
            raise MustInLoop(ast)

    def visitContinue(self, ast:Continue, c:Environment):
        if c.loopNum == 0:
            raise MustInLoop(ast)

    def sameRetTypes(typ1:Type, typ2:Type):
        if type(typ1) is ClassType and type(typ2) is ClassType:
            return typ1.classname.name == typ2.classname.name
        elif type(typ1) is ArrayType and type(typ2) is ArrayType:
            return typ1.size == typ2.size and StaticChecker.sameRetTypes(typ1.eleType, typ2.eleType)
        elif type(typ1) is type(typ2):
            return True

    def visitReturn(self, ast:Return, c:Environment):
        typ = NoneType() if not ast.expr else self.visit(ast.expr,c)[0]
        if not c.currentMethod.retType:
            c.currentMethod.retType = typ
        elif not StaticChecker.sameRetTypes(typ,c.currentMethod.retType):
            raise TypeMismatchInStatement(ast)

    def visitCallStmt(self, ast:CallStmt, c:Environment):
        c.idKind.append(Class() if ast.method.name[0] == '$' else Identifier())
        objTyp, _ = self.visit(ast.obj,c)
        c.idKind.pop()
        if type(objTyp) is ClassInfo:
            if ast.method.name in objTyp.methods:
                methodInfo = objTyp.methods[ast.method.name]
                if type(methodInfo.method.kind) is Static:
                    StaticChecker.checkparatype(methodInfo.method, ast.param, self, ast)
                    if type(methodInfo.retType) is not NoneType:
                        raise TypeMismatchInStatement(ast)
                    return
            else:
                raise Undeclared(Method(), ast.method.name)
        elif type(objTyp) is ClassType:
            if objTyp.classname.name in c.classList:
                classInfo = c.classList[objTyp.classname.name]
                if ast.method.name in classInfo.methods:
                    methodInfo = classInfo.methods[ast.method.name]
                    if type(methodInfo.method.kind) is Instance:
                        StaticChecker.checkparatype(methodInfo.method, ast.param, self, ast)
                        if type(methodInfo.retType) is not NoneType:
                            raise TypeMismatchInStatement(ast)
                        return
                else:
                    raise Undeclared(Method(), ast.method.name)
            else:
                raise Undeclared(Identifier(), objTyp.classname.name)
        raise TypeMismatchInExpression(ast)