# Generated from exprs.g4 by ANTLR 4.13.0
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,7,34,2,0,7,0,2,1,7,1,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,3,1,16,8,1,1,1,4,1,19,8,1,11,1,12,1,20,1,1,1,1,3,1,25,8,1,1,
        1,1,1,5,1,29,8,1,10,1,12,1,32,9,1,1,1,0,1,2,2,0,2,0,0,37,0,4,1,0,
        0,0,2,24,1,0,0,0,4,5,3,2,1,0,5,1,1,0,0,0,6,7,6,1,-1,0,7,25,5,6,0,
        0,8,9,5,1,0,0,9,10,3,2,1,0,10,11,5,2,0,0,11,25,1,0,0,0,12,16,5,3,
        0,0,13,16,1,0,0,0,14,16,5,4,0,0,15,12,1,0,0,0,15,13,1,0,0,0,15,14,
        1,0,0,0,16,18,1,0,0,0,17,19,5,6,0,0,18,17,1,0,0,0,19,20,1,0,0,0,
        20,18,1,0,0,0,20,21,1,0,0,0,21,22,1,0,0,0,22,23,5,5,0,0,23,25,3,
        2,1,1,24,6,1,0,0,0,24,8,1,0,0,0,24,15,1,0,0,0,25,30,1,0,0,0,26,27,
        10,2,0,0,27,29,3,2,1,3,28,26,1,0,0,0,29,32,1,0,0,0,30,28,1,0,0,0,
        30,31,1,0,0,0,31,3,1,0,0,0,32,30,1,0,0,0,4,15,20,24,30
    ]

class exprsParser ( Parser ):

    grammarFileName = "exprs.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'\\u03BB'", "'\\'", "'.'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "LLETRA", "WS" ]

    RULE_root = 0
    RULE_terme = 1

    ruleNames =  [ "root", "terme" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    LLETRA=6
    WS=7

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class RootContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def terme(self):
            return self.getTypedRuleContext(exprsParser.TermeContext,0)


        def getRuleIndex(self):
            return exprsParser.RULE_root

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRoot" ):
                return visitor.visitRoot(self)
            else:
                return visitor.visitChildren(self)




    def root(self):

        localctx = exprsParser.RootContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_root)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 4
            self.terme(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return exprsParser.RULE_terme

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class ParentesisContext(TermeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a exprsParser.TermeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def terme(self):
            return self.getTypedRuleContext(exprsParser.TermeContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParentesis" ):
                return visitor.visitParentesis(self)
            else:
                return visitor.visitChildren(self)


    class LletraContext(TermeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a exprsParser.TermeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LLETRA(self):
            return self.getToken(exprsParser.LLETRA, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLletra" ):
                return visitor.visitLletra(self)
            else:
                return visitor.visitChildren(self)


    class AbstraccioContext(TermeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a exprsParser.TermeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def terme(self):
            return self.getTypedRuleContext(exprsParser.TermeContext,0)

        def LLETRA(self, i:int=None):
            if i is None:
                return self.getTokens(exprsParser.LLETRA)
            else:
                return self.getToken(exprsParser.LLETRA, i)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAbstraccio" ):
                return visitor.visitAbstraccio(self)
            else:
                return visitor.visitChildren(self)


    class AplicacioContext(TermeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a exprsParser.TermeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def terme(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(exprsParser.TermeContext)
            else:
                return self.getTypedRuleContext(exprsParser.TermeContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAplicacio" ):
                return visitor.visitAplicacio(self)
            else:
                return visitor.visitChildren(self)



    def terme(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = exprsParser.TermeContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_terme, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                localctx = exprsParser.LletraContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 7
                self.match(exprsParser.LLETRA)
                pass

            elif la_ == 2:
                localctx = exprsParser.ParentesisContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 8
                self.match(exprsParser.T__0)
                self.state = 9
                self.terme(0)
                self.state = 10
                self.match(exprsParser.T__1)
                pass

            elif la_ == 3:
                localctx = exprsParser.AbstraccioContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 15
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [3]:
                    self.state = 12
                    self.match(exprsParser.T__2)
                    pass
                elif token in [6]:
                    pass
                elif token in [4]:
                    self.state = 14
                    self.match(exprsParser.T__3)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 18 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 17
                    self.match(exprsParser.LLETRA)
                    self.state = 20 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==6):
                        break

                self.state = 22
                self.match(exprsParser.T__4)
                self.state = 23
                self.terme(1)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 30
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = exprsParser.AplicacioContext(self, exprsParser.TermeContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_terme)
                    self.state = 26
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 27
                    self.terme(3) 
                self.state = 32
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
        self._predicates[1] = self.terme_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def terme_sempred(self, localctx:TermeContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         




