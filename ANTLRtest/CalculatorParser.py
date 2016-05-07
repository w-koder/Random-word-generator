# Generated from E:/Andre/Универ/Информатика/Checker/Random-word-generator/ANTLRtest\Calculator.g4 by ANTLR 4.5.1
# encoding: utf-8
from antlr4 import *
from io import StringIO

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3\f")
        buf.write("!\4\2\t\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2")
        buf.write("\3\2\5\2\21\n\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\7")
        buf.write("\2\34\n\2\f\2\16\2\37\13\2\3\2\2\3\2\3\2\2\4\3\2\7\b\3")
        buf.write("\2\t\n%\2\20\3\2\2\2\4\5\b\2\1\2\5\6\7\n\2\2\6\21\5\2")
        buf.write("\2\b\7\b\7\4\2\2\b\t\5\2\2\2\t\n\7\5\2\2\n\21\3\2\2\2")
        buf.write("\13\f\7\6\2\2\f\r\5\2\2\2\r\16\7\6\2\2\16\21\3\2\2\2\17")
        buf.write("\21\7\13\2\2\20\4\3\2\2\2\20\7\3\2\2\2\20\13\3\2\2\2\20")
        buf.write("\17\3\2\2\2\21\35\3\2\2\2\22\23\f\t\2\2\23\24\7\3\2\2")
        buf.write("\24\34\5\2\2\n\25\26\f\7\2\2\26\27\t\2\2\2\27\34\5\2\2")
        buf.write("\b\30\31\f\6\2\2\31\32\t\3\2\2\32\34\5\2\2\7\33\22\3\2")
        buf.write("\2\2\33\25\3\2\2\2\33\30\3\2\2\2\34\37\3\2\2\2\35\33\3")
        buf.write("\2\2\2\35\36\3\2\2\2\36\3\3\2\2\2\37\35\3\2\2\2\5\20\33")
        buf.write("\35")
        return buf.getvalue()


class CalculatorParser ( Parser ):

    grammarFileName = "Calculator.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'^'", "'('", "')'", "'|'", "'*'", "'/'", 
                     "'+'", "'-'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "MUL", "DIV", "ADD", "SUB", "INT", "WS" ]

    RULE_expr = 0

    ruleNames =  [ "expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    MUL=5
    DIV=6
    ADD=7
    SUB=8
    INT=9
    WS=10

    def __init__(self, input:TokenStream):
        super().__init__(input)
        self.checkVersion("4.5.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CalculatorParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class IntegerContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalculatorParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(CalculatorParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInteger" ):
                listener.enterInteger(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInteger" ):
                listener.exitInteger(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInteger" ):
                return visitor.visitInteger(self)
            else:
                return visitor.visitChildren(self)


    class AbsContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalculatorParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(CalculatorParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAbs" ):
                listener.enterAbs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAbs" ):
                listener.exitAbs(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAbs" ):
                return visitor.visitAbs(self)
            else:
                return visitor.visitChildren(self)


    class BracketsContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalculatorParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(CalculatorParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBrackets" ):
                listener.enterBrackets(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBrackets" ):
                listener.exitBrackets(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBrackets" ):
                return visitor.visitBrackets(self)
            else:
                return visitor.visitChildren(self)


    class MulDivContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalculatorParser.ExprContext
            super().__init__(parser)
            self.operator = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CalculatorParser.ExprContext)
            else:
                return self.getTypedRuleContext(CalculatorParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulDiv" ):
                listener.enterMulDiv(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulDiv" ):
                listener.exitMulDiv(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulDiv" ):
                return visitor.visitMulDiv(self)
            else:
                return visitor.visitChildren(self)


    class AddSubContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalculatorParser.ExprContext
            super().__init__(parser)
            self.operator = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CalculatorParser.ExprContext)
            else:
                return self.getTypedRuleContext(CalculatorParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddSub" ):
                listener.enterAddSub(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddSub" ):
                listener.exitAddSub(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddSub" ):
                return visitor.visitAddSub(self)
            else:
                return visitor.visitChildren(self)


    class ExpContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalculatorParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CalculatorParser.ExprContext)
            else:
                return self.getTypedRuleContext(CalculatorParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExp" ):
                listener.enterExp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExp" ):
                listener.exitExp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp" ):
                return visitor.visitExp(self)
            else:
                return visitor.visitChildren(self)


    class MinusContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalculatorParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(CalculatorParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMinus" ):
                listener.enterMinus(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMinus" ):
                listener.exitMinus(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMinus" ):
                return visitor.visitMinus(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CalculatorParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 0
        self.enterRecursionRule(localctx, 0, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 14
            token = self._input.LA(1)
            if token in [CalculatorParser.SUB]:
                localctx = CalculatorParser.MinusContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 3
                self.match(CalculatorParser.SUB)
                self.state = 4
                self.expr(6)

            elif token in [CalculatorParser.T__1]:
                localctx = CalculatorParser.BracketsContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 5
                self.match(CalculatorParser.T__1)
                self.state = 6
                self.expr(0)
                self.state = 7
                self.match(CalculatorParser.T__2)

            elif token in [CalculatorParser.T__3]:
                localctx = CalculatorParser.AbsContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 9
                self.match(CalculatorParser.T__3)
                self.state = 10
                self.expr(0)
                self.state = 11
                self.match(CalculatorParser.T__3)

            elif token in [CalculatorParser.INT]:
                localctx = CalculatorParser.IntegerContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 13
                self.match(CalculatorParser.INT)

            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 27
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 25
                    la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                    if la_ == 1:
                        localctx = CalculatorParser.ExpContext(self, CalculatorParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 16
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 17
                        self.match(CalculatorParser.T__0)
                        self.state = 18
                        self.expr(8)
                        pass

                    elif la_ == 2:
                        localctx = CalculatorParser.MulDivContext(self, CalculatorParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 19
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 20
                        localctx.operator = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==CalculatorParser.MUL or _la==CalculatorParser.DIV):
                            localctx.operator = self._errHandler.recoverInline(self)
                        else:
                            self.consume()
                        self.state = 21
                        self.expr(6)
                        pass

                    elif la_ == 3:
                        localctx = CalculatorParser.AddSubContext(self, CalculatorParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 22
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 23
                        localctx.operator = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==CalculatorParser.ADD or _la==CalculatorParser.SUB):
                            localctx.operator = self._errHandler.recoverInline(self)
                        else:
                            self.consume()
                        self.state = 24
                        self.expr(5)
                        pass

             
                self.state = 29
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

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
        self._predicates[0] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 4)
         




