# Generated from G:/sem_212/ppl/assignment/src/main/d96/parser\D96.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .D96Parser import D96Parser
else:
    from D96Parser import D96Parser

# This class defines a complete listener for a parse tree produced by D96Parser.
class D96Listener(ParseTreeListener):

    # Enter a parse tree produced by D96Parser#program.
    def enterProgram(self, ctx:D96Parser.ProgramContext):
        pass

    # Exit a parse tree produced by D96Parser#program.
    def exitProgram(self, ctx:D96Parser.ProgramContext):
        pass


    # Enter a parse tree produced by D96Parser#classDecl.
    def enterClassDecl(self, ctx:D96Parser.ClassDeclContext):
        pass

    # Exit a parse tree produced by D96Parser#classDecl.
    def exitClassDecl(self, ctx:D96Parser.ClassDeclContext):
        pass


    # Enter a parse tree produced by D96Parser#classMem.
    def enterClassMem(self, ctx:D96Parser.ClassMemContext):
        pass

    # Exit a parse tree produced by D96Parser#classMem.
    def exitClassMem(self, ctx:D96Parser.ClassMemContext):
        pass


    # Enter a parse tree produced by D96Parser#attribute.
    def enterAttribute(self, ctx:D96Parser.AttributeContext):
        pass

    # Exit a parse tree produced by D96Parser#attribute.
    def exitAttribute(self, ctx:D96Parser.AttributeContext):
        pass


    # Enter a parse tree produced by D96Parser#attrBody.
    def enterAttrBody(self, ctx:D96Parser.AttrBodyContext):
        pass

    # Exit a parse tree produced by D96Parser#attrBody.
    def exitAttrBody(self, ctx:D96Parser.AttrBodyContext):
        pass


    # Enter a parse tree produced by D96Parser#attrNonInit.
    def enterAttrNonInit(self, ctx:D96Parser.AttrNonInitContext):
        pass

    # Exit a parse tree produced by D96Parser#attrNonInit.
    def exitAttrNonInit(self, ctx:D96Parser.AttrNonInitContext):
        pass


    # Enter a parse tree produced by D96Parser#method.
    def enterMethod(self, ctx:D96Parser.MethodContext):
        pass

    # Exit a parse tree produced by D96Parser#method.
    def exitMethod(self, ctx:D96Parser.MethodContext):
        pass


    # Enter a parse tree produced by D96Parser#normalMet.
    def enterNormalMet(self, ctx:D96Parser.NormalMetContext):
        pass

    # Exit a parse tree produced by D96Parser#normalMet.
    def exitNormalMet(self, ctx:D96Parser.NormalMetContext):
        pass


    # Enter a parse tree produced by D96Parser#constructor.
    def enterConstructor(self, ctx:D96Parser.ConstructorContext):
        pass

    # Exit a parse tree produced by D96Parser#constructor.
    def exitConstructor(self, ctx:D96Parser.ConstructorContext):
        pass


    # Enter a parse tree produced by D96Parser#destructor.
    def enterDestructor(self, ctx:D96Parser.DestructorContext):
        pass

    # Exit a parse tree produced by D96Parser#destructor.
    def exitDestructor(self, ctx:D96Parser.DestructorContext):
        pass


    # Enter a parse tree produced by D96Parser#paraList.
    def enterParaList(self, ctx:D96Parser.ParaListContext):
        pass

    # Exit a parse tree produced by D96Parser#paraList.
    def exitParaList(self, ctx:D96Parser.ParaListContext):
        pass


    # Enter a parse tree produced by D96Parser#idList.
    def enterIdList(self, ctx:D96Parser.IdListContext):
        pass

    # Exit a parse tree produced by D96Parser#idList.
    def exitIdList(self, ctx:D96Parser.IdListContext):
        pass


    # Enter a parse tree produced by D96Parser#scope.
    def enterScope(self, ctx:D96Parser.ScopeContext):
        pass

    # Exit a parse tree produced by D96Parser#scope.
    def exitScope(self, ctx:D96Parser.ScopeContext):
        pass


    # Enter a parse tree produced by D96Parser#stmt.
    def enterStmt(self, ctx:D96Parser.StmtContext):
        pass

    # Exit a parse tree produced by D96Parser#stmt.
    def exitStmt(self, ctx:D96Parser.StmtContext):
        pass


    # Enter a parse tree produced by D96Parser#declStmt.
    def enterDeclStmt(self, ctx:D96Parser.DeclStmtContext):
        pass

    # Exit a parse tree produced by D96Parser#declStmt.
    def exitDeclStmt(self, ctx:D96Parser.DeclStmtContext):
        pass


    # Enter a parse tree produced by D96Parser#declBody.
    def enterDeclBody(self, ctx:D96Parser.DeclBodyContext):
        pass

    # Exit a parse tree produced by D96Parser#declBody.
    def exitDeclBody(self, ctx:D96Parser.DeclBodyContext):
        pass


    # Enter a parse tree produced by D96Parser#declNonInit.
    def enterDeclNonInit(self, ctx:D96Parser.DeclNonInitContext):
        pass

    # Exit a parse tree produced by D96Parser#declNonInit.
    def exitDeclNonInit(self, ctx:D96Parser.DeclNonInitContext):
        pass


    # Enter a parse tree produced by D96Parser#identifier.
    def enterIdentifier(self, ctx:D96Parser.IdentifierContext):
        pass

    # Exit a parse tree produced by D96Parser#identifier.
    def exitIdentifier(self, ctx:D96Parser.IdentifierContext):
        pass


    # Enter a parse tree produced by D96Parser#asnStmt.
    def enterAsnStmt(self, ctx:D96Parser.AsnStmtContext):
        pass

    # Exit a parse tree produced by D96Parser#asnStmt.
    def exitAsnStmt(self, ctx:D96Parser.AsnStmtContext):
        pass


    # Enter a parse tree produced by D96Parser#lhs.
    def enterLhs(self, ctx:D96Parser.LhsContext):
        pass

    # Exit a parse tree produced by D96Parser#lhs.
    def exitLhs(self, ctx:D96Parser.LhsContext):
        pass


    # Enter a parse tree produced by D96Parser#ifStmt.
    def enterIfStmt(self, ctx:D96Parser.IfStmtContext):
        pass

    # Exit a parse tree produced by D96Parser#ifStmt.
    def exitIfStmt(self, ctx:D96Parser.IfStmtContext):
        pass


    # Enter a parse tree produced by D96Parser#elifStmt.
    def enterElifStmt(self, ctx:D96Parser.ElifStmtContext):
        pass

    # Exit a parse tree produced by D96Parser#elifStmt.
    def exitElifStmt(self, ctx:D96Parser.ElifStmtContext):
        pass


    # Enter a parse tree produced by D96Parser#elseStmt.
    def enterElseStmt(self, ctx:D96Parser.ElseStmtContext):
        pass

    # Exit a parse tree produced by D96Parser#elseStmt.
    def exitElseStmt(self, ctx:D96Parser.ElseStmtContext):
        pass


    # Enter a parse tree produced by D96Parser#forStmt.
    def enterForStmt(self, ctx:D96Parser.ForStmtContext):
        pass

    # Exit a parse tree produced by D96Parser#forStmt.
    def exitForStmt(self, ctx:D96Parser.ForStmtContext):
        pass


    # Enter a parse tree produced by D96Parser#breakStmt.
    def enterBreakStmt(self, ctx:D96Parser.BreakStmtContext):
        pass

    # Exit a parse tree produced by D96Parser#breakStmt.
    def exitBreakStmt(self, ctx:D96Parser.BreakStmtContext):
        pass


    # Enter a parse tree produced by D96Parser#contStmt.
    def enterContStmt(self, ctx:D96Parser.ContStmtContext):
        pass

    # Exit a parse tree produced by D96Parser#contStmt.
    def exitContStmt(self, ctx:D96Parser.ContStmtContext):
        pass


    # Enter a parse tree produced by D96Parser#insMetStmt.
    def enterInsMetStmt(self, ctx:D96Parser.InsMetStmtContext):
        pass

    # Exit a parse tree produced by D96Parser#insMetStmt.
    def exitInsMetStmt(self, ctx:D96Parser.InsMetStmtContext):
        pass


    # Enter a parse tree produced by D96Parser#staMetStmt.
    def enterStaMetStmt(self, ctx:D96Parser.StaMetStmtContext):
        pass

    # Exit a parse tree produced by D96Parser#staMetStmt.
    def exitStaMetStmt(self, ctx:D96Parser.StaMetStmtContext):
        pass


    # Enter a parse tree produced by D96Parser#retStmt.
    def enterRetStmt(self, ctx:D96Parser.RetStmtContext):
        pass

    # Exit a parse tree produced by D96Parser#retStmt.
    def exitRetStmt(self, ctx:D96Parser.RetStmtContext):
        pass


    # Enter a parse tree produced by D96Parser#expr.
    def enterExpr(self, ctx:D96Parser.ExprContext):
        pass

    # Exit a parse tree produced by D96Parser#expr.
    def exitExpr(self, ctx:D96Parser.ExprContext):
        pass


    # Enter a parse tree produced by D96Parser#exprList.
    def enterExprList(self, ctx:D96Parser.ExprListContext):
        pass

    # Exit a parse tree produced by D96Parser#exprList.
    def exitExprList(self, ctx:D96Parser.ExprListContext):
        pass


    # Enter a parse tree produced by D96Parser#arrDec.
    def enterArrDec(self, ctx:D96Parser.ArrDecContext):
        pass

    # Exit a parse tree produced by D96Parser#arrDec.
    def exitArrDec(self, ctx:D96Parser.ArrDecContext):
        pass


    # Enter a parse tree produced by D96Parser#vartype.
    def enterVartype(self, ctx:D96Parser.VartypeContext):
        pass

    # Exit a parse tree produced by D96Parser#vartype.
    def exitVartype(self, ctx:D96Parser.VartypeContext):
        pass


    # Enter a parse tree produced by D96Parser#arrLit.
    def enterArrLit(self, ctx:D96Parser.ArrLitContext):
        pass

    # Exit a parse tree produced by D96Parser#arrLit.
    def exitArrLit(self, ctx:D96Parser.ArrLitContext):
        pass



del D96Parser