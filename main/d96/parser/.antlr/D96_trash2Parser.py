# Generated from g:\sem_212\ppl\assignment1\src\main\d96\parser\D96_trash2.g4 by ANTLR 4.8
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\25")
        buf.write("\'\4\2\t\2\4\3\t\3\4\4\t\4\3\2\3\2\3\3\3\3\3\3\3\3\7\3")
        buf.write("\17\n\3\f\3\16\3\22\13\3\3\4\3\4\3\4\3\4\3\4\3\4\5\4\32")
        buf.write("\n\4\3\4\3\4\3\4\3\4\3\4\3\4\7\4\"\n\4\f\4\16\4%\13\4")
        buf.write("\3\4\2\3\6\5\2\4\6\2\6\3\2\3\4\3\2\21\22\3\2\17\20\3\2")
        buf.write("\r\16\2\'\2\b\3\2\2\2\4\n\3\2\2\2\6\31\3\2\2\2\b\t\7\2")
        buf.write("\2\3\t\3\3\2\2\2\n\13\t\2\2\2\13\20\7\23\2\2\f\r\7\13")
        buf.write("\2\2\r\17\7\23\2\2\16\f\3\2\2\2\17\22\3\2\2\2\20\16\3")
        buf.write("\2\2\2\20\21\3\2\2\2\21\5\3\2\2\2\22\20\3\2\2\2\23\24")
        buf.write("\b\4\1\2\24\25\7\6\2\2\25\26\5\6\4\2\26\27\7\7\2\2\27")
        buf.write("\32\3\2\2\2\30\32\t\3\2\2\31\23\3\2\2\2\31\30\3\2\2\2")
        buf.write("\32#\3\2\2\2\33\34\f\6\2\2\34\35\t\4\2\2\35\"\5\6\4\7")
        buf.write("\36\37\f\5\2\2\37 \t\5\2\2 \"\5\6\4\6!\33\3\2\2\2!\36")
        buf.write("\3\2\2\2\"%\3\2\2\2#!\3\2\2\2#$\3\2\2\2$\7\3\2\2\2%#\3")
        buf.write("\2\2\2\6\20\31!#")
        return buf.getvalue()


class D96_trash2Parser ( Parser ):

    grammarFileName = "D96_trash2.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'Int'", "'Float'", "'Return'", "'('", 
                     "')'", "'{'", "'}'", "';'", "','", "'='", "'+'", "'-'", 
                     "'*'", "'/'" ]

    symbolicNames = [ "<INVALID>", "INT", "FLOAT", "RETURN", "LP", "RP", 
                      "LB", "RB", "SM", "CM", "EQ", "ADD", "SUB", "MUL", 
                      "DIV", "INTLIT", "FLOATLIT", "ID", "WS", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_declare = 1
    RULE_expr = 2

    ruleNames =  [ "program", "declare", "expr" ]

    EOF = Token.EOF
    INT=1
    FLOAT=2
    RETURN=3
    LP=4
    RP=5
    LB=6
    RB=7
    SM=8
    CM=9
    EQ=10
    ADD=11
    SUB=12
    MUL=13
    DIV=14
    INTLIT=15
    FLOATLIT=16
    ID=17
    WS=18
    ERROR_CHAR=19

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(D96_trash2Parser.EOF, 0)

        def getRuleIndex(self):
            return D96_trash2Parser.RULE_program




    def program(self):

        localctx = D96_trash2Parser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 6
            self.match(D96_trash2Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclareContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(D96_trash2Parser.ID)
            else:
                return self.getToken(D96_trash2Parser.ID, i)

        def INT(self):
            return self.getToken(D96_trash2Parser.INT, 0)

        def FLOAT(self):
            return self.getToken(D96_trash2Parser.FLOAT, 0)

        def CM(self, i:int=None):
            if i is None:
                return self.getTokens(D96_trash2Parser.CM)
            else:
                return self.getToken(D96_trash2Parser.CM, i)

        def getRuleIndex(self):
            return D96_trash2Parser.RULE_declare




    def declare(self):

        localctx = D96_trash2Parser.DeclareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_declare)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 8
            _la = self._input.LA(1)
            if not(_la==D96_trash2Parser.INT or _la==D96_trash2Parser.FLOAT):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 9
            self.match(D96_trash2Parser.ID)
            self.state = 14
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96_trash2Parser.CM:
                self.state = 10
                self.match(D96_trash2Parser.CM)
                self.state = 11
                self.match(D96_trash2Parser.ID)
                self.state = 16
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(D96_trash2Parser.LP, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96_trash2Parser.ExprContext)
            else:
                return self.getTypedRuleContext(D96_trash2Parser.ExprContext,i)


        def RP(self):
            return self.getToken(D96_trash2Parser.RP, 0)

        def INTLIT(self):
            return self.getToken(D96_trash2Parser.INTLIT, 0)

        def FLOATLIT(self):
            return self.getToken(D96_trash2Parser.FLOATLIT, 0)

        def MUL(self):
            return self.getToken(D96_trash2Parser.MUL, 0)

        def DIV(self):
            return self.getToken(D96_trash2Parser.DIV, 0)

        def ADD(self):
            return self.getToken(D96_trash2Parser.ADD, 0)

        def SUB(self):
            return self.getToken(D96_trash2Parser.SUB, 0)

        def getRuleIndex(self):
            return D96_trash2Parser.RULE_expr



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96_trash2Parser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 23
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96_trash2Parser.LP]:
                self.state = 18
                self.match(D96_trash2Parser.LP)
                self.state = 19
                self.expr(0)
                self.state = 20
                self.match(D96_trash2Parser.RP)
                pass
            elif token in [D96_trash2Parser.INTLIT, D96_trash2Parser.FLOATLIT]:
                self.state = 22
                _la = self._input.LA(1)
                if not(_la==D96_trash2Parser.INTLIT or _la==D96_trash2Parser.FLOATLIT):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 33
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 31
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                    if la_ == 1:
                        localctx = D96_trash2Parser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 25
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 26
                        _la = self._input.LA(1)
                        if not(_la==D96_trash2Parser.MUL or _la==D96_trash2Parser.DIV):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 27
                        self.expr(5)
                        pass

                    elif la_ == 2:
                        localctx = D96_trash2Parser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 28
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 29
                        _la = self._input.LA(1)
                        if not(_la==D96_trash2Parser.ADD or _la==D96_trash2Parser.SUB):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 30
                        self.expr(4)
                        pass

             
                self.state = 35
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[2] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 3)
         




