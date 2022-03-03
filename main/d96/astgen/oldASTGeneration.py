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
        #TODO: write this function
        return self.visitChildren(ctx)


    def visitConstructor(self, ctx:D96Parser.ConstructorContext):
        #TODO: write this function
        return self.visitChildren(ctx)


    def visitDestructor(self, ctx:D96Parser.DestructorContext):
        #TODO: write this function
        return self.visitChildren(ctx)


    def visitParaList(self, ctx:D96Parser.ParaListContext):
        #TODO: write this function
        return self.visitChildren(ctx)


    def visitIdList(self, ctx:D96Parser.IdListContext):
        #TODO: write this function
        return self.visitChildren(ctx)


    def visitScope(self, ctx:D96Parser.ScopeContext):
        #TODO: write this function
        return self.visitChildren(ctx)


    def visitStmt(self, ctx:D96Parser.StmtContext):
        #TODO: write this function
        return self.visitChildren(ctx)


    def visitDeclare(self, ctx:D96Parser.DeclareContext):
        mutable = True if ctx.VAR_() else False
        vars, inits, type = ctx.declBody().accept(self) if ctx.declBody() else\
                            ctx.notvalBody().accept(self)

        return [( AttributeDecl(kind=Static() if vars[i].name[0] == '$' else Instance(),
                                decl=VarDecl  (vars[i], type, inits[i]) if mutable else\
                                     ConstDecl(vars[i], type, inits[i]) ) )
                for i in range(len(vars))]


    def visitDeclBody(self, ctx:D96Parser.DeclBodyContext):
        if ctx.decmemInt():
            vars, inits, type = ctx.decmemInt().accept(self)
        elif ctx.decmemNum():
            vars, inits, type = ctx.decmemNum().accept(self)
        elif ctx.decmemBool():
            vars, inits, type = ctx.decmemBool().accept(self)
        elif ctx.decmemStr():
            vars, inits, type = ctx.decmemStr().accept(self)
        elif ctx.decmemArr():
            vars, inits, type = ctx.decmemArr().accept(self)
        vars.reverse()
        return vars, inits, type


    def visitNotvalBody(self, ctx:D96Parser.NotvalBodyContext):
        if ctx.declIntvar():
            vars, inits, type = ctx.declIntvar().accept(self)
        elif ctx.declNumvar():
            vars, inits, type = ctx.declNumvar().accept(self)
        elif ctx.declBoolvar():
            vars, inits, type = ctx.declBoolvar().accept(self)
        elif ctx.declStrvar():
            vars, inits, type = ctx.declStrvar().accept(self)
        elif ctx.declArrvar():
            vars, inits, type = ctx.declArrvar().accept(self)
        vars.reverse()
        return vars, inits, type


    def decmem(self, ctx, visitfunc, expr):
        vars, inits, type = None, None, None
        if visitfunc():
            vars, inits, type = visitfunc().accept(self)
            vars.append(ctx.identifier().accept(self))
            inits.append(expr().accept(self))
        elif ctx.ASNOP():
            vars = [ctx.identifier().accept(self)]
            inits = [expr().accept(self)]
        return vars, inits, type


    def decvarmem(self, ctx):
        vars = [ident.accept(self) for ident in ctx.identifier()]
        vars.reverse()
        inits = [None] * len(ctx.identifier())
        return vars, inits


    def visitDecmemInt(self, ctx:D96Parser.DecmemIntContext):
        vars, inits, type = self.decmem(ctx, ctx.decmemInt, ctx.intExpr)
        return vars, inits, type if type else IntType()


    def visitDeclIntvar(self, ctx:D96Parser.DeclIntvarContext):
        vars, inits = self.decvarmem(ctx)
        return vars, inits, IntType()


    def visitDecmemNum(self, ctx:D96Parser.DecmemNumContext):
        vars, inits, type = self.decmem(ctx, ctx.decmemNum, ctx.numExpr)
        return vars, inits, type if type else FloatType()


    def visitDeclNumvar(self, ctx:D96Parser.DeclNumvarContext):
        vars, inits = self.decvarmem(ctx)
        return vars, inits, FloatType()


    def visitDecmemStr(self, ctx:D96Parser.DecmemStrContext):
        vars, inits, type = self.decmem(ctx, ctx.decmemStr, ctx.strExpr)
        return vars, inits, type if type else StringType()


    def visitDeclStrvar(self, ctx:D96Parser.DeclStrvarContext):
        vars, inits = self.decvarmem(ctx)
        return vars, inits, StringType()


    def visitDecmemBool(self, ctx:D96Parser.DecmemBoolContext):
        vars, inits, type = self.decmem(ctx, ctx.decmemBool, ctx.boolExpr)
        return vars, inits, type if type else BoolType()


    def visitDeclBoolvar(self, ctx:D96Parser.DeclBoolvarContext):
        vars, inits = self.decvarmem(ctx)
        return vars, inits, BoolType()


    def visitDecmemArr(self, ctx:D96Parser.DecmemArrContext):
        vars, inits, type = self.decmem(ctx, ctx.decmemArr, ctx.arrExpr)
        return vars, inits, type if type else ctx.arrDec().accept(self)


    def visitDeclArrvar(self, ctx:D96Parser.DeclArrvarContext):
        vars, inits = self.decvarmem(ctx)
        return vars, inits, ctx.arrDec().accept(self)


    def visitDecmemObj(self, ctx:D96Parser.DecmemObjContext):
        return self.decmem(ctx, ctx.decmemObj, ctx.objExpr)


    def visitDeclObjvar(self, ctx:D96Parser.DeclObjvarContext):
        #TODO: write this function
        return self.visitChildren(ctx)


    def visitIdentifier(self, ctx:D96Parser.IdentifierContext):
        return Id(ctx.ID().getText()) if ctx.ID() else Id(ctx.VID().getText())


    def visitAsnStmt(self, ctx:D96Parser.AsnStmtContext):
        #TODO: write this function
        return self.visitChildren(ctx)


    def visitIfStmt(self, ctx:D96Parser.IfStmtContext):
        #TODO: write this function
        return self.visitChildren(ctx)


    def visitForStmt(self, ctx:D96Parser.ForStmtContext):
        #TODO: write this function
        return self.visitChildren(ctx)


    def visitScopeLoop(self, ctx:D96Parser.ScopeLoopContext):
        #TODO: write this function
        return self.visitChildren(ctx)


    def visitStmtLoop(self, ctx:D96Parser.StmtLoopContext):
        #TODO: write this function
        return self.visitChildren(ctx)


    def visitIfStmtLoop(self, ctx:D96Parser.IfStmtLoopContext):
        #TODO: write this function
        return self.visitChildren(ctx)


    def visitBreakStmt(self, ctx:D96Parser.BreakStmtContext):
        #TODO: write this function
        return self.visitChildren(ctx)


    def visitContStmt(self, ctx:D96Parser.ContStmtContext):
        #TODO: write this function
        return self.visitChildren(ctx)


    def visitInsAttr(self, ctx:D96Parser.InsAttrContext):
        #TODO: write this function
        return self.visitChildren(ctx)


    def visitStaAttr(self, ctx:D96Parser.StaAttrContext):
        #TODO: write this function
        return self.visitChildren(ctx)


    def visitInsMethod(self, ctx:D96Parser.InsMethodContext):
        #TODO: write this function
        return self.visitChildren(ctx)


    def visitStaMethod(self, ctx:D96Parser.StaMethodContext):
        #TODO: write this function
        return self.visitChildren(ctx)


    def visitCallMethod(self, ctx:D96Parser.CallMethodContext):
        #TODO: write this function
        return self.visitChildren(ctx)


    def visitRetStmt(self, ctx:D96Parser.RetStmtContext):
        #TODO: write this function
        return self.visitChildren(ctx)


    def visitExpr(self, ctx:D96Parser.ExprContext):
        return  ctx.intExpr().accept(self) if ctx.intExpr() else\
                ctx.numExpr().accept(self) if ctx.numExpr() else\
                ctx.boolExpr().accept(self) if ctx.boolExpr() else\
                ctx.arrExpr().accept(self) if ctx.arrExpr() else\
                ctx.eleExpr().accept(self) if ctx.eleExpr() else\
                ctx.objExpr().accept(self) if ctx.objExpr() else\
                None


    def visitIntExpr(self, ctx:D96Parser.IntExprContext):
        if ctx.getChildCount() == 1:
            return IntLiteral(ctx.INTLIT().getText()) if ctx.INTLIT() else\
                   ctx.getChild(0).accept(self)
        elif ctx.LB() and ctx.RB():
            return ctx.intExpr(0).accept(self)
        elif ctx.getChildCount() == 2 and ctx.SUBOP():
            return UnaryOp(ctx.SUBOP().getText(), ctx.intExpr(0).accept(self))
        elif ctx.getChildCount() == 3:
            return BinaryOp(ctx.getChild(1).getText(), ctx.intExpr(0).accept(self), ctx.intExpr(1).accept(self))


    def visitNumExpr(self, ctx:D96Parser.NumExprContext):
        if ctx.getChildCount() == 1:
            return FloatLiteral(ctx.FLOATLIT().getText()) if ctx.FLOATLIT() else\
                   IntLiteral(ctx.INTLIT().getText()) if ctx.INTLIT() else\
                   ctx.getChild(0).accept(self)
        elif ctx.LB() and ctx.RB():
            return ctx.numExpr(0).accept(self)
        elif ctx.getChildCount() == 2 and ctx.SUBOP():
            return UnaryOp(ctx.SUBOP().getText(), ctx.numExpr(0).accept(self))
        elif ctx.getChildCount() == 3:
            return BinaryOp(ctx.getChild(1).getText(), ctx.numExpr(0).accept(self), ctx.numExpr(1).accept(self))


    def visitStrExpr(self, ctx:D96Parser.StrExprContext):
        if ctx.getChildCount() == 1:
            return StringLiteral(ctx.STRLIT().getText()) if ctx.STRLIT() else\
                   ctx.getChild(0).accept(self)
        elif ctx.LB() and ctx.RB():
            return ctx.strExpr(0).accept(self)
        elif ctx.getChildCount() == 3:
            return BinaryOp(ctx.getChild(1).getText(), ctx.strExpr(0).accept(self), ctx.strExpr(1).accept(self))


    def visitBoolExpr(self, ctx:D96Parser.BoolExprContext):
        if ctx.getChildCount() == 1:
            return BooleanLiteral(ctx.BOOLLIT().getText()) if ctx.BOOLLIT() else\
                   ctx.getChild(0).accept(self)
        elif ctx.LB() and ctx.RB():
            return ctx.boolExpr(0).accept(self)
        elif ctx.getChildCount() == 2 and ctx.NOTOP():
            return UnaryOp(ctx.NOTOP().getText(), ctx.boolExpr(0).accept(self))
        elif ctx.getChildCount() == 3:
            return BinaryOp(ctx.getChild(1).getText(), ctx.getChild(0).accept(self), ctx.getChild(2).accept(self))


    def visitArrExpr(self, ctx:D96Parser.ArrExprContext):
        #TODO: write this function
        return self.visitChildren(ctx)


    def visitObjExpr(self, ctx:D96Parser.ObjExprContext):
        #TODO: write this function
        return self.visitChildren(ctx)


    def visitEleExpr(self, ctx:D96Parser.EleExprContext):
        #TODO: write this function
        return self.visitChildren(ctx)


    def visitArrDec(self, ctx:D96Parser.ArrDecContext):
        return ArrayType(size=int(ctx.INTLIT().getText()),
                         eleType=ctx.vartype().accept(self))


    def visitVartype(self, ctx:D96Parser.VartypeContext):
        return  IntType() if ctx.INT_() else\
                FloatType() if ctx.FLOAT_() else\
                BoolType() if ctx.BOOL_() else\
                StringType() if ctx.STR_() else\
                ClassType(Id(ctx.ID().getText())) if ctx.ID() else\
                ctx.arrDec().accept(self) if ctx.arrDec() else\
                None


    def visitArrLit(self, ctx:D96Parser.ArrLitContext):
        return ArrayLiteral([expr.accept(self) for expr in ctx.expr()])