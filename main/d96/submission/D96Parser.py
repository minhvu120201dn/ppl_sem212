# Generated from main/d96/parser/D96.g4 by ANTLR 4.9.3
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3B")
        buf.write("\u01d5\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\3\2\7\2R\n\2\f\2\16\2U\13\2\3\2\3\2\3")
        buf.write("\3\3\3\3\3\3\3\5\3]\n\3\3\3\3\3\7\3a\n\3\f\3\16\3d\13")
        buf.write("\3\3\3\3\3\3\4\3\4\5\4j\n\4\3\5\3\5\3\5\5\5o\n\5\3\5\3")
        buf.write("\5\3\5\3\5\3\5\3\5\5\5w\n\5\3\6\3\6\3\6\3\6\3\6\3\6\3")
        buf.write("\6\3\6\3\6\3\6\3\6\3\6\5\6\u0085\n\6\3\7\3\7\3\7\7\7\u008a")
        buf.write("\n\7\f\7\16\7\u008d\13\7\3\7\3\7\3\7\3\b\3\b\3\b\5\b\u0095")
        buf.write("\n\b\3\t\3\t\3\t\5\t\u009a\n\t\3\t\3\t\3\t\3\n\3\n\3\n")
        buf.write("\5\n\u00a2\n\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3")
        buf.write("\f\3\f\3\f\7\f\u00af\n\f\f\f\16\f\u00b2\13\f\3\r\3\r\3")
        buf.write("\r\7\r\u00b7\n\r\f\r\16\r\u00ba\13\r\3\r\3\r\3\r\3\16")
        buf.write("\3\16\7\16\u00c1\n\16\f\16\16\16\u00c4\13\16\3\16\3\16")
        buf.write("\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\5\17\u00d0\n")
        buf.write("\17\3\20\3\20\3\20\5\20\u00d5\n\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\5\20\u00dd\n\20\3\21\3\21\3\21\3\21\3\21\3")
        buf.write("\21\3\21\3\21\3\21\3\21\3\21\3\21\5\21\u00eb\n\21\3\22")
        buf.write("\3\22\3\22\7\22\u00f0\n\22\f\22\16\22\u00f3\13\22\3\22")
        buf.write("\3\22\3\22\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\25\5\25\u0105\n\25\3\25\3\25\3\25\3")
        buf.write("\25\3\25\6\25\u010c\n\25\r\25\16\25\u010d\3\25\3\25\3")
        buf.write("\25\7\25\u0113\n\25\f\25\16\25\u0116\13\25\3\26\3\26\3")
        buf.write("\26\3\26\3\26\3\26\3\26\5\26\u011f\n\26\3\27\3\27\3\27")
        buf.write("\3\27\3\27\3\27\3\27\5\27\u0128\n\27\3\30\3\30\3\30\3")
        buf.write("\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\5\31\u0136")
        buf.write("\n\31\3\31\3\31\3\31\3\32\3\32\7\32\u013d\n\32\f\32\16")
        buf.write("\32\u0140\13\32\3\32\3\32\3\33\3\33\3\33\3\33\5\33\u0148")
        buf.write("\n\33\3\34\3\34\3\34\3\34\3\34\3\34\3\34\5\34\u0151\n")
        buf.write("\34\3\35\3\35\3\35\3\35\3\35\3\35\3\35\5\35\u015a\n\35")
        buf.write("\3\36\3\36\3\36\3\37\3\37\3\37\3 \3 \3 \3!\3!\3!\3!\3")
        buf.write("!\3!\3\"\3\"\3\"\3\"\3\"\3\"\3#\3#\5#\u0173\n#\3#\3#\3")
        buf.write("$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3")
        buf.write("$\3$\5$\u018b\n$\3$\3$\3$\3$\5$\u0191\n$\3$\3$\3$\3$\3")
        buf.write("$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\5$\u01a6\n")
        buf.write("$\3$\3$\3$\3$\3$\6$\u01ad\n$\r$\16$\u01ae\7$\u01b1\n$")
        buf.write("\f$\16$\u01b4\13$\3%\3%\3%\3%\7%\u01ba\n%\f%\16%\u01bd")
        buf.write("\13%\5%\u01bf\n%\3%\3%\3&\3&\3&\3&\3&\3&\3&\3\'\3\'\3")
        buf.write("\'\3\'\3\'\3\'\5\'\u01d0\n\'\3(\3(\3(\3(\2\4(F)\2\4\6")
        buf.write("\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\66")
        buf.write("8:<>@BDFHJLN\2\b\3\2<=\3\2,.\3\2*+\3\2\60\61\4\2\62\62")
        buf.write("\648\3\29:\2\u01f7\2S\3\2\2\2\4X\3\2\2\2\6i\3\2\2\2\b")
        buf.write("v\3\2\2\2\n\u0084\3\2\2\2\f\u0086\3\2\2\2\16\u0094\3\2")
        buf.write("\2\2\20\u0096\3\2\2\2\22\u009e\3\2\2\2\24\u00a6\3\2\2")
        buf.write("\2\26\u00ab\3\2\2\2\30\u00b3\3\2\2\2\32\u00be\3\2\2\2")
        buf.write("\34\u00cf\3\2\2\2\36\u00dc\3\2\2\2 \u00ea\3\2\2\2\"\u00ec")
        buf.write("\3\2\2\2$\u00f7\3\2\2\2&\u00f9\3\2\2\2(\u0104\3\2\2\2")
        buf.write("*\u0117\3\2\2\2,\u0120\3\2\2\2.\u0129\3\2\2\2\60\u012c")
        buf.write("\3\2\2\2\62\u013a\3\2\2\2\64\u0147\3\2\2\2\66\u0149\3")
        buf.write("\2\2\28\u0152\3\2\2\2:\u015b\3\2\2\2<\u015e\3\2\2\2>\u0161")
        buf.write("\3\2\2\2@\u0164\3\2\2\2B\u016a\3\2\2\2D\u0170\3\2\2\2")
        buf.write("F\u0190\3\2\2\2H\u01b5\3\2\2\2J\u01c2\3\2\2\2L\u01cf\3")
        buf.write("\2\2\2N\u01d1\3\2\2\2PR\5\4\3\2QP\3\2\2\2RU\3\2\2\2SQ")
        buf.write("\3\2\2\2ST\3\2\2\2TV\3\2\2\2US\3\2\2\2VW\7\2\2\3W\3\3")
        buf.write("\2\2\2XY\7\27\2\2Y\\\7<\2\2Z[\7 \2\2[]\7<\2\2\\Z\3\2\2")
        buf.write("\2\\]\3\2\2\2]^\3\2\2\2^b\7(\2\2_a\5\6\4\2`_\3\2\2\2a")
        buf.write("d\3\2\2\2b`\3\2\2\2bc\3\2\2\2ce\3\2\2\2db\3\2\2\2ef\7")
        buf.write(")\2\2f\5\3\2\2\2gj\5\b\5\2hj\5\16\b\2ig\3\2\2\2ih\3\2")
        buf.write("\2\2j\7\3\2\2\2kn\7\31\2\2lo\5\n\6\2mo\5\f\7\2nl\3\2\2")
        buf.write("\2nm\3\2\2\2op\3\2\2\2pq\7\37\2\2qw\3\2\2\2rs\7\30\2\2")
        buf.write("st\5\n\6\2tu\7\37\2\2uw\3\2\2\2vk\3\2\2\2vr\3\2\2\2w\t")
        buf.write("\3\2\2\2xy\5$\23\2yz\7 \2\2z{\5L\'\2{|\7\63\2\2|}\5F$")
        buf.write("\2}\u0085\3\2\2\2~\177\5$\23\2\177\u0080\7!\2\2\u0080")
        buf.write("\u0081\5\n\6\2\u0081\u0082\7!\2\2\u0082\u0083\5F$\2\u0083")
        buf.write("\u0085\3\2\2\2\u0084x\3\2\2\2\u0084~\3\2\2\2\u0085\13")
        buf.write("\3\2\2\2\u0086\u008b\5$\23\2\u0087\u0088\7!\2\2\u0088")
        buf.write("\u008a\5$\23\2\u0089\u0087\3\2\2\2\u008a\u008d\3\2\2\2")
        buf.write("\u008b\u0089\3\2\2\2\u008b\u008c\3\2\2\2\u008c\u008e\3")
        buf.write("\2\2\2\u008d\u008b\3\2\2\2\u008e\u008f\7 \2\2\u008f\u0090")
        buf.write("\5L\'\2\u0090\r\3\2\2\2\u0091\u0095\5\20\t\2\u0092\u0095")
        buf.write("\5\22\n\2\u0093\u0095\5\24\13\2\u0094\u0091\3\2\2\2\u0094")
        buf.write("\u0092\3\2\2\2\u0094\u0093\3\2\2\2\u0095\17\3\2\2\2\u0096")
        buf.write("\u0097\t\2\2\2\u0097\u0099\7$\2\2\u0098\u009a\5\26\f\2")
        buf.write("\u0099\u0098\3\2\2\2\u0099\u009a\3\2\2\2\u009a\u009b\3")
        buf.write("\2\2\2\u009b\u009c\7%\2\2\u009c\u009d\5\32\16\2\u009d")
        buf.write("\21\3\2\2\2\u009e\u009f\7\32\2\2\u009f\u00a1\7$\2\2\u00a0")
        buf.write("\u00a2\5\26\f\2\u00a1\u00a0\3\2\2\2\u00a1\u00a2\3\2\2")
        buf.write("\2\u00a2\u00a3\3\2\2\2\u00a3\u00a4\7%\2\2\u00a4\u00a5")
        buf.write("\5\32\16\2\u00a5\23\3\2\2\2\u00a6\u00a7\7\33\2\2\u00a7")
        buf.write("\u00a8\7$\2\2\u00a8\u00a9\7%\2\2\u00a9\u00aa\5\32\16\2")
        buf.write("\u00aa\25\3\2\2\2\u00ab\u00b0\5\30\r\2\u00ac\u00ad\7\37")
        buf.write("\2\2\u00ad\u00af\5\30\r\2\u00ae\u00ac\3\2\2\2\u00af\u00b2")
        buf.write("\3\2\2\2\u00b0\u00ae\3\2\2\2\u00b0\u00b1\3\2\2\2\u00b1")
        buf.write("\27\3\2\2\2\u00b2\u00b0\3\2\2\2\u00b3\u00b8\5$\23\2\u00b4")
        buf.write("\u00b5\7!\2\2\u00b5\u00b7\5$\23\2\u00b6\u00b4\3\2\2\2")
        buf.write("\u00b7\u00ba\3\2\2\2\u00b8\u00b6\3\2\2\2\u00b8\u00b9\3")
        buf.write("\2\2\2\u00b9\u00bb\3\2\2\2\u00ba\u00b8\3\2\2\2\u00bb\u00bc")
        buf.write("\7 \2\2\u00bc\u00bd\5L\'\2\u00bd\31\3\2\2\2\u00be\u00c2")
        buf.write("\7(\2\2\u00bf\u00c1\5\34\17\2\u00c0\u00bf\3\2\2\2\u00c1")
        buf.write("\u00c4\3\2\2\2\u00c2\u00c0\3\2\2\2\u00c2\u00c3\3\2\2\2")
        buf.write("\u00c3\u00c5\3\2\2\2\u00c4\u00c2\3\2\2\2\u00c5\u00c6\7")
        buf.write(")\2\2\u00c6\33\3\2\2\2\u00c7\u00d0\5\36\20\2\u00c8\u00d0")
        buf.write("\5&\24\2\u00c9\u00d0\5*\26\2\u00ca\u00d0\5\60\31\2\u00cb")
        buf.write("\u00d0\5D#\2\u00cc\u00d0\5@!\2\u00cd\u00d0\5B\"\2\u00ce")
        buf.write("\u00d0\5\32\16\2\u00cf\u00c7\3\2\2\2\u00cf\u00c8\3\2\2")
        buf.write("\2\u00cf\u00c9\3\2\2\2\u00cf\u00ca\3\2\2\2\u00cf\u00cb")
        buf.write("\3\2\2\2\u00cf\u00cc\3\2\2\2\u00cf\u00cd\3\2\2\2\u00cf")
        buf.write("\u00ce\3\2\2\2\u00d0\35\3\2\2\2\u00d1\u00d4\7\31\2\2\u00d2")
        buf.write("\u00d5\5 \21\2\u00d3\u00d5\5\"\22\2\u00d4\u00d2\3\2\2")
        buf.write("\2\u00d4\u00d3\3\2\2\2\u00d5\u00d6\3\2\2\2\u00d6\u00d7")
        buf.write("\7\37\2\2\u00d7\u00dd\3\2\2\2\u00d8\u00d9\7\30\2\2\u00d9")
        buf.write("\u00da\5 \21\2\u00da\u00db\7\37\2\2\u00db\u00dd\3\2\2")
        buf.write("\2\u00dc\u00d1\3\2\2\2\u00dc\u00d8\3\2\2\2\u00dd\37\3")
        buf.write("\2\2\2\u00de\u00df\7<\2\2\u00df\u00e0\7 \2\2\u00e0\u00e1")
        buf.write("\5L\'\2\u00e1\u00e2\7\63\2\2\u00e2\u00e3\5F$\2\u00e3\u00eb")
        buf.write("\3\2\2\2\u00e4\u00e5\7<\2\2\u00e5\u00e6\7!\2\2\u00e6\u00e7")
        buf.write("\5 \21\2\u00e7\u00e8\7!\2\2\u00e8\u00e9\5F$\2\u00e9\u00eb")
        buf.write("\3\2\2\2\u00ea\u00de\3\2\2\2\u00ea\u00e4\3\2\2\2\u00eb")
        buf.write("!\3\2\2\2\u00ec\u00f1\7<\2\2\u00ed\u00ee\7!\2\2\u00ee")
        buf.write("\u00f0\7<\2\2\u00ef\u00ed\3\2\2\2\u00f0\u00f3\3\2\2\2")
        buf.write("\u00f1\u00ef\3\2\2\2\u00f1\u00f2\3\2\2\2\u00f2\u00f4\3")
        buf.write("\2\2\2\u00f3\u00f1\3\2\2\2\u00f4\u00f5\7 \2\2\u00f5\u00f6")
        buf.write("\5L\'\2\u00f6#\3\2\2\2\u00f7\u00f8\t\2\2\2\u00f8%\3\2")
        buf.write("\2\2\u00f9\u00fa\5(\25\2\u00fa\u00fb\7\63\2\2\u00fb\u00fc")
        buf.write("\5F$\2\u00fc\u00fd\7\37\2\2\u00fd\'\3\2\2\2\u00fe\u00ff")
        buf.write("\b\25\1\2\u00ff\u0105\5$\23\2\u0100\u0105\7\36\2\2\u0101")
        buf.write("\u0102\7<\2\2\u0102\u0103\7;\2\2\u0103\u0105\7=\2\2\u0104")
        buf.write("\u00fe\3\2\2\2\u0104\u0100\3\2\2\2\u0104\u0101\3\2\2\2")
        buf.write("\u0105\u0114\3\2\2\2\u0106\u010b\f\5\2\2\u0107\u0108\7")
        buf.write("&\2\2\u0108\u0109\5F$\2\u0109\u010a\7\'\2\2\u010a\u010c")
        buf.write("\3\2\2\2\u010b\u0107\3\2\2\2\u010c\u010d\3\2\2\2\u010d")
        buf.write("\u010b\3\2\2\2\u010d\u010e\3\2\2\2\u010e\u0113\3\2\2\2")
        buf.write("\u010f\u0110\f\4\2\2\u0110\u0111\7\"\2\2\u0111\u0113\7")
        buf.write("<\2\2\u0112\u0106\3\2\2\2\u0112\u010f\3\2\2\2\u0113\u0116")
        buf.write("\3\2\2\2\u0114\u0112\3\2\2\2\u0114\u0115\3\2\2\2\u0115")
        buf.write(")\3\2\2\2\u0116\u0114\3\2\2\2\u0117\u0118\7\t\2\2\u0118")
        buf.write("\u0119\7$\2\2\u0119\u011a\5F$\2\u011a\u011b\7%\2\2\u011b")
        buf.write("\u011e\5\32\16\2\u011c\u011f\5,\27\2\u011d\u011f\5.\30")
        buf.write("\2\u011e\u011c\3\2\2\2\u011e\u011d\3\2\2\2\u011e\u011f")
        buf.write("\3\2\2\2\u011f+\3\2\2\2\u0120\u0121\7\n\2\2\u0121\u0122")
        buf.write("\7$\2\2\u0122\u0123\5F$\2\u0123\u0124\7%\2\2\u0124\u0127")
        buf.write("\5\32\16\2\u0125\u0128\5,\27\2\u0126\u0128\5.\30\2\u0127")
        buf.write("\u0125\3\2\2\2\u0127\u0126\3\2\2\2\u0127\u0128\3\2\2\2")
        buf.write("\u0128-\3\2\2\2\u0129\u012a\7\13\2\2\u012a\u012b\5\32")
        buf.write("\16\2\u012b/\3\2\2\2\u012c\u012d\7\f\2\2\u012d\u012e\7")
        buf.write("$\2\2\u012e\u012f\7<\2\2\u012f\u0130\7\20\2\2\u0130\u0131")
        buf.write("\5F$\2\u0131\u0132\7#\2\2\u0132\u0135\5F$\2\u0133\u0134")
        buf.write("\7\35\2\2\u0134\u0136\5F$\2\u0135\u0133\3\2\2\2\u0135")
        buf.write("\u0136\3\2\2\2\u0136\u0137\3\2\2\2\u0137\u0138\7%\2\2")
        buf.write("\u0138\u0139\5\62\32\2\u0139\61\3\2\2\2\u013a\u013e\7")
        buf.write("(\2\2\u013b\u013d\5\64\33\2\u013c\u013b\3\2\2\2\u013d")
        buf.write("\u0140\3\2\2\2\u013e\u013c\3\2\2\2\u013e\u013f\3\2\2\2")
        buf.write("\u013f\u0141\3\2\2\2\u0140\u013e\3\2\2\2\u0141\u0142\7")
        buf.write(")\2\2\u0142\63\3\2\2\2\u0143\u0148\5\34\17\2\u0144\u0148")
        buf.write("\5\66\34\2\u0145\u0148\5<\37\2\u0146\u0148\5> \2\u0147")
        buf.write("\u0143\3\2\2\2\u0147\u0144\3\2\2\2\u0147\u0145\3\2\2\2")
        buf.write("\u0147\u0146\3\2\2\2\u0148\65\3\2\2\2\u0149\u014a\7\t")
        buf.write("\2\2\u014a\u014b\7$\2\2\u014b\u014c\5F$\2\u014c\u014d")
        buf.write("\7%\2\2\u014d\u0150\5\32\16\2\u014e\u0151\58\35\2\u014f")
        buf.write("\u0151\5:\36\2\u0150\u014e\3\2\2\2\u0150\u014f\3\2\2\2")
        buf.write("\u0150\u0151\3\2\2\2\u0151\67\3\2\2\2\u0152\u0153\7\n")
        buf.write("\2\2\u0153\u0154\7$\2\2\u0154\u0155\5F$\2\u0155\u0156")
        buf.write("\7%\2\2\u0156\u0159\5\32\16\2\u0157\u015a\58\35\2\u0158")
        buf.write("\u015a\5:\36\2\u0159\u0157\3\2\2\2\u0159\u0158\3\2\2\2")
        buf.write("\u0159\u015a\3\2\2\2\u015a9\3\2\2\2\u015b\u015c\7\13\2")
        buf.write("\2\u015c\u015d\5\62\32\2\u015d;\3\2\2\2\u015e\u015f\7")
        buf.write("\7\2\2\u015f\u0160\7\37\2\2\u0160=\3\2\2\2\u0161\u0162")
        buf.write("\7\b\2\2\u0162\u0163\7\37\2\2\u0163?\3\2\2\2\u0164\u0165")
        buf.write("\5F$\2\u0165\u0166\7\"\2\2\u0166\u0167\7<\2\2\u0167\u0168")
        buf.write("\5H%\2\u0168\u0169\7\37\2\2\u0169A\3\2\2\2\u016a\u016b")
        buf.write("\7<\2\2\u016b\u016c\7;\2\2\u016c\u016d\7=\2\2\u016d\u016e")
        buf.write("\5H%\2\u016e\u016f\7\37\2\2\u016fC\3\2\2\2\u0170\u0172")
        buf.write("\7\25\2\2\u0171\u0173\5F$\2\u0172\u0171\3\2\2\2\u0172")
        buf.write("\u0173\3\2\2\2\u0173\u0174\3\2\2\2\u0174\u0175\7\37\2")
        buf.write("\2\u0175E\3\2\2\2\u0176\u0177\b$\1\2\u0177\u0191\7\3\2")
        buf.write("\2\u0178\u0191\7\4\2\2\u0179\u0191\7\5\2\2\u017a\u0191")
        buf.write("\7\6\2\2\u017b\u0191\7\26\2\2\u017c\u0191\7\36\2\2\u017d")
        buf.write("\u0191\5N(\2\u017e\u0191\5$\23\2\u017f\u0180\7$\2\2\u0180")
        buf.write("\u0181\5F$\2\u0181\u0182\7%\2\2\u0182\u0191\3\2\2\2\u0183")
        buf.write("\u0184\7\34\2\2\u0184\u0185\7<\2\2\u0185\u0191\5H%\2\u0186")
        buf.write("\u0187\7<\2\2\u0187\u0188\7;\2\2\u0188\u018a\7=\2\2\u0189")
        buf.write("\u018b\5H%\2\u018a\u0189\3\2\2\2\u018a\u018b\3\2\2\2\u018b")
        buf.write("\u0191\3\2\2\2\u018c\u018d\7+\2\2\u018d\u0191\5F$\t\u018e")
        buf.write("\u018f\7/\2\2\u018f\u0191\5F$\b\u0190\u0176\3\2\2\2\u0190")
        buf.write("\u0178\3\2\2\2\u0190\u0179\3\2\2\2\u0190\u017a\3\2\2\2")
        buf.write("\u0190\u017b\3\2\2\2\u0190\u017c\3\2\2\2\u0190\u017d\3")
        buf.write("\2\2\2\u0190\u017e\3\2\2\2\u0190\u017f\3\2\2\2\u0190\u0183")
        buf.write("\3\2\2\2\u0190\u0186\3\2\2\2\u0190\u018c\3\2\2\2\u0190")
        buf.write("\u018e\3\2\2\2\u0191\u01b2\3\2\2\2\u0192\u0193\f\7\2\2")
        buf.write("\u0193\u0194\t\3\2\2\u0194\u01b1\5F$\b\u0195\u0196\f\6")
        buf.write("\2\2\u0196\u0197\t\4\2\2\u0197\u01b1\5F$\7\u0198\u0199")
        buf.write("\f\5\2\2\u0199\u019a\t\5\2\2\u019a\u01b1\5F$\6\u019b\u019c")
        buf.write("\f\4\2\2\u019c\u019d\t\6\2\2\u019d\u01b1\5F$\5\u019e\u019f")
        buf.write("\f\3\2\2\u019f\u01a0\t\7\2\2\u01a0\u01b1\5F$\4\u01a1\u01a2")
        buf.write("\f\13\2\2\u01a2\u01a3\7\"\2\2\u01a3\u01a5\7<\2\2\u01a4")
        buf.write("\u01a6\5H%\2\u01a5\u01a4\3\2\2\2\u01a5\u01a6\3\2\2\2\u01a6")
        buf.write("\u01b1\3\2\2\2\u01a7\u01ac\f\n\2\2\u01a8\u01a9\7&\2\2")
        buf.write("\u01a9\u01aa\5F$\2\u01aa\u01ab\7\'\2\2\u01ab\u01ad\3\2")
        buf.write("\2\2\u01ac\u01a8\3\2\2\2\u01ad\u01ae\3\2\2\2\u01ae\u01ac")
        buf.write("\3\2\2\2\u01ae\u01af\3\2\2\2\u01af\u01b1\3\2\2\2\u01b0")
        buf.write("\u0192\3\2\2\2\u01b0\u0195\3\2\2\2\u01b0\u0198\3\2\2\2")
        buf.write("\u01b0\u019b\3\2\2\2\u01b0\u019e\3\2\2\2\u01b0\u01a1\3")
        buf.write("\2\2\2\u01b0\u01a7\3\2\2\2\u01b1\u01b4\3\2\2\2\u01b2\u01b0")
        buf.write("\3\2\2\2\u01b2\u01b3\3\2\2\2\u01b3G\3\2\2\2\u01b4\u01b2")
        buf.write("\3\2\2\2\u01b5\u01be\7$\2\2\u01b6\u01bb\5F$\2\u01b7\u01b8")
        buf.write("\7!\2\2\u01b8\u01ba\5F$\2\u01b9\u01b7\3\2\2\2\u01ba\u01bd")
        buf.write("\3\2\2\2\u01bb\u01b9\3\2\2\2\u01bb\u01bc\3\2\2\2\u01bc")
        buf.write("\u01bf\3\2\2\2\u01bd\u01bb\3\2\2\2\u01be\u01b6\3\2\2\2")
        buf.write("\u01be\u01bf\3\2\2\2\u01bf\u01c0\3\2\2\2\u01c0\u01c1\7")
        buf.write("%\2\2\u01c1I\3\2\2\2\u01c2\u01c3\7\17\2\2\u01c3\u01c4")
        buf.write("\7&\2\2\u01c4\u01c5\5L\'\2\u01c5\u01c6\7!\2\2\u01c6\u01c7")
        buf.write("\7\3\2\2\u01c7\u01c8\7\'\2\2\u01c8K\3\2\2\2\u01c9\u01d0")
        buf.write("\7\21\2\2\u01ca\u01d0\7\22\2\2\u01cb\u01d0\7\23\2\2\u01cc")
        buf.write("\u01d0\7\24\2\2\u01cd\u01d0\5J&\2\u01ce\u01d0\7<\2\2\u01cf")
        buf.write("\u01c9\3\2\2\2\u01cf\u01ca\3\2\2\2\u01cf\u01cb\3\2\2\2")
        buf.write("\u01cf\u01cc\3\2\2\2\u01cf\u01cd\3\2\2\2\u01cf\u01ce\3")
        buf.write("\2\2\2\u01d0M\3\2\2\2\u01d1\u01d2\7\17\2\2\u01d2\u01d3")
        buf.write("\5H%\2\u01d3O\3\2\2\2*S\\binv\u0084\u008b\u0094\u0099")
        buf.write("\u00a1\u00b0\u00b8\u00c2\u00cf\u00d4\u00dc\u00ea\u00f1")
        buf.write("\u0104\u010d\u0112\u0114\u011e\u0127\u0135\u013e\u0147")
        buf.write("\u0150\u0159\u0172\u018a\u0190\u01a5\u01ae\u01b0\u01b2")
        buf.write("\u01bb\u01be\u01cf")
        return buf.getvalue()


