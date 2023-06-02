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
        4,1,11,58,2,0,7,0,2,1,7,1,2,2,7,2,1,0,1,0,3,0,9,8,0,1,1,1,1,1,1,
        1,1,3,1,15,8,1,1,1,1,1,1,1,1,1,1,1,3,1,22,8,1,1,1,3,1,25,8,1,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,40,8,2,1,2,4,
        2,43,8,2,11,2,12,2,44,1,2,1,2,3,2,49,8,2,1,2,1,2,5,2,53,8,2,10,2,
        12,2,56,9,2,1,2,0,1,4,3,0,2,4,0,0,68,0,8,1,0,0,0,2,24,1,0,0,0,4,
        48,1,0,0,0,6,9,3,4,2,0,7,9,3,2,1,0,8,6,1,0,0,0,8,7,1,0,0,0,9,1,1,
        0,0,0,10,14,5,9,0,0,11,15,5,1,0,0,12,15,1,0,0,0,13,15,5,2,0,0,14,
        11,1,0,0,0,14,12,1,0,0,0,14,13,1,0,0,0,15,16,1,0,0,0,16,25,3,4,2,
        0,17,21,5,10,0,0,18,22,5,1,0,0,19,22,1,0,0,0,20,22,5,2,0,0,21,18,
        1,0,0,0,21,19,1,0,0,0,21,20,1,0,0,0,22,23,1,0,0,0,23,25,3,4,2,0,
        24,10,1,0,0,0,24,17,1,0,0,0,25,3,1,0,0,0,26,27,6,2,-1,0,27,49,5,
        8,0,0,28,29,5,9,0,0,29,30,5,10,0,0,30,49,5,9,0,0,31,49,5,9,0,0,32,
        33,5,3,0,0,33,34,3,4,2,0,34,35,5,4,0,0,35,49,1,0,0,0,36,40,5,5,0,
        0,37,40,1,0,0,0,38,40,5,6,0,0,39,36,1,0,0,0,39,37,1,0,0,0,39,38,
        1,0,0,0,40,42,1,0,0,0,41,43,5,8,0,0,42,41,1,0,0,0,43,44,1,0,0,0,
        44,42,1,0,0,0,44,45,1,0,0,0,45,46,1,0,0,0,46,47,5,7,0,0,47,49,3,
        4,2,1,48,26,1,0,0,0,48,28,1,0,0,0,48,31,1,0,0,0,48,32,1,0,0,0,48,
        39,1,0,0,0,49,54,1,0,0,0,50,51,10,2,0,0,51,53,3,4,2,3,52,50,1,0,
        0,0,53,56,1,0,0,0,54,52,1,0,0,0,54,55,1,0,0,0,55,5,1,0,0,0,56,54,
        1,0,0,0,8,8,14,21,24,39,44,48,54
    ]

class exprsParser ( Parser ):

    grammarFileName = "exprs.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'\\u2261'", "'='", "'('", "')'", "'\\u03BB'", 
                     "'\\'", "'.'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "LLETRA", "NOM_MACRO", "INFIX", "WS" ]

    RULE_root = 0
    RULE_assignar = 1
    RULE_terme = 2

    ruleNames =  [ "root", "assignar", "terme" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    LLETRA=8
    NOM_MACRO=9
    INFIX=10
    WS=11

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


        def assignar(self):
            return self.getTypedRuleContext(exprsParser.AssignarContext,0)


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
            self.state = 8
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 6
                self.terme(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 7
                self.assignar()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignarContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return exprsParser.RULE_assignar

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class AssignarInfixContext(AssignarContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a exprsParser.AssignarContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INFIX(self):
            return self.getToken(exprsParser.INFIX, 0)
        def terme(self):
            return self.getTypedRuleContext(exprsParser.TermeContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignarInfix" ):
                return visitor.visitAssignarInfix(self)
            else:
                return visitor.visitChildren(self)


    class AssignarMacroContext(AssignarContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a exprsParser.AssignarContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NOM_MACRO(self):
            return self.getToken(exprsParser.NOM_MACRO, 0)
        def terme(self):
            return self.getTypedRuleContext(exprsParser.TermeContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignarMacro" ):
                return visitor.visitAssignarMacro(self)
            else:
                return visitor.visitChildren(self)



    def assignar(self):

        localctx = exprsParser.AssignarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_assignar)
        try:
            self.state = 24
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [9]:
                localctx = exprsParser.AssignarMacroContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 10
                self.match(exprsParser.NOM_MACRO)
                self.state = 14
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [1]:
                    self.state = 11
                    self.match(exprsParser.T__0)
                    pass
                elif token in [3, 5, 6, 8, 9]:
                    pass
                elif token in [2]:
                    self.state = 13
                    self.match(exprsParser.T__1)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 16
                self.terme(0)
                pass
            elif token in [10]:
                localctx = exprsParser.AssignarInfixContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 17
                self.match(exprsParser.INFIX)
                self.state = 21
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [1]:
                    self.state = 18
                    self.match(exprsParser.T__0)
                    pass
                elif token in [3, 5, 6, 8, 9]:
                    pass
                elif token in [2]:
                    self.state = 20
                    self.match(exprsParser.T__1)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 23
                self.terme(0)
                pass
            else:
                raise NoViableAltException(self)

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


    class MacroContext(TermeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a exprsParser.TermeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NOM_MACRO(self):
            return self.getToken(exprsParser.NOM_MACRO, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMacro" ):
                return visitor.visitMacro(self)
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


    class InfixContext(TermeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a exprsParser.TermeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NOM_MACRO(self, i:int=None):
            if i is None:
                return self.getTokens(exprsParser.NOM_MACRO)
            else:
                return self.getToken(exprsParser.NOM_MACRO, i)
        def INFIX(self):
            return self.getToken(exprsParser.INFIX, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInfix" ):
                return visitor.visitInfix(self)
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
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_terme, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                localctx = exprsParser.LletraContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 27
                self.match(exprsParser.LLETRA)
                pass

            elif la_ == 2:
                localctx = exprsParser.InfixContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 28
                self.match(exprsParser.NOM_MACRO)
                self.state = 29
                self.match(exprsParser.INFIX)
                self.state = 30
                self.match(exprsParser.NOM_MACRO)
                pass

            elif la_ == 3:
                localctx = exprsParser.MacroContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 31
                self.match(exprsParser.NOM_MACRO)
                pass

            elif la_ == 4:
                localctx = exprsParser.ParentesisContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 32
                self.match(exprsParser.T__2)
                self.state = 33
                self.terme(0)
                self.state = 34
                self.match(exprsParser.T__3)
                pass

            elif la_ == 5:
                localctx = exprsParser.AbstraccioContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 39
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [5]:
                    self.state = 36
                    self.match(exprsParser.T__4)
                    pass
                elif token in [8]:
                    pass
                elif token in [6]:
                    self.state = 38
                    self.match(exprsParser.T__5)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 42 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 41
                    self.match(exprsParser.LLETRA)
                    self.state = 44 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==8):
                        break

                self.state = 46
                self.match(exprsParser.T__6)
                self.state = 47
                self.terme(1)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 54
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = exprsParser.AplicacioContext(self, exprsParser.TermeContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_terme)
                    self.state = 50
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 51
                    self.terme(3) 
                self.state = 56
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

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
        self._predicates[2] = self.terme_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def terme_sempred(self, localctx:TermeContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         




