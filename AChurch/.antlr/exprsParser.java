// Generated from /home/miquel/Documents/Q6/LP/AChurch/exprs.g4 by ANTLR 4.9.2
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class exprsParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.9.2", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, LLETRA=8, NOM_MACRO=9, 
		INFIX=10, WS=11;
	public static final int
		RULE_root = 0, RULE_assignar = 1, RULE_terme = 2;
	private static String[] makeRuleNames() {
		return new String[] {
			"root", "assignar", "terme"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'\u2261'", "'='", "'('", "')'", "'\u03BB'", "'\\'", "'.'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, "LLETRA", "NOM_MACRO", 
			"INFIX", "WS"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "exprs.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public exprsParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	public static class RootContext extends ParserRuleContext {
		public TermeContext terme() {
			return getRuleContext(TermeContext.class,0);
		}
		public AssignarContext assignar() {
			return getRuleContext(AssignarContext.class,0);
		}
		public RootContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_root; }
	}

	public final RootContext root() throws RecognitionException {
		RootContext _localctx = new RootContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_root);
		try {
			setState(8);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,0,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(6);
				terme(0);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(7);
				assignar();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class AssignarContext extends ParserRuleContext {
		public AssignarContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assignar; }
	 
		public AssignarContext() { }
		public void copyFrom(AssignarContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class AssignarInfixContext extends AssignarContext {
		public TerminalNode INFIX() { return getToken(exprsParser.INFIX, 0); }
		public TermeContext terme() {
			return getRuleContext(TermeContext.class,0);
		}
		public AssignarInfixContext(AssignarContext ctx) { copyFrom(ctx); }
	}
	public static class AssignarMacroContext extends AssignarContext {
		public TerminalNode NOM_MACRO() { return getToken(exprsParser.NOM_MACRO, 0); }
		public TermeContext terme() {
			return getRuleContext(TermeContext.class,0);
		}
		public AssignarMacroContext(AssignarContext ctx) { copyFrom(ctx); }
	}

	public final AssignarContext assignar() throws RecognitionException {
		AssignarContext _localctx = new AssignarContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_assignar);
		try {
			setState(24);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case INFIX:
				_localctx = new AssignarInfixContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(10);
				match(INFIX);
				setState(14);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case T__0:
					{
					setState(11);
					match(T__0);
					}
					break;
				case T__2:
				case T__4:
				case T__5:
				case LLETRA:
				case NOM_MACRO:
					{
					}
					break;
				case T__1:
					{
					setState(13);
					match(T__1);
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(16);
				terme(0);
				}
				break;
			case NOM_MACRO:
				_localctx = new AssignarMacroContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(17);
				match(NOM_MACRO);
				setState(21);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case T__0:
					{
					setState(18);
					match(T__0);
					}
					break;
				case T__2:
				case T__4:
				case T__5:
				case LLETRA:
				case NOM_MACRO:
					{
					}
					break;
				case T__1:
					{
					setState(20);
					match(T__1);
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(23);
				terme(0);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class TermeContext extends ParserRuleContext {
		public TermeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_terme; }
	 
		public TermeContext() { }
		public void copyFrom(TermeContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class ParentesisContext extends TermeContext {
		public TermeContext terme() {
			return getRuleContext(TermeContext.class,0);
		}
		public ParentesisContext(TermeContext ctx) { copyFrom(ctx); }
	}
	public static class MacroContext extends TermeContext {
		public TerminalNode NOM_MACRO() { return getToken(exprsParser.NOM_MACRO, 0); }
		public MacroContext(TermeContext ctx) { copyFrom(ctx); }
	}
	public static class LletraContext extends TermeContext {
		public TerminalNode LLETRA() { return getToken(exprsParser.LLETRA, 0); }
		public LletraContext(TermeContext ctx) { copyFrom(ctx); }
	}
	public static class AbstraccioContext extends TermeContext {
		public TermeContext terme() {
			return getRuleContext(TermeContext.class,0);
		}
		public List<TerminalNode> LLETRA() { return getTokens(exprsParser.LLETRA); }
		public TerminalNode LLETRA(int i) {
			return getToken(exprsParser.LLETRA, i);
		}
		public AbstraccioContext(TermeContext ctx) { copyFrom(ctx); }
	}
	public static class InfixContext extends TermeContext {
		public List<TerminalNode> NOM_MACRO() { return getTokens(exprsParser.NOM_MACRO); }
		public TerminalNode NOM_MACRO(int i) {
			return getToken(exprsParser.NOM_MACRO, i);
		}
		public TerminalNode INFIX() { return getToken(exprsParser.INFIX, 0); }
		public InfixContext(TermeContext ctx) { copyFrom(ctx); }
	}
	public static class AplicacioContext extends TermeContext {
		public List<TermeContext> terme() {
			return getRuleContexts(TermeContext.class);
		}
		public TermeContext terme(int i) {
			return getRuleContext(TermeContext.class,i);
		}
		public AplicacioContext(TermeContext ctx) { copyFrom(ctx); }
	}

	public final TermeContext terme() throws RecognitionException {
		return terme(0);
	}

	private TermeContext terme(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		TermeContext _localctx = new TermeContext(_ctx, _parentState);
		TermeContext _prevctx = _localctx;
		int _startState = 4;
		enterRecursionRule(_localctx, 4, RULE_terme, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(48);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,6,_ctx) ) {
			case 1:
				{
				_localctx = new LletraContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;

				setState(27);
				match(LLETRA);
				}
				break;
			case 2:
				{
				_localctx = new InfixContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(28);
				match(NOM_MACRO);
				setState(29);
				match(INFIX);
				setState(30);
				match(NOM_MACRO);
				}
				break;
			case 3:
				{
				_localctx = new MacroContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(31);
				match(NOM_MACRO);
				}
				break;
			case 4:
				{
				_localctx = new ParentesisContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(32);
				match(T__2);
				setState(33);
				terme(0);
				setState(34);
				match(T__3);
				}
				break;
			case 5:
				{
				_localctx = new AbstraccioContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(39);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case T__4:
					{
					setState(36);
					match(T__4);
					}
					break;
				case LLETRA:
					{
					}
					break;
				case T__5:
					{
					setState(38);
					match(T__5);
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(42); 
				_errHandler.sync(this);
				_la = _input.LA(1);
				do {
					{
					{
					setState(41);
					match(LLETRA);
					}
					}
					setState(44); 
					_errHandler.sync(this);
					_la = _input.LA(1);
				} while ( _la==LLETRA );
				setState(46);
				match(T__6);
				setState(47);
				terme(1);
				}
				break;
			}
			_ctx.stop = _input.LT(-1);
			setState(54);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,7,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new AplicacioContext(new TermeContext(_parentctx, _parentState));
					pushNewRecursionContext(_localctx, _startState, RULE_terme);
					setState(50);
					if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
					setState(51);
					terme(3);
					}
					} 
				}
				setState(56);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,7,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 2:
			return terme_sempred((TermeContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean terme_sempred(TermeContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 2);
		}
		return true;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\r<\4\2\t\2\4\3\t"+
		"\3\4\4\t\4\3\2\3\2\5\2\13\n\2\3\3\3\3\3\3\3\3\5\3\21\n\3\3\3\3\3\3\3\3"+
		"\3\3\3\5\3\30\n\3\3\3\5\3\33\n\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3"+
		"\4\3\4\3\4\3\4\5\4*\n\4\3\4\6\4-\n\4\r\4\16\4.\3\4\3\4\5\4\63\n\4\3\4"+
		"\3\4\7\4\67\n\4\f\4\16\4:\13\4\3\4\2\3\6\5\2\4\6\2\2\2F\2\n\3\2\2\2\4"+
		"\32\3\2\2\2\6\62\3\2\2\2\b\13\5\6\4\2\t\13\5\4\3\2\n\b\3\2\2\2\n\t\3\2"+
		"\2\2\13\3\3\2\2\2\f\20\7\f\2\2\r\21\7\3\2\2\16\21\3\2\2\2\17\21\7\4\2"+
		"\2\20\r\3\2\2\2\20\16\3\2\2\2\20\17\3\2\2\2\21\22\3\2\2\2\22\33\5\6\4"+
		"\2\23\27\7\13\2\2\24\30\7\3\2\2\25\30\3\2\2\2\26\30\7\4\2\2\27\24\3\2"+
		"\2\2\27\25\3\2\2\2\27\26\3\2\2\2\30\31\3\2\2\2\31\33\5\6\4\2\32\f\3\2"+
		"\2\2\32\23\3\2\2\2\33\5\3\2\2\2\34\35\b\4\1\2\35\63\7\n\2\2\36\37\7\13"+
		"\2\2\37 \7\f\2\2 \63\7\13\2\2!\63\7\13\2\2\"#\7\5\2\2#$\5\6\4\2$%\7\6"+
		"\2\2%\63\3\2\2\2&*\7\7\2\2\'*\3\2\2\2(*\7\b\2\2)&\3\2\2\2)\'\3\2\2\2)"+
		"(\3\2\2\2*,\3\2\2\2+-\7\n\2\2,+\3\2\2\2-.\3\2\2\2.,\3\2\2\2./\3\2\2\2"+
		"/\60\3\2\2\2\60\61\7\t\2\2\61\63\5\6\4\3\62\34\3\2\2\2\62\36\3\2\2\2\62"+
		"!\3\2\2\2\62\"\3\2\2\2\62)\3\2\2\2\638\3\2\2\2\64\65\f\4\2\2\65\67\5\6"+
		"\4\5\66\64\3\2\2\2\67:\3\2\2\28\66\3\2\2\289\3\2\2\29\7\3\2\2\2:8\3\2"+
		"\2\2\n\n\20\27\32).\628";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}