class D96Parser ( Parser ):

    grammarFileName = "D96.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'Break'", "'Continue'", "'If'", "'Elseif'", 
                     "'Else'", "'Foreach'", "'True'", "'False'", "'Array'", 
                     "'In'", "'Int'", "'Float'", "'Boolean'", "'String'", 
                     "'Return'", "'Null'", "'Class'", "'Val'", "'Var'", 
                     "'Constructor'", "'Destructor'", "'New'", "'By'", "'Self'", 
                     "';'", "':'", "','", "'.'", "'..'", "'('", "')'", "'['", 
                     "']'", "'{'", "'}'", "'+'", "'-'", "'*'", "'/'", "'%'", 
                     "'!'", "'&&'", "'||'", "'=='", "'='", "'!='", "'<'", 
                     "'<='", "'>'", "'>='", "'==.'", "'+.'", "'::'" ]

    symbolicNames = [ "<INVALID>", "INTLIT", "FLOATLIT", "BOOLLIT", "STRLIT", 
                      "BREAK_", "CONTINUE_", "IF_", "ELSEIF_", "ELSE_", 
                      "FOREACH_", "TRUE_", "FALSE_", "ARRAY_", "IN_", "INT_", 
                      "FLOAT_", "BOOL_", "STR_", "RETURN_", "NULL_", "CLASS_", 
                      "VAL_", "VAR_", "CONSTRUCTOR_", "DESTRUCTOR_", "NEW_", 
                      "BY_", "SELF_", "SEMI", "COLON", "COMMA", "DOT", "DOUBLEDOT", 
                      "LB", "RB", "LSB", "RSB", "LCB", "RCB", "ADDOP", "SUBOP", 
                      "MULOP", "DIVOP", "MODOP", "NOTOP", "ANDOP", "OROP", 
                      "EQCMP", "ASNOP", "DIFCMP", "LESCMP", "LEQCMP", "GRECMP", 
                      "GEQCMP", "SEQCMP", "SADDOP", "CSMEM", "ID", "VID", 
                      "COMMENT", "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_classDecl = 1
    RULE_classMem = 2
    RULE_attribute = 3
    RULE_attrBody = 4
    RULE_attrNonInit = 5
    RULE_method = 6
    RULE_normalMet = 7
    RULE_constructor = 8
    RULE_destructor = 9
    RULE_paraList = 10
    RULE_idList = 11
    RULE_scope = 12
    RULE_stmt = 13
    RULE_declStmt = 14
    RULE_declBody = 15
    RULE_declNonInit = 16
    RULE_identifier = 17
    RULE_asnStmt = 18
    RULE_lhs = 19
    RULE_ifStmt = 20
    RULE_elifStmt = 21
    RULE_elseStmt = 22
    RULE_forStmt = 23
    RULE_scopeLoop = 24
    RULE_stmtLoop = 25
    RULE_ifStmtLoop = 26
    RULE_elifStmtLoop = 27
    RULE_elseStmtLoop = 28
    RULE_breakStmt = 29
    RULE_contStmt = 30
    RULE_insMetStmt = 31
    RULE_staMetStmt = 32
    RULE_retStmt = 33
    RULE_expr = 34
    RULE_exprList = 35
    RULE_arrDec = 36
    RULE_vartype = 37
    RULE_arrLit = 38

    ruleNames =  [ "program", "classDecl", "classMem", "attribute", "attrBody", 
                   "attrNonInit", "method", "normalMet", "constructor", 
                   "destructor", "paraList", "idList", "scope", "stmt", 
                   "declStmt", "declBody", "declNonInit", "identifier", 
                   "asnStmt", "lhs", "ifStmt", "elifStmt", "elseStmt", "forStmt", 
                   "scopeLoop", "stmtLoop", "ifStmtLoop", "elifStmtLoop", 
                   "elseStmtLoop", "breakStmt", "contStmt", "insMetStmt", 
                   "staMetStmt", "retStmt", "expr", "exprList", "arrDec", 
                   "vartype", "arrLit" ]

    EOF = Token.EOF
    INTLIT=1
    FLOATLIT=2
    BOOLLIT=3
    STRLIT=4
    BREAK_=5
    CONTINUE_=6
    IF_=7
    ELSEIF_=8
    ELSE_=9
    FOREACH_=10
    TRUE_=11
    FALSE_=12
    ARRAY_=13
    IN_=14
    INT_=15
    FLOAT_=16
    BOOL_=17
    STR_=18
    RETURN_=19
    NULL_=20
    CLASS_=21
    VAL_=22
    VAR_=23
    CONSTRUCTOR_=24
    DESTRUCTOR_=25
    NEW_=26
    BY_=27
    SELF_=28
    SEMI=29
    COLON=30
    COMMA=31
    DOT=32
    DOUBLEDOT=33
    LB=34
    RB=35
    LSB=36
    RSB=37
    LCB=38
    RCB=39
    ADDOP=40
    SUBOP=41
    MULOP=42
    DIVOP=43
    MODOP=44
    NOTOP=45
    ANDOP=46
    OROP=47
    EQCMP=48
    ASNOP=49
    DIFCMP=50
    LESCMP=51
    LEQCMP=52
    GRECMP=53
    GEQCMP=54
    SEQCMP=55
    SADDOP=56
    CSMEM=57
    ID=58
    VID=59
    COMMENT=60
    WS=61
    ERROR_CHAR=62
    UNCLOSE_STRING=63
    ILLEGAL_ESCAPE=64

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(D96Parser.EOF, 0)

        def classDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.ClassDeclContext)
            else:
                return self.getTypedRuleContext(D96Parser.ClassDeclContext,i)


        def getRuleIndex(self):
            return D96Parser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = D96Parser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.CLASS_:
                self.state = 78
                self.classDecl()
                self.state = 83
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 84
            self.match(D96Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CLASS_(self):
            return self.getToken(D96Parser.CLASS_, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.ID)
            else:
                return self.getToken(D96Parser.ID, i)

        def LCB(self):
            return self.getToken(D96Parser.LCB, 0)

        def RCB(self):
            return self.getToken(D96Parser.RCB, 0)

        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def classMem(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.ClassMemContext)
            else:
                return self.getTypedRuleContext(D96Parser.ClassMemContext,i)


        def getRuleIndex(self):
            return D96Parser.RULE_classDecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassDecl" ):
                return visitor.visitClassDecl(self)
            else:
                return visitor.visitChildren(self)




    def classDecl(self):

        localctx = D96Parser.ClassDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_classDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            self.match(D96Parser.CLASS_)
            self.state = 87
            self.match(D96Parser.ID)
            self.state = 90
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.COLON:
                self.state = 88
                self.match(D96Parser.COLON)
                self.state = 89
                self.match(D96Parser.ID)


            self.state = 92
            self.match(D96Parser.LCB)
            self.state = 96
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.VAL_) | (1 << D96Parser.VAR_) | (1 << D96Parser.CONSTRUCTOR_) | (1 << D96Parser.DESTRUCTOR_) | (1 << D96Parser.ID) | (1 << D96Parser.VID))) != 0):
                self.state = 93
                self.classMem()
                self.state = 98
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 99
            self.match(D96Parser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassMemContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attribute(self):
            return self.getTypedRuleContext(D96Parser.AttributeContext,0)


        def method(self):
            return self.getTypedRuleContext(D96Parser.MethodContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_classMem

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassMem" ):
                return visitor.visitClassMem(self)
            else:
                return visitor.visitChildren(self)




    def classMem(self):

        localctx = D96Parser.ClassMemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_classMem)
        try:
            self.state = 103
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.VAL_, D96Parser.VAR_]:
                self.enterOuterAlt(localctx, 1)
                self.state = 101
                self.attribute()
                pass
            elif token in [D96Parser.CONSTRUCTOR_, D96Parser.DESTRUCTOR_, D96Parser.ID, D96Parser.VID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 102
                self.method()
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


    class AttributeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR_(self):
            return self.getToken(D96Parser.VAR_, 0)

        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def attrBody(self):
            return self.getTypedRuleContext(D96Parser.AttrBodyContext,0)


        def attrNonInit(self):
            return self.getTypedRuleContext(D96Parser.AttrNonInitContext,0)


        def VAL_(self):
            return self.getToken(D96Parser.VAL_, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_attribute

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttribute" ):
                return visitor.visitAttribute(self)
            else:
                return visitor.visitChildren(self)




    def attribute(self):

        localctx = D96Parser.AttributeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_attribute)
        try:
            self.state = 116
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.VAR_]:
                self.enterOuterAlt(localctx, 1)
                self.state = 105
                self.match(D96Parser.VAR_)
                self.state = 108
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                if la_ == 1:
                    self.state = 106
                    self.attrBody()
                    pass

                elif la_ == 2:
                    self.state = 107
                    self.attrNonInit()
                    pass


                self.state = 110
                self.match(D96Parser.SEMI)
                pass
            elif token in [D96Parser.VAL_]:
                self.enterOuterAlt(localctx, 2)
                self.state = 112
                self.match(D96Parser.VAL_)
                self.state = 113
                self.attrBody()
                self.state = 114
                self.match(D96Parser.SEMI)
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


    class AttrBodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(D96Parser.IdentifierContext,0)


        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def vartype(self):
            return self.getTypedRuleContext(D96Parser.VartypeContext,0)


        def ASNOP(self):
            return self.getToken(D96Parser.ASNOP, 0)

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def attrBody(self):
            return self.getTypedRuleContext(D96Parser.AttrBodyContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_attrBody

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttrBody" ):
                return visitor.visitAttrBody(self)
            else:
                return visitor.visitChildren(self)




    def attrBody(self):

        localctx = D96Parser.AttrBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_attrBody)
        try:
            self.state = 130
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 118
                self.identifier()
                self.state = 119
                self.match(D96Parser.COLON)
                self.state = 120
                self.vartype()
                self.state = 121
                self.match(D96Parser.ASNOP)
                self.state = 122
                self.expr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 124
                self.identifier()
                self.state = 125
                self.match(D96Parser.COMMA)
                self.state = 126
                self.attrBody()
                self.state = 127
                self.match(D96Parser.COMMA)
                self.state = 128
                self.expr(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttrNonInitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.IdentifierContext)
            else:
                return self.getTypedRuleContext(D96Parser.IdentifierContext,i)


        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def vartype(self):
            return self.getTypedRuleContext(D96Parser.VartypeContext,0)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def getRuleIndex(self):
            return D96Parser.RULE_attrNonInit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttrNonInit" ):
                return visitor.visitAttrNonInit(self)
            else:
                return visitor.visitChildren(self)




    def attrNonInit(self):

        localctx = D96Parser.AttrNonInitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_attrNonInit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 132
            self.identifier()
            self.state = 137
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COMMA:
                self.state = 133
                self.match(D96Parser.COMMA)
                self.state = 134
                self.identifier()
                self.state = 139
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 140
            self.match(D96Parser.COLON)
            self.state = 141
            self.vartype()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def normalMet(self):
            return self.getTypedRuleContext(D96Parser.NormalMetContext,0)


        def constructor(self):
            return self.getTypedRuleContext(D96Parser.ConstructorContext,0)


        def destructor(self):
            return self.getTypedRuleContext(D96Parser.DestructorContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_method

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod" ):
                return visitor.visitMethod(self)
            else:
                return visitor.visitChildren(self)




    def method(self):

        localctx = D96Parser.MethodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_method)
        try:
            self.state = 146
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ID, D96Parser.VID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 143
                self.normalMet()
                pass
            elif token in [D96Parser.CONSTRUCTOR_]:
                self.enterOuterAlt(localctx, 2)
                self.state = 144
                self.constructor()
                pass
            elif token in [D96Parser.DESTRUCTOR_]:
                self.enterOuterAlt(localctx, 3)
                self.state = 145
                self.destructor()
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


    class NormalMetContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def scope(self):
            return self.getTypedRuleContext(D96Parser.ScopeContext,0)


        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def VID(self):
            return self.getToken(D96Parser.VID, 0)

        def paraList(self):
            return self.getTypedRuleContext(D96Parser.ParaListContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_normalMet

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNormalMet" ):
                return visitor.visitNormalMet(self)
            else:
                return visitor.visitChildren(self)




    def normalMet(self):

        localctx = D96Parser.NormalMetContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_normalMet)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 148
            _la = self._input.LA(1)
            if not(_la==D96Parser.ID or _la==D96Parser.VID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 149
            self.match(D96Parser.LB)
            self.state = 151
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.ID or _la==D96Parser.VID:
                self.state = 150
                self.paraList()


            self.state = 153
            self.match(D96Parser.RB)
            self.state = 154
            self.scope()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstructorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONSTRUCTOR_(self):
            return self.getToken(D96Parser.CONSTRUCTOR_, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def scope(self):
            return self.getTypedRuleContext(D96Parser.ScopeContext,0)


        def paraList(self):
            return self.getTypedRuleContext(D96Parser.ParaListContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_constructor

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstructor" ):
                return visitor.visitConstructor(self)
            else:
                return visitor.visitChildren(self)




    def constructor(self):

        localctx = D96Parser.ConstructorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_constructor)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 156
            self.match(D96Parser.CONSTRUCTOR_)
            self.state = 157
            self.match(D96Parser.LB)
            self.state = 159
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.ID or _la==D96Parser.VID:
                self.state = 158
                self.paraList()


            self.state = 161
            self.match(D96Parser.RB)
            self.state = 162
            self.scope()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DestructorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DESTRUCTOR_(self):
            return self.getToken(D96Parser.DESTRUCTOR_, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def scope(self):
            return self.getTypedRuleContext(D96Parser.ScopeContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_destructor

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDestructor" ):
                return visitor.visitDestructor(self)
            else:
                return visitor.visitChildren(self)




    def destructor(self):

        localctx = D96Parser.DestructorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_destructor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 164
            self.match(D96Parser.DESTRUCTOR_)
            self.state = 165
            self.match(D96Parser.LB)
            self.state = 166
            self.match(D96Parser.RB)
            self.state = 167
            self.scope()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParaListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def idList(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.IdListContext)
            else:
                return self.getTypedRuleContext(D96Parser.IdListContext,i)


        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.SEMI)
            else:
                return self.getToken(D96Parser.SEMI, i)

        def getRuleIndex(self):
            return D96Parser.RULE_paraList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParaList" ):
                return visitor.visitParaList(self)
            else:
                return visitor.visitChildren(self)




    def paraList(self):

        localctx = D96Parser.ParaListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_paraList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 169
            self.idList()
            self.state = 174
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.SEMI:
                self.state = 170
                self.match(D96Parser.SEMI)
                self.state = 171
                self.idList()
                self.state = 176
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.IdentifierContext)
            else:
                return self.getTypedRuleContext(D96Parser.IdentifierContext,i)


        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def vartype(self):
            return self.getTypedRuleContext(D96Parser.VartypeContext,0)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def getRuleIndex(self):
            return D96Parser.RULE_idList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdList" ):
                return visitor.visitIdList(self)
            else:
                return visitor.visitChildren(self)




    def idList(self):

        localctx = D96Parser.IdListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_idList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 177
            self.identifier()
            self.state = 182
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COMMA:
                self.state = 178
                self.match(D96Parser.COMMA)
                self.state = 179
                self.identifier()
                self.state = 184
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 185
            self.match(D96Parser.COLON)
            self.state = 186
            self.vartype()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ScopeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LCB(self):
            return self.getToken(D96Parser.LCB, 0)

        def RCB(self):
            return self.getToken(D96Parser.RCB, 0)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.StmtContext)
            else:
                return self.getTypedRuleContext(D96Parser.StmtContext,i)


        def getRuleIndex(self):
            return D96Parser.RULE_scope

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitScope" ):
                return visitor.visitScope(self)
            else:
                return visitor.visitChildren(self)




    def scope(self):

        localctx = D96Parser.ScopeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_scope)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 188
            self.match(D96Parser.LCB)
            self.state = 192
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.INTLIT) | (1 << D96Parser.FLOATLIT) | (1 << D96Parser.BOOLLIT) | (1 << D96Parser.STRLIT) | (1 << D96Parser.IF_) | (1 << D96Parser.FOREACH_) | (1 << D96Parser.ARRAY_) | (1 << D96Parser.RETURN_) | (1 << D96Parser.NULL_) | (1 << D96Parser.VAL_) | (1 << D96Parser.VAR_) | (1 << D96Parser.NEW_) | (1 << D96Parser.SELF_) | (1 << D96Parser.LB) | (1 << D96Parser.LCB) | (1 << D96Parser.SUBOP) | (1 << D96Parser.NOTOP) | (1 << D96Parser.ID) | (1 << D96Parser.VID))) != 0):
                self.state = 189
                self.stmt()
                self.state = 194
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 195
            self.match(D96Parser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declStmt(self):
            return self.getTypedRuleContext(D96Parser.DeclStmtContext,0)


        def asnStmt(self):
            return self.getTypedRuleContext(D96Parser.AsnStmtContext,0)


        def ifStmt(self):
            return self.getTypedRuleContext(D96Parser.IfStmtContext,0)


        def forStmt(self):
            return self.getTypedRuleContext(D96Parser.ForStmtContext,0)


        def retStmt(self):
            return self.getTypedRuleContext(D96Parser.RetStmtContext,0)


        def insMetStmt(self):
            return self.getTypedRuleContext(D96Parser.InsMetStmtContext,0)


        def staMetStmt(self):
            return self.getTypedRuleContext(D96Parser.StaMetStmtContext,0)


        def scope(self):
            return self.getTypedRuleContext(D96Parser.ScopeContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = D96Parser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_stmt)
        try:
            self.state = 205
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 197
                self.declStmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 198
                self.asnStmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 199
                self.ifStmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 200
                self.forStmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 201
                self.retStmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 202
                self.insMetStmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 203
                self.staMetStmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 204
                self.scope()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR_(self):
            return self.getToken(D96Parser.VAR_, 0)

        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def declBody(self):
            return self.getTypedRuleContext(D96Parser.DeclBodyContext,0)


        def declNonInit(self):
            return self.getTypedRuleContext(D96Parser.DeclNonInitContext,0)


        def VAL_(self):
            return self.getToken(D96Parser.VAL_, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_declStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclStmt" ):
                return visitor.visitDeclStmt(self)
            else:
                return visitor.visitChildren(self)




    def declStmt(self):

        localctx = D96Parser.DeclStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_declStmt)
        try:
            self.state = 218
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.VAR_]:
                self.enterOuterAlt(localctx, 1)
                self.state = 207
                self.match(D96Parser.VAR_)
                self.state = 210
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
                if la_ == 1:
                    self.state = 208
                    self.declBody()
                    pass

                elif la_ == 2:
                    self.state = 209
                    self.declNonInit()
                    pass


                self.state = 212
                self.match(D96Parser.SEMI)
                pass
            elif token in [D96Parser.VAL_]:
                self.enterOuterAlt(localctx, 2)
                self.state = 214
                self.match(D96Parser.VAL_)
                self.state = 215
                self.declBody()
                self.state = 216
                self.match(D96Parser.SEMI)
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


    class DeclBodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def vartype(self):
            return self.getTypedRuleContext(D96Parser.VartypeContext,0)


        def ASNOP(self):
            return self.getToken(D96Parser.ASNOP, 0)

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def declBody(self):
            return self.getTypedRuleContext(D96Parser.DeclBodyContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_declBody

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclBody" ):
                return visitor.visitDeclBody(self)
            else:
                return visitor.visitChildren(self)




    def declBody(self):

        localctx = D96Parser.DeclBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_declBody)
        try:
            self.state = 232
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 220
                self.match(D96Parser.ID)
                self.state = 221
                self.match(D96Parser.COLON)
                self.state = 222
                self.vartype()
                self.state = 223
                self.match(D96Parser.ASNOP)
                self.state = 224
                self.expr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 226
                self.match(D96Parser.ID)
                self.state = 227
                self.match(D96Parser.COMMA)
                self.state = 228
                self.declBody()
                self.state = 229
                self.match(D96Parser.COMMA)
                self.state = 230
                self.expr(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclNonInitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.ID)
            else:
                return self.getToken(D96Parser.ID, i)

        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def vartype(self):
            return self.getTypedRuleContext(D96Parser.VartypeContext,0)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def getRuleIndex(self):
            return D96Parser.RULE_declNonInit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclNonInit" ):
                return visitor.visitDeclNonInit(self)
            else:
                return visitor.visitChildren(self)




    def declNonInit(self):

        localctx = D96Parser.DeclNonInitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_declNonInit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 234
            self.match(D96Parser.ID)
            self.state = 239
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COMMA:
                self.state = 235
                self.match(D96Parser.COMMA)
                self.state = 236
                self.match(D96Parser.ID)
                self.state = 241
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 242
            self.match(D96Parser.COLON)
            self.state = 243
            self.vartype()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdentifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def VID(self):
            return self.getToken(D96Parser.VID, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_identifier

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdentifier" ):
                return visitor.visitIdentifier(self)
            else:
                return visitor.visitChildren(self)




    def identifier(self):

        localctx = D96Parser.IdentifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_identifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 245
            _la = self._input.LA(1)
            if not(_la==D96Parser.ID or _la==D96Parser.VID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AsnStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lhs(self):
            return self.getTypedRuleContext(D96Parser.LhsContext,0)


        def ASNOP(self):
            return self.getToken(D96Parser.ASNOP, 0)

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_asnStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAsnStmt" ):
                return visitor.visitAsnStmt(self)
            else:
                return visitor.visitChildren(self)




    def asnStmt(self):

        localctx = D96Parser.AsnStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_asnStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 247
            self.lhs(0)
            self.state = 248
            self.match(D96Parser.ASNOP)
            self.state = 249
            self.expr(0)
            self.state = 250
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(D96Parser.IdentifierContext,0)


        def SELF_(self):
            return self.getToken(D96Parser.SELF_, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def CSMEM(self):
            return self.getToken(D96Parser.CSMEM, 0)

        def VID(self):
            return self.getToken(D96Parser.VID, 0)

        def lhs(self):
            return self.getTypedRuleContext(D96Parser.LhsContext,0)


        def LSB(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.LSB)
            else:
                return self.getToken(D96Parser.LSB, i)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.ExprContext)
            else:
                return self.getTypedRuleContext(D96Parser.ExprContext,i)


        def RSB(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.RSB)
            else:
                return self.getToken(D96Parser.RSB, i)

        def DOT(self):
            return self.getToken(D96Parser.DOT, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_lhs

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLhs" ):
                return visitor.visitLhs(self)
            else:
                return visitor.visitChildren(self)



    def lhs(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.LhsContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 38
        self.enterRecursionRule(localctx, 38, self.RULE_lhs, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 258
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.state = 253
                self.identifier()
                pass

            elif la_ == 2:
                self.state = 254
                self.match(D96Parser.SELF_)
                pass

            elif la_ == 3:
                self.state = 255
                self.match(D96Parser.ID)
                self.state = 256
                self.match(D96Parser.CSMEM)
                self.state = 257
                self.match(D96Parser.VID)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 274
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 272
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
                    if la_ == 1:
                        localctx = D96Parser.LhsContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_lhs)
                        self.state = 260
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 265 
                        self._errHandler.sync(self)
                        _alt = 1
                        while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                            if _alt == 1:
                                self.state = 261
                                self.match(D96Parser.LSB)
                                self.state = 262
                                self.expr(0)
                                self.state = 263
                                self.match(D96Parser.RSB)

                            else:
                                raise NoViableAltException(self)
                            self.state = 267 
                            self._errHandler.sync(self)
                            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

                        pass

                    elif la_ == 2:
                        localctx = D96Parser.LhsContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_lhs)
                        self.state = 269
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 270
                        self.match(D96Parser.DOT)
                        self.state = 271
                        self.match(D96Parser.ID)
                        pass

             
                self.state = 276
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class IfStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF_(self):
            return self.getToken(D96Parser.IF_, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def scope(self):
            return self.getTypedRuleContext(D96Parser.ScopeContext,0)


        def elifStmt(self):
            return self.getTypedRuleContext(D96Parser.ElifStmtContext,0)


        def elseStmt(self):
            return self.getTypedRuleContext(D96Parser.ElseStmtContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_ifStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStmt" ):
                return visitor.visitIfStmt(self)
            else:
                return visitor.visitChildren(self)




    def ifStmt(self):

        localctx = D96Parser.IfStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_ifStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 277
            self.match(D96Parser.IF_)
            self.state = 278
            self.match(D96Parser.LB)
            self.state = 279
            self.expr(0)
            self.state = 280
            self.match(D96Parser.RB)
            self.state = 281
            self.scope()
            self.state = 284
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ELSEIF_]:
                self.state = 282
                self.elifStmt()
                pass
            elif token in [D96Parser.ELSE_]:
                self.state = 283
                self.elseStmt()
                pass
            elif token in [D96Parser.INTLIT, D96Parser.FLOATLIT, D96Parser.BOOLLIT, D96Parser.STRLIT, D96Parser.BREAK_, D96Parser.CONTINUE_, D96Parser.IF_, D96Parser.FOREACH_, D96Parser.ARRAY_, D96Parser.RETURN_, D96Parser.NULL_, D96Parser.VAL_, D96Parser.VAR_, D96Parser.NEW_, D96Parser.SELF_, D96Parser.LB, D96Parser.LCB, D96Parser.RCB, D96Parser.SUBOP, D96Parser.NOTOP, D96Parser.ID, D96Parser.VID]:
                pass
            else:
                pass
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElifStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSEIF_(self):
            return self.getToken(D96Parser.ELSEIF_, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def scope(self):
            return self.getTypedRuleContext(D96Parser.ScopeContext,0)


        def elifStmt(self):
            return self.getTypedRuleContext(D96Parser.ElifStmtContext,0)


        def elseStmt(self):
            return self.getTypedRuleContext(D96Parser.ElseStmtContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_elifStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElifStmt" ):
                return visitor.visitElifStmt(self)
            else:
                return visitor.visitChildren(self)




    def elifStmt(self):

        localctx = D96Parser.ElifStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_elifStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 286
            self.match(D96Parser.ELSEIF_)
            self.state = 287
            self.match(D96Parser.LB)
            self.state = 288
            self.expr(0)
            self.state = 289
            self.match(D96Parser.RB)
            self.state = 290
            self.scope()
            self.state = 293
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ELSEIF_]:
                self.state = 291
                self.elifStmt()
                pass
            elif token in [D96Parser.ELSE_]:
                self.state = 292
                self.elseStmt()
                pass
            elif token in [D96Parser.INTLIT, D96Parser.FLOATLIT, D96Parser.BOOLLIT, D96Parser.STRLIT, D96Parser.BREAK_, D96Parser.CONTINUE_, D96Parser.IF_, D96Parser.FOREACH_, D96Parser.ARRAY_, D96Parser.RETURN_, D96Parser.NULL_, D96Parser.VAL_, D96Parser.VAR_, D96Parser.NEW_, D96Parser.SELF_, D96Parser.LB, D96Parser.LCB, D96Parser.RCB, D96Parser.SUBOP, D96Parser.NOTOP, D96Parser.ID, D96Parser.VID]:
                pass
            else:
                pass
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElseStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE_(self):
            return self.getToken(D96Parser.ELSE_, 0)

        def scope(self):
            return self.getTypedRuleContext(D96Parser.ScopeContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_elseStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElseStmt" ):
                return visitor.visitElseStmt(self)
            else:
                return visitor.visitChildren(self)




    def elseStmt(self):

        localctx = D96Parser.ElseStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_elseStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 295
            self.match(D96Parser.ELSE_)
            self.state = 296
            self.scope()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOREACH_(self):
            return self.getToken(D96Parser.FOREACH_, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def IN_(self):
            return self.getToken(D96Parser.IN_, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.ExprContext)
            else:
                return self.getTypedRuleContext(D96Parser.ExprContext,i)


        def DOUBLEDOT(self):
            return self.getToken(D96Parser.DOUBLEDOT, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def scopeLoop(self):
            return self.getTypedRuleContext(D96Parser.ScopeLoopContext,0)


        def BY_(self):
            return self.getToken(D96Parser.BY_, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_forStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForStmt" ):
                return visitor.visitForStmt(self)
            else:
                return visitor.visitChildren(self)




    def forStmt(self):

        localctx = D96Parser.ForStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_forStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 298
            self.match(D96Parser.FOREACH_)
            self.state = 299
            self.match(D96Parser.LB)
            self.state = 300
            self.match(D96Parser.ID)
            self.state = 301
            self.match(D96Parser.IN_)
            self.state = 302
            self.expr(0)
            self.state = 303
            self.match(D96Parser.DOUBLEDOT)
            self.state = 304
            self.expr(0)
            self.state = 307
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.BY_:
                self.state = 305
                self.match(D96Parser.BY_)
                self.state = 306
                self.expr(0)


            self.state = 309
            self.match(D96Parser.RB)
            self.state = 310
            self.scopeLoop()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ScopeLoopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LCB(self):
            return self.getToken(D96Parser.LCB, 0)

        def RCB(self):
            return self.getToken(D96Parser.RCB, 0)

        def stmtLoop(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.StmtLoopContext)
            else:
                return self.getTypedRuleContext(D96Parser.StmtLoopContext,i)


        def getRuleIndex(self):
            return D96Parser.RULE_scopeLoop

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitScopeLoop" ):
                return visitor.visitScopeLoop(self)
            else:
                return visitor.visitChildren(self)




    def scopeLoop(self):

        localctx = D96Parser.ScopeLoopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_scopeLoop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 312
            self.match(D96Parser.LCB)
            self.state = 316
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.INTLIT) | (1 << D96Parser.FLOATLIT) | (1 << D96Parser.BOOLLIT) | (1 << D96Parser.STRLIT) | (1 << D96Parser.BREAK_) | (1 << D96Parser.CONTINUE_) | (1 << D96Parser.IF_) | (1 << D96Parser.FOREACH_) | (1 << D96Parser.ARRAY_) | (1 << D96Parser.RETURN_) | (1 << D96Parser.NULL_) | (1 << D96Parser.VAL_) | (1 << D96Parser.VAR_) | (1 << D96Parser.NEW_) | (1 << D96Parser.SELF_) | (1 << D96Parser.LB) | (1 << D96Parser.LCB) | (1 << D96Parser.SUBOP) | (1 << D96Parser.NOTOP) | (1 << D96Parser.ID) | (1 << D96Parser.VID))) != 0):
                self.state = 313
                self.stmtLoop()
                self.state = 318
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 319
            self.match(D96Parser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtLoopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self):
            return self.getTypedRuleContext(D96Parser.StmtContext,0)


        def ifStmtLoop(self):
            return self.getTypedRuleContext(D96Parser.IfStmtLoopContext,0)


        def breakStmt(self):
            return self.getTypedRuleContext(D96Parser.BreakStmtContext,0)


        def contStmt(self):
            return self.getTypedRuleContext(D96Parser.ContStmtContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_stmtLoop

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmtLoop" ):
                return visitor.visitStmtLoop(self)
            else:
                return visitor.visitChildren(self)




    def stmtLoop(self):

        localctx = D96Parser.StmtLoopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_stmtLoop)
        try:
            self.state = 325
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 321
                self.stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 322
                self.ifStmtLoop()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 323
                self.breakStmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 324
                self.contStmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStmtLoopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF_(self):
            return self.getToken(D96Parser.IF_, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def scope(self):
            return self.getTypedRuleContext(D96Parser.ScopeContext,0)


        def elifStmtLoop(self):
            return self.getTypedRuleContext(D96Parser.ElifStmtLoopContext,0)


        def elseStmtLoop(self):
            return self.getTypedRuleContext(D96Parser.ElseStmtLoopContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_ifStmtLoop

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStmtLoop" ):
                return visitor.visitIfStmtLoop(self)
            else:
                return visitor.visitChildren(self)




    def ifStmtLoop(self):

        localctx = D96Parser.IfStmtLoopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_ifStmtLoop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 327
            self.match(D96Parser.IF_)
            self.state = 328
            self.match(D96Parser.LB)
            self.state = 329
            self.expr(0)
            self.state = 330
            self.match(D96Parser.RB)
            self.state = 331
            self.scope()
            self.state = 334
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ELSEIF_]:
                self.state = 332
                self.elifStmtLoop()
                pass
            elif token in [D96Parser.ELSE_]:
                self.state = 333
                self.elseStmtLoop()
                pass
            elif token in [D96Parser.INTLIT, D96Parser.FLOATLIT, D96Parser.BOOLLIT, D96Parser.STRLIT, D96Parser.BREAK_, D96Parser.CONTINUE_, D96Parser.IF_, D96Parser.FOREACH_, D96Parser.ARRAY_, D96Parser.RETURN_, D96Parser.NULL_, D96Parser.VAL_, D96Parser.VAR_, D96Parser.NEW_, D96Parser.SELF_, D96Parser.LB, D96Parser.LCB, D96Parser.RCB, D96Parser.SUBOP, D96Parser.NOTOP, D96Parser.ID, D96Parser.VID]:
                pass
            else:
                pass
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElifStmtLoopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSEIF_(self):
            return self.getToken(D96Parser.ELSEIF_, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def scope(self):
            return self.getTypedRuleContext(D96Parser.ScopeContext,0)


        def elifStmtLoop(self):
            return self.getTypedRuleContext(D96Parser.ElifStmtLoopContext,0)


        def elseStmtLoop(self):
            return self.getTypedRuleContext(D96Parser.ElseStmtLoopContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_elifStmtLoop

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElifStmtLoop" ):
                return visitor.visitElifStmtLoop(self)
            else:
                return visitor.visitChildren(self)




    def elifStmtLoop(self):

        localctx = D96Parser.ElifStmtLoopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_elifStmtLoop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 336
            self.match(D96Parser.ELSEIF_)
            self.state = 337
            self.match(D96Parser.LB)
            self.state = 338
            self.expr(0)
            self.state = 339
            self.match(D96Parser.RB)
            self.state = 340
            self.scope()
            self.state = 343
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ELSEIF_]:
                self.state = 341
                self.elifStmtLoop()
                pass
            elif token in [D96Parser.ELSE_]:
                self.state = 342
                self.elseStmtLoop()
                pass
            elif token in [D96Parser.INTLIT, D96Parser.FLOATLIT, D96Parser.BOOLLIT, D96Parser.STRLIT, D96Parser.BREAK_, D96Parser.CONTINUE_, D96Parser.IF_, D96Parser.FOREACH_, D96Parser.ARRAY_, D96Parser.RETURN_, D96Parser.NULL_, D96Parser.VAL_, D96Parser.VAR_, D96Parser.NEW_, D96Parser.SELF_, D96Parser.LB, D96Parser.LCB, D96Parser.RCB, D96Parser.SUBOP, D96Parser.NOTOP, D96Parser.ID, D96Parser.VID]:
                pass
            else:
                pass
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElseStmtLoopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE_(self):
            return self.getToken(D96Parser.ELSE_, 0)

        def scopeLoop(self):
            return self.getTypedRuleContext(D96Parser.ScopeLoopContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_elseStmtLoop

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElseStmtLoop" ):
                return visitor.visitElseStmtLoop(self)
            else:
                return visitor.visitChildren(self)




    def elseStmtLoop(self):

        localctx = D96Parser.ElseStmtLoopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_elseStmtLoop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 345
            self.match(D96Parser.ELSE_)
            self.state = 346
            self.scopeLoop()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BreakStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK_(self):
            return self.getToken(D96Parser.BREAK_, 0)

        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_breakStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreakStmt" ):
                return visitor.visitBreakStmt(self)
            else:
                return visitor.visitChildren(self)




    def breakStmt(self):

        localctx = D96Parser.BreakStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_breakStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 348
            self.match(D96Parser.BREAK_)
            self.state = 349
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE_(self):
            return self.getToken(D96Parser.CONTINUE_, 0)

        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_contStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContStmt" ):
                return visitor.visitContStmt(self)
            else:
                return visitor.visitChildren(self)




    def contStmt(self):

        localctx = D96Parser.ContStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_contStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 351
            self.match(D96Parser.CONTINUE_)
            self.state = 352
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InsMetStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def DOT(self):
            return self.getToken(D96Parser.DOT, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def exprList(self):
            return self.getTypedRuleContext(D96Parser.ExprListContext,0)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_insMetStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInsMetStmt" ):
                return visitor.visitInsMetStmt(self)
            else:
                return visitor.visitChildren(self)




    def insMetStmt(self):

        localctx = D96Parser.InsMetStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_insMetStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 354
            self.expr(0)
            self.state = 355
            self.match(D96Parser.DOT)
            self.state = 356
            self.match(D96Parser.ID)
            self.state = 357
            self.exprList()
            self.state = 358
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StaMetStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def CSMEM(self):
            return self.getToken(D96Parser.CSMEM, 0)

        def VID(self):
            return self.getToken(D96Parser.VID, 0)

        def exprList(self):
            return self.getTypedRuleContext(D96Parser.ExprListContext,0)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_staMetStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStaMetStmt" ):
                return visitor.visitStaMetStmt(self)
            else:
                return visitor.visitChildren(self)




    def staMetStmt(self):

        localctx = D96Parser.StaMetStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_staMetStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 360
            self.match(D96Parser.ID)
            self.state = 361
            self.match(D96Parser.CSMEM)
            self.state = 362
            self.match(D96Parser.VID)
            self.state = 363
            self.exprList()
            self.state = 364
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RetStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN_(self):
            return self.getToken(D96Parser.RETURN_, 0)

        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_retStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRetStmt" ):
                return visitor.visitRetStmt(self)
            else:
                return visitor.visitChildren(self)




    def retStmt(self):

        localctx = D96Parser.RetStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_retStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 366
            self.match(D96Parser.RETURN_)
            self.state = 368
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.INTLIT) | (1 << D96Parser.FLOATLIT) | (1 << D96Parser.BOOLLIT) | (1 << D96Parser.STRLIT) | (1 << D96Parser.ARRAY_) | (1 << D96Parser.NULL_) | (1 << D96Parser.NEW_) | (1 << D96Parser.SELF_) | (1 << D96Parser.LB) | (1 << D96Parser.SUBOP) | (1 << D96Parser.NOTOP) | (1 << D96Parser.ID) | (1 << D96Parser.VID))) != 0):
                self.state = 367
                self.expr(0)


            self.state = 370
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTLIT(self):
            return self.getToken(D96Parser.INTLIT, 0)

        def FLOATLIT(self):
            return self.getToken(D96Parser.FLOATLIT, 0)

        def BOOLLIT(self):
            return self.getToken(D96Parser.BOOLLIT, 0)

        def STRLIT(self):
            return self.getToken(D96Parser.STRLIT, 0)

        def NULL_(self):
            return self.getToken(D96Parser.NULL_, 0)

        def SELF_(self):
            return self.getToken(D96Parser.SELF_, 0)

        def arrLit(self):
            return self.getTypedRuleContext(D96Parser.ArrLitContext,0)


        def identifier(self):
            return self.getTypedRuleContext(D96Parser.IdentifierContext,0)


        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.ExprContext)
            else:
                return self.getTypedRuleContext(D96Parser.ExprContext,i)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def NEW_(self):
            return self.getToken(D96Parser.NEW_, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def exprList(self):
            return self.getTypedRuleContext(D96Parser.ExprListContext,0)


        def CSMEM(self):
            return self.getToken(D96Parser.CSMEM, 0)

        def VID(self):
            return self.getToken(D96Parser.VID, 0)

        def SUBOP(self):
            return self.getToken(D96Parser.SUBOP, 0)

        def NOTOP(self):
            return self.getToken(D96Parser.NOTOP, 0)

        def MULOP(self):
            return self.getToken(D96Parser.MULOP, 0)

        def DIVOP(self):
            return self.getToken(D96Parser.DIVOP, 0)

        def MODOP(self):
            return self.getToken(D96Parser.MODOP, 0)

        def ADDOP(self):
            return self.getToken(D96Parser.ADDOP, 0)

        def ANDOP(self):
            return self.getToken(D96Parser.ANDOP, 0)

        def OROP(self):
            return self.getToken(D96Parser.OROP, 0)

        def EQCMP(self):
            return self.getToken(D96Parser.EQCMP, 0)

        def DIFCMP(self):
            return self.getToken(D96Parser.DIFCMP, 0)

        def LESCMP(self):
            return self.getToken(D96Parser.LESCMP, 0)

        def GRECMP(self):
            return self.getToken(D96Parser.GRECMP, 0)

        def LEQCMP(self):
            return self.getToken(D96Parser.LEQCMP, 0)

        def GEQCMP(self):
            return self.getToken(D96Parser.GEQCMP, 0)

        def SADDOP(self):
            return self.getToken(D96Parser.SADDOP, 0)

        def SEQCMP(self):
            return self.getToken(D96Parser.SEQCMP, 0)

        def DOT(self):
            return self.getToken(D96Parser.DOT, 0)

        def LSB(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.LSB)
            else:
                return self.getToken(D96Parser.LSB, i)

        def RSB(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.RSB)
            else:
                return self.getToken(D96Parser.RSB, i)

        def getRuleIndex(self):
            return D96Parser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 68
        self.enterRecursionRule(localctx, 68, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 398
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.state = 373
                self.match(D96Parser.INTLIT)
                pass

            elif la_ == 2:
                self.state = 374
                self.match(D96Parser.FLOATLIT)
                pass

            elif la_ == 3:
                self.state = 375
                self.match(D96Parser.BOOLLIT)
                pass

            elif la_ == 4:
                self.state = 376
                self.match(D96Parser.STRLIT)
                pass

            elif la_ == 5:
                self.state = 377
                self.match(D96Parser.NULL_)
                pass

            elif la_ == 6:
                self.state = 378
                self.match(D96Parser.SELF_)
                pass

            elif la_ == 7:
                self.state = 379
                self.arrLit()
                pass

            elif la_ == 8:
                self.state = 380
                self.identifier()
                pass

            elif la_ == 9:
                self.state = 381
                self.match(D96Parser.LB)
                self.state = 382
                self.expr(0)
                self.state = 383
                self.match(D96Parser.RB)
                pass

            elif la_ == 10:
                self.state = 385
                self.match(D96Parser.NEW_)
                self.state = 386
                self.match(D96Parser.ID)
                self.state = 387
                self.exprList()
                pass

            elif la_ == 11:
                self.state = 388
                self.match(D96Parser.ID)
                self.state = 389
                self.match(D96Parser.CSMEM)
                self.state = 390
                self.match(D96Parser.VID)
                self.state = 392
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
                if la_ == 1:
                    self.state = 391
                    self.exprList()


                pass

            elif la_ == 12:
                self.state = 394
                self.match(D96Parser.SUBOP)
                self.state = 395
                self.expr(7)
                pass

            elif la_ == 13:
                self.state = 396
                self.match(D96Parser.NOTOP)
                self.state = 397
                self.expr(6)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 432
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,36,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 430
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
                    if la_ == 1:
                        localctx = D96Parser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 400
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 401
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.MULOP) | (1 << D96Parser.DIVOP) | (1 << D96Parser.MODOP))) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 402
                        self.expr(6)
                        pass

                    elif la_ == 2:
                        localctx = D96Parser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 403
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 404
                        _la = self._input.LA(1)
                        if not(_la==D96Parser.ADDOP or _la==D96Parser.SUBOP):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 405
                        self.expr(5)
                        pass

                    elif la_ == 3:
                        localctx = D96Parser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 406
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 407
                        _la = self._input.LA(1)
                        if not(_la==D96Parser.ANDOP or _la==D96Parser.OROP):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 408
                        self.expr(4)
                        pass

                    elif la_ == 4:
                        localctx = D96Parser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 409
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 410
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.EQCMP) | (1 << D96Parser.DIFCMP) | (1 << D96Parser.LESCMP) | (1 << D96Parser.LEQCMP) | (1 << D96Parser.GRECMP) | (1 << D96Parser.GEQCMP))) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 411
                        self.expr(3)
                        pass

                    elif la_ == 5:
                        localctx = D96Parser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 412
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 413
                        _la = self._input.LA(1)
                        if not(_la==D96Parser.SEQCMP or _la==D96Parser.SADDOP):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 414
                        self.expr(2)
                        pass

                    elif la_ == 6:
                        localctx = D96Parser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 415
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 416
                        self.match(D96Parser.DOT)
                        self.state = 417
                        self.match(D96Parser.ID)
                        self.state = 419
                        self._errHandler.sync(self)
                        la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
                        if la_ == 1:
                            self.state = 418
                            self.exprList()


                        pass

                    elif la_ == 7:
                        localctx = D96Parser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 421
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 426 
                        self._errHandler.sync(self)
                        _alt = 1
                        while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                            if _alt == 1:
                                self.state = 422
                                self.match(D96Parser.LSB)
                                self.state = 423
                                self.expr(0)
                                self.state = 424
                                self.match(D96Parser.RSB)

                            else:
                                raise NoViableAltException(self)
                            self.state = 428 
                            self._errHandler.sync(self)
                            _alt = self._interp.adaptivePredict(self._input,34,self._ctx)

                        pass

             
                self.state = 434
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,36,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ExprListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.ExprContext)
            else:
                return self.getTypedRuleContext(D96Parser.ExprContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def getRuleIndex(self):
            return D96Parser.RULE_exprList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprList" ):
                return visitor.visitExprList(self)
            else:
                return visitor.visitChildren(self)




    def exprList(self):

        localctx = D96Parser.ExprListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_exprList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 435
            self.match(D96Parser.LB)
            self.state = 444
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.INTLIT) | (1 << D96Parser.FLOATLIT) | (1 << D96Parser.BOOLLIT) | (1 << D96Parser.STRLIT) | (1 << D96Parser.ARRAY_) | (1 << D96Parser.NULL_) | (1 << D96Parser.NEW_) | (1 << D96Parser.SELF_) | (1 << D96Parser.LB) | (1 << D96Parser.SUBOP) | (1 << D96Parser.NOTOP) | (1 << D96Parser.ID) | (1 << D96Parser.VID))) != 0):
                self.state = 436
                self.expr(0)
                self.state = 441
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==D96Parser.COMMA:
                    self.state = 437
                    self.match(D96Parser.COMMA)
                    self.state = 438
                    self.expr(0)
                    self.state = 443
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 446
            self.match(D96Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrDecContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARRAY_(self):
            return self.getToken(D96Parser.ARRAY_, 0)

        def LSB(self):
            return self.getToken(D96Parser.LSB, 0)

        def vartype(self):
            return self.getTypedRuleContext(D96Parser.VartypeContext,0)


        def COMMA(self):
            return self.getToken(D96Parser.COMMA, 0)

        def INTLIT(self):
            return self.getToken(D96Parser.INTLIT, 0)

        def RSB(self):
            return self.getToken(D96Parser.RSB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_arrDec

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrDec" ):
                return visitor.visitArrDec(self)
            else:
                return visitor.visitChildren(self)




    def arrDec(self):

        localctx = D96Parser.ArrDecContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_arrDec)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 448
            self.match(D96Parser.ARRAY_)
            self.state = 449
            self.match(D96Parser.LSB)
            self.state = 450
            self.vartype()
            self.state = 451
            self.match(D96Parser.COMMA)
            self.state = 452
            self.match(D96Parser.INTLIT)
            self.state = 453
            self.match(D96Parser.RSB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VartypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT_(self):
            return self.getToken(D96Parser.INT_, 0)

        def FLOAT_(self):
            return self.getToken(D96Parser.FLOAT_, 0)

        def BOOL_(self):
            return self.getToken(D96Parser.BOOL_, 0)

        def STR_(self):
            return self.getToken(D96Parser.STR_, 0)

        def arrDec(self):
            return self.getTypedRuleContext(D96Parser.ArrDecContext,0)


        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_vartype

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVartype" ):
                return visitor.visitVartype(self)
            else:
                return visitor.visitChildren(self)




    def vartype(self):

        localctx = D96Parser.VartypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_vartype)
        try:
            self.state = 461
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INT_]:
                self.enterOuterAlt(localctx, 1)
                self.state = 455
                self.match(D96Parser.INT_)
                pass
            elif token in [D96Parser.FLOAT_]:
                self.enterOuterAlt(localctx, 2)
                self.state = 456
                self.match(D96Parser.FLOAT_)
                pass
            elif token in [D96Parser.BOOL_]:
                self.enterOuterAlt(localctx, 3)
                self.state = 457
                self.match(D96Parser.BOOL_)
                pass
            elif token in [D96Parser.STR_]:
                self.enterOuterAlt(localctx, 4)
                self.state = 458
                self.match(D96Parser.STR_)
                pass
            elif token in [D96Parser.ARRAY_]:
                self.enterOuterAlt(localctx, 5)
                self.state = 459
                self.arrDec()
                pass
            elif token in [D96Parser.ID]:
                self.enterOuterAlt(localctx, 6)
                self.state = 460
                self.match(D96Parser.ID)
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


    class ArrLitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARRAY_(self):
            return self.getToken(D96Parser.ARRAY_, 0)

        def exprList(self):
            return self.getTypedRuleContext(D96Parser.ExprListContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_arrLit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrLit" ):
                return visitor.visitArrLit(self)
            else:
                return visitor.visitChildren(self)




    def arrLit(self):

        localctx = D96Parser.ArrLitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_arrLit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 463
            self.match(D96Parser.ARRAY_)
            self.state = 464
            self.exprList()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[19] = self.lhs_sempred
        self._predicates[34] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def lhs_sempred(self, localctx:LhsContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 1)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 8:
                return self.precpred(self._ctx, 8)
         




