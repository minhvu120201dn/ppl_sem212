
"""
 * @author nhphung
"""
from msilib.schema import Binary
from AST import * 
from Visitor import *
from Utils import Utils
from StaticError import *

# class MType:
#     def __init__(self,partype,rettype):
#         self.partype = partype
#         self.rettype = rettype

# class Symbol:
#     def __init__(self,name,mtype,value = None):
#         self.name = name
#         self.mtype = mtype
#         self.value = value

class StaticChecker(BaseVisitor,Utils):

    def __init__(self,ast):
        self.ast = ast
 
    
    def check(self):
        return self.visit(self.ast,None)

    def visitProgram(self, ast:Program, c):
        ids = [{'#ProgramClass': False, '#mainFunc': False, '#inProgram': False}]
        for x in ast.decl:
            self.visit(x,ids)
        if not ids[0]['#mainFunc']:
            raise NoEntryPoint()
        return ''

    def visitClassDecl(self, ast:ClassDecl, ids:List[dict]):
        if ast.classname.name in ids[-1]:
            raise Redeclared(Class(), ast.classname.name)
        ids[-1][ast.classname.name] = ast
        if ast.classname.name == 'Program':
            ids[0]['#ProgramClass'] = True
            ids[0]['#inProgram'] = True
        if ast.parentname and ast.parentname.name not in ids[-1]:
            raise Undeclared(Class(), ast.parentname.name)
        ids.append({})
        for x in ast.memlist:
            self.visit(x,ids)
        ids.pop()
        ids[0]['#inProgram'] = False

    def visitAttributeDecl(self, ast:AttributeDecl, ids:List[dict]):
        id = self.visit(ast.decl, ids)
        if id:
            raise Redeclared(Attribute(), id)

    def visitMethodDecl(self, ast:MethodDecl, ids:List[dict]):
        returnType = None
        ids[-1][ast.name.name] = ast
        if ast.name.name == 'main' and ids[0]['#inProgram']:
            ids[0]['#mainFunc'] = True
        ids.append({})
        for p in ast.param:
            self.visit(p,ids)
        self.visit(ast.body,ids)
        ids.pop()

    def sameTypes(typ1:Type, typ2:Type):
        if type(typ1) is VoidType or type(typ2) is VoidType:
            return True
        elif type(typ1) is ClassType and type(typ2) is ClassType:
            return typ1.classname.name == typ2.classname.name
        elif type(typ1) is ArrayType and type(typ2) is ArrayType:
            return typ1.size == typ2.size and StaticChecker.sameTypes(typ1.eleType, typ2.eleType)
        elif type(typ1) is type(typ2):
            return True

    def visitVarDecl(self, ast:VarDecl, ids:List[dict]):
        if ast.variable.name in ids[-1]:
            return ast.variable.name
        ids[-1][ast.variable.name] = ast
        self.visit(ast.varType,ids)
        if ast.varInit:
            if not StaticChecker.sameTypes(self.visit(ast.varType,ids),self.visit(ast.varInit,ids)[0]):
                raise TypeMismatchInStatement(ast)

    def visitConstDecl(self, ast:ConstDecl, ids:List[dict]):
        if ast.constant.name in ids[-1]:
            return ast.constant.name
        ids[-1][ast.constant.name] = ast
        self.visit(ast.constType,ids)
        if ast.value:
            typ, decl = self.visit(ast.value,ids)
            if not StaticChecker.sameTypes(self.visit(ast.constType,ids),typ):
                raise TypeMismatchInConstant(ast)
            if decl is VarDecl:
                raise IllegalConstantExpression(ast.value) #TODO: this needs to be considered again
        else:
            raise IllegalConstantExpression(ast.value)

    def visitIntType(self, ast:IntType, ids:List[dict]):
        return ast

    def visitFloatType(self, ast:FloatType, ids:List[dict]):
        return ast

    def visitBoolType(self, ast:BoolType, ids:List[dict]):
        return ast

    def visitStringType(self, ast:StringType, ids:List[dict]):
        return ast

    def visitArrayType(self, ast:ArrayType, ids:List[dict]):
        self.visit(ast.eleType, ids)
        return ast

    def visitClassType(self, ast:ClassType, ids:List[dict]):
        if ast.classname.name in ids[0]:
            if type(ids[0][ast.classname.name]) == ClassDecl:
                return ast
        raise Undeclared(Class(), ast.classname.name)

    def visitIntLiteral(self, ast:IntLiteral, ids:List[dict]):
        return IntType(), ConstDecl

    def visitFloatLiteral(self, ast:FloatLiteral, ids:List[dict]):
        return FloatType(), ConstDecl

    def visitStringLiteral(self, ast:StringLiteral, ids:List[dict]):
        return StringType(), ConstDecl

    def visitBooleanLiteral(self, ast:BooleanLiteral, ids:List[dict]):
        return BoolType(), ConstDecl

    def visitNullLiteral(self, ast:NullLiteral, ids:List[dict]):
        return VoidType(), ConstDecl

    def visitArrayLiteral(self, ast:ArrayLiteral, ids:List[dict]):
        size = len(ast.value)
        if size == 0:
            return ArrayType(0,None), ConstDecl

        typ, decl = self.visit(ast.value[0],ids)
        for mem in ast.value:
            t, d = self.visit(mem,ids)
            if type(typ) != type(t):
                raise IllegalArrayLiteral(ast)
            if d is VarDecl:
                decl = VarDecl
        return ArrayType(size,typ), decl
    
    def visitId(self, ast:Id, ids:List[dict]):
        for scope in reversed(ids):
            if ast.name in scope:
                decl = scope[ast.name]
                if type(decl) is ConstDecl:
                    return decl.constType, ConstDecl
                elif type(decl) is VarDecl:
                    return decl.varType, VarDecl
        raise Undeclared(Identifier(),ast.name)

    def visitBinaryOp(self, ast:BinaryOp, ids:List[dict]):
        left, ld = self.visit(ast.left, ids)
        right, rd = self.visit(ast.right, ids)
        d = ConstDecl if ld is ConstDecl and rd is ConstDecl else VarDecl
        if ast.op in ('+','-','*','/'):
            if type(left) is IntType and type(right) is IntType:
                return IntType(), d
            elif type(left) in (IntType, FloatType) and type(right) in (IntType, FloatType):
                return FloatType(), d
        elif ast.op in ('%'):
            if type(left) is IntType and type(right) is IntType:
                return IntType(), d
        elif ast.op in ('!','&&','||'):
            if type(left) is BoolType and type(right) is BoolType:
                return BoolType(), d
        elif ast.op == '==.': # Special case. <<< '==' in ('==.') >>> is true
            if type(left) is StringType and type(right) is StringType:
                return BoolType(), d
        elif ast.op in ('+.'):
            if type(left) is StringType and type(right) is StringType:
                return StringType(), d
        elif ast.op in ('==','!='):
            if (type(left) is IntType and type(right) is IntType) or (type(left) is BoolType and type(right) is BoolType):
                return BoolType(), d
        elif ast.op in ('<','<=','>','>='):
            if type(left) in (IntType, FloatType) and type(right) in (IntType, FloatType):
                return BoolType(), d
        raise TypeMismatchInExpression(ast)
    
    def visitUnaryOp(self, ast:UnaryOp, ids:List[dict]):
        body, d = self.visit(ast.body, ids)
        if ast.op in ('-'):
            if type(body) in (IntType, FloatType):
                return type(body)(), d
        elif ast.op in ('!'):
            if type(body) is BoolType:
                return BoolType(), d
        raise TypeMismatchInExpression(ast)

    def visitCallExpr(self, ast:CallExpr, ids:List[dict]):
        pass #TODO
    
    def visitNewExpr(self, ast:NewExpr, ids:List[dict]):
        pass #TODO

    def visitFieldAccess(self, ast:FieldAccess, ids:List[dict]):
        pass #TODO

    def visitArrayCell(self, ast:ArrayCell, ids:List[dict]):
        decl = ConstDecl
        for e in ast.idx:
            t, d = self.visit(e,ids)
            if not type(t) is IntType:
                raise TypeMismatchInExpression(ast)
            if d is VarDecl:
                decl = VarDecl
        typ, decl0 = self.visit(ast.arr,ids)
        if decl0 is VarDecl:
            decl = VarDecl
        for _ in range(len(ast.idx)):
            if type(typ) is ArrayType:
                typ = typ.eleType
            else:
                raise TypeMismatchInExpression(ast)
        return typ, decl