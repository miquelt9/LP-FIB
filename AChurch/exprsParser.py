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
        4,1,10,48,2,0,7,0,2,1,7,1,2,2,7,2,1,0,1,0,3,0,9,8,0,1,1,1,1,1,1,
        1,1,1,1,1,1,3,1,17,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,
        2,3,2,30,8,2,1,2,4,2,33,8,2,11,2,12,2,34,1,2,1,2,3,2,39,8,2,1,2,
        1,2,5,2,43,8,2,10,2,12,2,46,9,2,1,2,0,1,4,3,0,2,4,0,0,54,0,8,1,0,
        0,0,2,16,1,0,0,0,4,38,1,0,0,0,6,9,3,4,2,0,7,9,3,2,1,0,8,6,1,0,0,
        0,8,7,1,0,0,0,9,1,1,0,0,0,10,11,5,8,0,0,11,12,5,9,0,0,12,17,3,4,
        2,0,13,14,5,7,0,0,14,15,5,9,0,0,15,17,3,4,2,0,16,10,1,0,0,0,16,13,
        1,0,0,0,17,3,1,0,0,0,18,19,6,2,-1,0,19,39,5,6,0,0,20,39,5,8,0,0,
        21,39,5,7,0,0,22,23,5,1,0,0,23,24,3,4,2,0,24,25,5,2,0,0,25,39,1,
        0,0,0,26,30,5,3,0,0,27,30,1,0,0,0,28,30,5,4,0,0,29,26,1,0,0,0,29,
        27,1,0,0,0,29,28,1,0,0,0,30,32,1,0,0,0,31,33,5,6,0,0,32,31,1,0,0,
        0,33,34,1,0,0,0,34,32,1,0,0,0,34,35,1,0,0,0,35,36,1,0,0,0,36,37,
        5,5,0,0,37,39,3,4,2,1,38,18,1,0,0,0,38,20,1,0,0,0,38,21,1,0,0,0,
        38,22,1,0,0,0,38,29,1,0,0,0,39,44,1,0,0,0,40,41,10,2,0,0,41,43,3,
        4,2,3,42,40,1,0,0,0,43,46,1,0,0,0,44,42,1,0,0,0,44,45,1,0,0,0,45,
        5,1,0,0,0,46,44,1,0,0,0,6,8,16,29,34,38,44
    ]

class exprsParser ( Parser ):

    grammarFileName = "exprs.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'\\u03BB'", "'\\'", "'.'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "LLETRA", "NOM_MACRO", "INFIX", 
                      "EQUALS", "WS" ]

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
    LLETRA=6
    NOM_MACRO=7
    INFIX=8
    EQUALS=9
    WS=10

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
        def EQUALS(self):
            return self.getToken(exprsParser.EQUALS, 0)
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
        def EQUALS(self):
            return self.getToken(exprsParser.EQUALS, 0)
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
            self.state = 16
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8]:
                localctx = exprsParser.AssignarInfixContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 10
                self.match(exprsParser.INFIX)
                self.state = 11
                self.match(exprsParser.EQUALS)
                self.state = 12
                self.terme(0)
                pass
            elif token in [7]:
                localctx = exprsParser.AssignarMacroContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 13
                self.match(exprsParser.NOM_MACRO)
                self.state = 14
                self.match(exprsParser.EQUALS)
                self.state = 15
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
            self.state = 38
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                localctx = exprsParser.LletraContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 19
                self.match(exprsParser.LLETRA)
                pass

            elif la_ == 2:
                localctx = exprsParser.InfixContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 20
                self.match(exprsParser.INFIX)
                pass

            elif la_ == 3:
                localctx = exprsParser.MacroContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 21
                self.match(exprsParser.NOM_MACRO)
                pass

            elif la_ == 4:
                localctx = exprsParser.ParentesisContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 22
                self.match(exprsParser.T__0)
                self.state = 23
                self.terme(0)
                self.state = 24
                self.match(exprsParser.T__1)
                pass

            elif la_ == 5:
                localctx = exprsParser.AbstraccioContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 29
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [3]:
                    self.state = 26
                    self.match(exprsParser.T__2)
                    pass
                elif token in [6]:
                    pass
                elif token in [4]:
                    self.state = 28
                    self.match(exprsParser.T__3)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 32 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 31
                    self.match(exprsParser.LLETRA)
                    self.state = 34 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==6):
                        break

                self.state = 36
                self.match(exprsParser.T__4)
                self.state = 37
                self.terme(1)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 44
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = exprsParser.AplicacioContext(self, exprsParser.TermeContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_terme)
                    self.state = 40
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 41
                    self.terme(3) 
                self.state = 46
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

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
         




