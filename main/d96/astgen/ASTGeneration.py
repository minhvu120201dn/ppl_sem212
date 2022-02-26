from array import ArrayType
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
        return ClassDecl(classname=Id(ctx.ID(0).getText()),
                         memlist=reduce(lambda l, c: l + c, [c.accept(self) for c in ctx.classMem()], []),
                         parentname=None if len(ctx.ID()) < 2 else Id(ctx.ID(1).getText()))


    def visitClassMem(self, ctx:D96Parser.ClassMemContext):
        return ctx.attribute().accept(self) if ctx.attribute() else ctx.method().accept(self)


    def visitAttribute(self, ctx:D96Parser.AttributeContext):
        return ctx.declare().accept(self)


    def visitMethod(self, ctx:D96Parser.MethodContext):
        return self.visitChildren(ctx)
        #TODO: write this function


    def visitConstructor(self, ctx:D96Parser.ConstructorContext):
        return self.visitChildren(ctx)
        #TODO: write this function


    def visitDestructor(self, ctx:D96Parser.DestructorContext):
        return self.visitChildren(ctx)
        #TODO: write this function


    def visitParaList(self, ctx:D96Parser.ParaListContext):
        return self.visitChildren(ctx)
        #TODO: write this function


    def visitIdList(self, ctx:D96Parser.IdListContext):
        return self.visitChildren(ctx)
        #TODO: write this function


    def visitScope(self, ctx:D96Parser.ScopeContext):
        return self.visitChildren(ctx)
        #TODO: write this function


    def visitStmt(self, ctx:D96Parser.StmtContext):
        return self.visitChildren(ctx)
        #TODO: write this function


    def visitDeclare(self, ctx:D96Parser.DeclareContext):
        mutable = True if ctx.VAR_() else False
        vars, inits, type = ctx.declBody().accept(self) if ctx.declBody() else\
                            ctx.notvalBody().accept(self)
        vars.reverse() if ctx.declBody() else None

        return [( AttributeDecl(kind=Static() if vars[i].name[0] == '$' else Instance(),
                                decl=VarDecl  (vars[i], type, inits[i]) if mutable else\
                                     ConstDecl(vars[i], type, inits[i]) ) )
                for i in range(len(vars))]


    def visitDeclBody(self, ctx:D96Parser.DeclBodyContext):
        vars, inits, type = None, None, None
        if ctx.declBody():
            vars, inits, type = ctx.declBody().accept(self)
            vars.append(ctx.identifier().accept(self))
            inits.append(ctx.expr().accept(self))
        elif ctx.ASNOP():
            vars = [ctx.identifier().accept(self)]
            inits = [ctx.expr().accept(self)]
            type = ctx.vartype().accept(self)
        return vars, inits, type


    def visitNotvalBody(self, ctx:D96Parser.NotvalBodyContext):
        vars = [ident.accept(self) for ident in ctx.identifier()]
        inits = [None] * len(ctx.identifier())
        type = ctx.vartype().accept(self)
        return vars, inits, type;


    def visitIdentifier(self, ctx:D96Parser.IdentifierContext):
        return Id(ctx.ID().getText()) if ctx.ID() else Id(ctx.VID().getText())


    def visitAsnStmt(self, ctx:D96Parser.AsnStmtContext):
        return self.visitChildren(ctx)
        #TODO: write this function


    def visitLhs(self, ctx:D96Parser.LhsContext):
        return self.visitChildren(ctx)
        #TODO: write this function


    def visitIfStmt(self, ctx:D96Parser.IfStmtContext):
        return self.visitChildren(ctx)
        #TODO: write this function


    def visitForStmt(self, ctx:D96Parser.ForStmtContext):
        return self.visitChildren(ctx)
        #TODO: write this function


    def visitScopeLoop(self, ctx:D96Parser.ScopeLoopContext):
        return self.visitChildren(ctx)
        #TODO: write this function


    def visitStmtLoop(self, ctx:D96Parser.StmtLoopContext):
        return self.visitChildren(ctx)
        #TODO: write this function


    def visitIfStmtLoop(self, ctx:D96Parser.IfStmtLoopContext):
        return self.visitChildren(ctx)
        #TODO: write this function


    def visitBreakStmt(self, ctx:D96Parser.BreakStmtContext):
        return self.visitChildren(ctx)
        #TODO: write this function


    def visitContStmt(self, ctx:D96Parser.ContStmtContext):
        return self.visitChildren(ctx)
        #TODO: write this function


    def visitCallMethod(self, ctx:D96Parser.CallMethodContext):
        return self.visitChildren(ctx)
        #TODO: write this function


    def visitRetStmt(self, ctx:D96Parser.RetStmtContext):
        return self.visitChildren(ctx)
        #TODO: write this function


    def visitExpr(self, ctx:D96Parser.ExprContext):
        if ctx.getChildCount() == 1:
            return  ctx.getChild(0).accept(self) if ctx.arrLit() or ctx.identifier() or ctx.callMethod() else\
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
            return NewExpr(classname= ctx.ID().getText(),
                           param= ctx.exprList().accept(self))
        elif ctx.CSMEM():
            pass
        elif ctx.DOT():
            pass
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