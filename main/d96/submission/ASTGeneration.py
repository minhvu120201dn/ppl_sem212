from array import ArrayType
from ast import expr
from xmlrpc.client import Boolean
from D96Visitor import D96Visitor
from D96Parser import D96Parser
from AST import *
from functools import reduce

from main.d96.utils.AST import AST, ArrayLiteral, AttributeDecl, BinaryOp, BoolType, BooleanLiteral, ClassDecl, ClassType, ConstDecl, FloatLiteral, FloatType, Id, Instance, IntLiteral, IntType, Program, SelfLiteral, Static, StringLiteral, StringType, UnaryOp, VarDecl


class ASTGeneration(D96Visitor):

    def visitProgram(self, ctx:D96Parser.ProgramContext):
        return Program([c.accept(self) for c in ctx.classDecl()])


    def visitClassDecl(self, ctx:D96Parser.ClassDeclContext):
        ret = ClassDecl(classname=Id(ctx.ID(0).getText()),
                        memlist=reduce(lambda l, c: l + c, [c.accept(self) for c in ctx.classMem()], []),
                        parentname=None if len(ctx.ID()) < 2 else Id(ctx.ID(1).getText()))
        if ret.classname.name == 'Program':
            for mem in ret.memlist:
                if type(mem) == MethodDecl:
                    if mem.name.name == 'main' and mem.param == []:
                        mem.kind = Static()
        return ret


    def visitClassMem(self, ctx:D96Parser.ClassMemContext):
        return ctx.attribute().accept(self) if ctx.attribute() else ctx.method().accept(self)


    def visitAttribute(self, ctx:D96Parser.AttributeContext):
        mutable = True if ctx.VAR_() else False
        vars, inits, type = ctx.attrBody().accept(self) if ctx.attrBody() else\
                            ctx.attrNonInit().accept(self)
        vars.reverse() if ctx.attrBody() else None

        return [( AttributeDecl(kind=Static() if vars[i].name[0] == '$' else Instance(),
                                decl=VarDecl  (vars[i], type, inits[i]) if mutable else\
                                     ConstDecl(vars[i], type, inits[i]) ) )
                for i in range(len(vars))]


    def visitAttrBody(self, ctx:D96Parser.AttrBodyContext):
        vars, inits, type = None, None, None
        if ctx.attrBody():
            vars, inits, type = ctx.attrBody().accept(self)
            vars.append(ctx.identifier().accept(self))
            inits.append(ctx.expr().accept(self))
        elif ctx.ASNOP():
            vars = [ctx.identifier().accept(self)]
            inits = [ctx.expr().accept(self)]
            type = ctx.vartype().accept(self)
        return vars, inits, type


    def visitAttrNonInit(self, ctx:D96Parser.AttrNonInitContext):
        vars = [ident.accept(self) for ident in ctx.identifier()]
        inits = [None] * len(ctx.identifier())
        type = ctx.vartype().accept(self)
        return vars, inits, type


    def visitMethod(self, ctx:D96Parser.MethodContext):
        return [ctx.getChild(0).accept(self)]


    def visitNormalMet(self, ctx:D96Parser.NormalMetContext):
        if ctx.VID():
            kind = Static()
            name = Id(ctx.VID().getText())
        else:
            kind = Instance()
            name = Id(ctx.ID().getText())
        return MethodDecl(name= name,
                          kind= kind,
                          param= ctx.paraList().accept(self) if ctx.paraList() else [],
                          body= ctx.scope().accept(self))


    def visitConstructor(self, ctx:D96Parser.ConstructorContext):
        return MethodDecl(name= Id('Constructor'),
                          kind= Instance(),
                          param= ctx.paraList().accept(self) if ctx.paraList() else [],
                          body= ctx.scope().accept(self))


    def visitDestructor(self, ctx:D96Parser.DestructorContext):
        return MethodDecl(name= Id('Destructor'),
                          kind= Instance(),
                          param= [],
                          body= ctx.scope().accept(self))


    def visitParaList(self, ctx:D96Parser.ParaListContext):
        return reduce(lambda l, c: l + c, [idList.accept(self) for idList in ctx.idList()], [])


    def visitIdList(self, ctx:D96Parser.IdListContext):
        type = ctx.vartype().accept(self)
        return [VarDecl(ident.accept(self), type) for ident in ctx.identifier()]


    def visitScope(self, ctx:D96Parser.ScopeContext):
        return Block(reduce(lambda l, c: l+c if type(c)==list else l+[c], [stmt.accept(self) for stmt in ctx.stmt()], []))


    def visitStmt(self, ctx:D96Parser.StmtContext):
        return ctx.getChild(0).accept(self)


    def visitDeclStmt(self, ctx:D96Parser.DeclStmtContext):
        mutable = True if ctx.VAR_() else False
        vars, inits, type = ctx.declBody().accept(self) if ctx.declBody() else\
                            ctx.declNonInit().accept(self)
        vars.reverse() if ctx.declBody() else None

        return [VarDecl  (vars[i], type, inits[i]) if mutable else\
                ConstDecl(vars[i], type, inits[i])
                for i in range(len(vars))]


    def visitDeclBody(self, ctx:D96Parser.DeclBodyContext):
        vars, inits, type = None, None, None
        if ctx.declBody():
            vars, inits, type = ctx.declBody().accept(self)
            vars.append(Id(ctx.ID().getText()))
            inits.append(ctx.expr().accept(self))
        elif ctx.ASNOP():
            vars = [Id(ctx.ID().getText())]
            inits = [ctx.expr().accept(self)]
            type = ctx.vartype().accept(self)
        return vars, inits, type


    def visitDeclNonInit(self, ctx:D96Parser.DeclNonInitContext):
        vars = [Id(ident.getText()) for ident in ctx.ID()]
        inits = [None] * len(ctx.ID())
        type = ctx.vartype().accept(self)
        return vars, inits, type


    def visitIdentifier(self, ctx:D96Parser.IdentifierContext):
        return Id(ctx.ID().getText()) if ctx.ID() else Id(ctx.VID().getText())


    def visitAsnStmt(self, ctx:D96Parser.AsnStmtContext):
        return Assign(ctx.lhs().accept(self), ctx.expr().accept(self))


    def visitLhs(self, ctx:D96Parser.LhsContext):
        if ctx.identifier():
            return ctx.identifier().accept(self)
        elif ctx.SELF_():
            return SelfLiteral()
        elif ctx.LSB() and ctx.RSB():
            return ArrayCell(ctx.lhs().accept(self), [expr.accept(self) for expr in ctx.expr()])
        elif ctx.DOT():
            return FieldAccess(ctx.lhs().accept(self), Id(ctx.ID().getText()))
        elif ctx.CSMEM():
            return FieldAccess(Id(ctx.ID().getText()), Id(ctx.VID().getText()))


    def visitIfStmt(self, ctx:D96Parser.IfStmtContext):
        return If(expr= ctx.expr().accept(self),
                  thenStmt= ctx.scope().accept(self),
                  elseStmt= ctx.elifStmt().accept(self) if ctx.elifStmt() else\
                            ctx.elseStmt().accept(self) if ctx.elseStmt() else\
                            None)


    def visitElifStmt(self, ctx:D96Parser.ElifStmtContext):
        return If(expr= ctx.expr().accept(self),
                  thenStmt= ctx.scope().accept(self),
                  elseStmt= ctx.elifStmt().accept(self) if ctx.elifStmt() else\
                            ctx.elseStmt().accept(self) if ctx.elseStmt() else\
                            None)


    def visitElseStmt(self, ctx:D96Parser.ElseStmtContext):
        return ctx.scope().accept(self)


    def visitForStmt(self, ctx:D96Parser.ForStmtContext):
        exprs = ctx.expr() + [None]
        return For(id= Id(ctx.ID().getText()),
                   expr1= exprs[0].accept(self),
                   expr2= exprs[1].accept(self),
                   loop= ctx.scopeLoop().accept(self),
                   expr3= exprs[2].accept(self))


    def visitScopeLoop(self, ctx:D96Parser.ScopeLoopContext):
        return Block([stmt.accept(self) for stmt in ctx.stmtLoop()])


    def visitStmtLoop(self, ctx:D96Parser.StmtLoopContext):
        return ctx.getChild(0).accept(self)


    def visitIfStmtLoop(self, ctx:D96Parser.IfStmtLoopContext):
        return If(expr= ctx.expr().accept(self),
                  thenStmt= ctx.scopeLoop().accept(self),
                  elseStmt= ctx.elifStmtLoop().accept(self) if ctx.elifStmtLoop() else\
                            ctx.elseStmtLoop().accept(self) if ctx.elseStmtLoop() else\
                            None)


    def visitElifStmtLoop(self, ctx:D96Parser.ElifStmtLoopContext):
        return If(expr= ctx.expr().accept(self),
                  thenStmt= ctx.scopeLoop().accept(self),
                  elseStmt= ctx.elifStmtLoop().accept(self) if ctx.elifStmtLoop() else\
                            ctx.elseStmtLoop().accept(self) if ctx.elseStmtLoop() else\
                            None)


    def visitElseStmtLoop(self, ctx:D96Parser.ElseStmtLoopContext):
        return ctx.scopeLoop().accept(self)


    def visitBreakStmt(self, ctx:D96Parser.BreakStmtContext):
        return Break()


    def visitContStmt(self, ctx:D96Parser.ContStmtContext):
        return Continue()


    def visitInsMetStmt(self, ctx:D96Parser.InsMetStmtContext):
        return CallStmt(obj= ctx.expr().accept(self),
                        method= Id(ctx.ID().getText()),
                        param= ctx.exprList().accept(self))


    def visitStaMetStmt(self, ctx:D96Parser.StaMetStmtContext):
        return CallStmt(obj= Id(ctx.ID().getText()),
                        method= Id(ctx.VID().getText()),
                        param= ctx.exprList().accept(self))


    def visitRetStmt(self, ctx:D96Parser.RetStmtContext):
        return Return(expr= ctx.expr().accept(self) if ctx.expr() else None)


    def visitExpr(self, ctx:D96Parser.ExprContext):
        if ctx.getChildCount() == 1:
            return  ctx.getChild(0).accept(self) if ctx.arrLit() or ctx.identifier() else\
                    IntLiteral(ctx.INTLIT().getText()) if ctx.INTLIT() else\
                    FloatLiteral(ctx.FLOATLIT().getText()) if ctx.FLOATLIT() else\
                    BooleanLiteral(ctx.BOOLLIT().getText()) if ctx.BOOLLIT() else\
                    StringLiteral(ctx.STRLIT().getText()) if ctx.STRLIT() else\
                    NullLiteral() if ctx.NULL_() else\
                    SelfLiteral() if ctx.SELF_() else\
                    None
        elif ctx.LB() and ctx.RB():
            return ctx.expr(0).accept(self)
        elif ctx.NEW_():
            return NewExpr(classname= Id(ctx.ID().getText()),
                           param= ctx.exprList().accept(self))
        elif ctx.CSMEM():
            if ctx.exprList():
                return CallExpr(obj= Id(ctx.ID().getText()),
                                method= Id(ctx.VID().getText()),
                                param= ctx.exprList().accept(self))
            else:
                return FieldAccess(obj= Id(ctx.ID().getText()),
                                   fieldname = Id(ctx.VID().getText()))
        elif ctx.DOT():
            if ctx.exprList():
                return CallExpr(obj= ctx.expr(0).accept(self),
                                method= Id(ctx.ID().getText()),
                                param= ctx.exprList().accept(self))
            else:
                return FieldAccess(obj= ctx.expr(0).accept(self),
                                   fieldname = Id(ctx.ID().getText()))
        elif ctx.LSB() and ctx.RSB():
            expr_list = [e.accept(self) for e in ctx.expr()]
            return ArrayCell(arr= expr_list[0],
                             idx= expr_list[1:])
        elif ctx.getChildCount() == 2:
            return UnaryOp(ctx.getChild(0).getText(), ctx.getChild(1).accept(self))
        elif ctx.getChildCount() == 3:
            return BinaryOp(ctx.getChild(1).getText(), ctx.getChild(0).accept(self), ctx.getChild(2).accept(self))
    
    
    def visitExprList(self, ctx:D96Parser.ExprListContext):
        return [expr.accept(self) for expr in ctx.expr()]


    def visitArrDec(self, ctx:D96Parser.ArrDecContext):
        return ArrayType(size=int(ctx.INTLIT().getText()),
                         eleType=ctx.vartype().accept(self))


    def visitVartype(self, ctx:D96Parser.VartypeContext):
        return  IntType() if ctx.INT_() else\
                FloatType() if ctx.FLOAT_() else\
                BoolType() if ctx.BOOL_() else\
                StringType() if ctx.STR_() else\
                ctx.arrDec().accept(self) if ctx.arrDec() else\
                ClassType(Id(ctx.ID().getText())) if ctx.ID() else\
                None


    def visitArrLit(self, ctx:D96Parser.ArrLitContext):
        return ArrayLiteral(ctx.exprList().accept(self))