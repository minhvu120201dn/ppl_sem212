# Generated from main/d96/parser/D96.g4 by ANTLR 4.9.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .D96Parser import D96Parser
else:
    from D96Parser import D96Parser

# This class defines a complete generic visitor for a parse tree produced by D96Parser.

class D96Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by D96Parser#program.
    def visitProgram(self, ctx:D96Parser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#classDecl.
    def visitClassDecl(self, ctx:D96Parser.ClassDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#classMem.
    def visitClassMem(self, ctx:D96Parser.ClassMemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#attribute.
    def visitAttribute(self, ctx:D96Parser.AttributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#attrBody.
    def visitAttrBody(self, ctx:D96Parser.AttrBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#attrNonInit.
    def visitAttrNonInit(self, ctx:D96Parser.AttrNonInitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#method.
    def visitMethod(self, ctx:D96Parser.MethodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#normalMet.
    def visitNormalMet(self, ctx:D96Parser.NormalMetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#constructor.
    def visitConstructor(self, ctx:D96Parser.ConstructorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#destructor.
    def visitDestructor(self, ctx:D96Parser.DestructorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#paraList.
    def visitParaList(self, ctx:D96Parser.ParaListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#idList.
    def visitIdList(self, ctx:D96Parser.IdListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#scope.
    def visitScope(self, ctx:D96Parser.ScopeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#stmt.
    def visitStmt(self, ctx:D96Parser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#declStmt.
    def visitDeclStmt(self, ctx:D96Parser.DeclStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#declBody.
    def visitDeclBody(self, ctx:D96Parser.DeclBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#declNonInit.
    def visitDeclNonInit(self, ctx:D96Parser.DeclNonInitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#identifier.
    def visitIdentifier(self, ctx:D96Parser.IdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#asnStmt.
    def visitAsnStmt(self, ctx:D96Parser.AsnStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#lhs.
    def visitLhs(self, ctx:D96Parser.LhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#ifStmt.
    def visitIfStmt(self, ctx:D96Parser.IfStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#elifStmt.
    def visitElifStmt(self, ctx:D96Parser.ElifStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#elseStmt.
    def visitElseStmt(self, ctx:D96Parser.ElseStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#forStmt.
    def visitForStmt(self, ctx:D96Parser.ForStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#breakStmt.
    def visitBreakStmt(self, ctx:D96Parser.BreakStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#contStmt.
    def visitContStmt(self, ctx:D96Parser.ContStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#insMetStmt.
    def visitInsMetStmt(self, ctx:D96Parser.InsMetStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#staMetStmt.
    def visitStaMetStmt(self, ctx:D96Parser.StaMetStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#retStmt.
    def visitRetStmt(self, ctx:D96Parser.RetStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr.
    def visitExpr(self, ctx:D96Parser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exprList.
    def visitExprList(self, ctx:D96Parser.ExprListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#arrDec.
    def visitArrDec(self, ctx:D96Parser.ArrDecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#vartype.
    def visitVartype(self, ctx:D96Parser.VartypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#arrLit.
    def visitArrLit(self, ctx:D96Parser.ArrLitContext):
        return self.visitChildren(ctx)



del D96Parser