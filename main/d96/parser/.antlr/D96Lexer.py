# Generated from g:\sem_212\ppl\assignment\src\main\d96\parser\D96 copy.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2B")
        buf.write("\u0241\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\t")
        buf.write("L\3\2\3\2\3\2\3\2\5\2\u009e\n\2\3\2\3\2\3\3\3\3\3\3\5")
        buf.write("\3\u00a5\n\3\3\3\7\3\u00a8\n\3\f\3\16\3\u00ab\13\3\5\3")
        buf.write("\u00ad\n\3\3\4\3\4\3\4\3\4\5\4\u00b3\n\4\3\4\7\4\u00b6")
        buf.write("\n\4\f\4\16\4\u00b9\13\4\5\4\u00bb\n\4\3\5\3\5\3\5\3\5")
        buf.write("\3\5\5\5\u00c2\n\5\3\5\7\5\u00c5\n\5\f\5\16\5\u00c8\13")
        buf.write("\5\5\5\u00ca\n\5\3\6\3\6\3\6\3\6\3\6\5\6\u00d1\n\6\3\6")
        buf.write("\7\6\u00d4\n\6\f\6\16\6\u00d7\13\6\5\6\u00d9\n\6\3\7\3")
        buf.write("\7\5\7\u00dd\n\7\3\7\5\7\u00e0\n\7\3\7\3\7\3\7\3\7\5\7")
        buf.write("\u00e6\n\7\3\b\3\b\3\b\5\b\u00eb\n\b\3\b\7\b\u00ee\n\b")
        buf.write("\f\b\16\b\u00f1\13\b\5\b\u00f3\n\b\3\t\3\t\7\t\u00f7\n")
        buf.write("\t\f\t\16\t\u00fa\13\t\3\n\3\n\5\n\u00fe\n\n\3\n\3\n\3")
        buf.write("\13\3\13\5\13\u0104\n\13\3\f\3\f\7\f\u0108\n\f\f\f\16")
        buf.write("\f\u010b\13\f\3\f\3\f\3\r\3\r\5\r\u0111\n\r\3\16\3\16")
        buf.write("\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\17\3\17\3\17\5\17\u0125\n\17\3\20\3\20\3")
        buf.write("\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27")
        buf.write("\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\30\3\31\3\31")
        buf.write("\3\31\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\33\3\33")
        buf.write("\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\35\3\35\3\35")
        buf.write("\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3\36\3\36\3\36")
        buf.write("\3\37\3\37\3\37\3\37\3\37\3 \3 \3 \3 \3 \3 \3!\3!\3!\3")
        buf.write("!\3\"\3\"\3\"\3\"\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#")
        buf.write("\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3%\3%\3%\3%\3&\3&\3")
        buf.write("&\3\'\3\'\3\'\3\'\3\'\3(\3(\3)\3)\3*\3*\3+\3+\3,\3,\3")
        buf.write(",\3-\3-\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3\62\3\62\3\63")
        buf.write("\3\63\3\64\3\64\3\65\3\65\3\66\3\66\3\67\3\67\38\38\3")
        buf.write("9\39\39\3:\3:\3:\3;\3;\3;\3<\3<\3=\3=\3=\3>\3>\3?\3?\3")
        buf.write("?\3@\3@\3A\3A\3A\3B\3B\3B\3B\3C\3C\3C\3D\3D\3D\3E\3E\7")
        buf.write("E\u01fe\nE\fE\16E\u0201\13E\3F\3F\6F\u0205\nF\rF\16F\u0206")
        buf.write("\3G\3G\3G\3G\7G\u020d\nG\fG\16G\u0210\13G\3G\3G\3G\3G")
        buf.write("\3G\3H\3H\3H\6H\u021a\nH\rH\16H\u021b\5H\u021e\nH\3I\6")
        buf.write("I\u0221\nI\rI\16I\u0222\3I\3I\3J\3J\3J\3K\3K\7K\u022c")
        buf.write("\nK\fK\16K\u022f\13K\3K\3K\3L\3L\7L\u0235\nL\fL\16L\u0238")
        buf.write("\13L\3L\3L\3L\3L\5L\u023e\nL\3L\3L\3\u0236\2M\3\3\5\2")
        buf.write("\7\2\t\2\13\2\r\4\17\2\21\2\23\2\25\5\27\6\31\2\33\2\35")
        buf.write("\2\37\7!\b#\t%\n\'\13)\f+\r-\16/\17\61\20\63\21\65\22")
        buf.write("\67\239\24;\25=\26?\27A\30C\31E\32G\33I\34K\35M\36O\37")
        buf.write("Q S!U\"W#Y$[%]&_\'a(c)e*g+i,k-m.o/q\60s\61u\62w\63y\64")
        buf.write("{\65}\66\177\67\u00818\u00839\u0085:\u0087;\u0089<\u008b")
        buf.write("=\u008d>\u008f\2\u0091?\u0093@\u0095A\u0097B\3\2\24\3")
        buf.write("\2\62;\3\2\63;\3\2\629\3\2\639\4\2ZZzz\4\2\62;CH\4\2\63")
        buf.write(";CH\4\2DDdd\3\2\62\63\4\2GGgg\4\2--//\7\2\n\f\16\17$$")
        buf.write("))^^\5\2C\\aac|\6\2\62;C\\aac|\3\2%%\5\2\13\f\17\17\"")
        buf.write("\"\3\2$$\t\2))^^ddhhppttvv\2\u025f\2\3\3\2\2\2\2\r\3\2")
        buf.write("\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2")
        buf.write("\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2")
        buf.write("\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65")
        buf.write("\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2")
        buf.write("\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2")
        buf.write("\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2")
        buf.write("\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3")
        buf.write("\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e")
        buf.write("\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2")
        buf.write("o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2")
        buf.write("\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081")
        buf.write("\3\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2")
        buf.write("\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2\2\u008d\3\2\2\2\2\u0091")
        buf.write("\3\2\2\2\2\u0093\3\2\2\2\2\u0095\3\2\2\2\2\u0097\3\2\2")
        buf.write("\2\3\u009d\3\2\2\2\5\u00ac\3\2\2\2\7\u00ae\3\2\2\2\t\u00bc")
        buf.write("\3\2\2\2\13\u00cb\3\2\2\2\r\u00e5\3\2\2\2\17\u00f2\3\2")
        buf.write("\2\2\21\u00f4\3\2\2\2\23\u00fb\3\2\2\2\25\u0103\3\2\2")
        buf.write("\2\27\u0105\3\2\2\2\31\u0110\3\2\2\2\33\u0112\3\2\2\2")
        buf.write("\35\u0124\3\2\2\2\37\u0126\3\2\2\2!\u012c\3\2\2\2#\u0135")
        buf.write("\3\2\2\2%\u0138\3\2\2\2\'\u013f\3\2\2\2)\u0144\3\2\2\2")
        buf.write("+\u014c\3\2\2\2-\u0151\3\2\2\2/\u0157\3\2\2\2\61\u015d")
        buf.write("\3\2\2\2\63\u0160\3\2\2\2\65\u0164\3\2\2\2\67\u016a\3")
        buf.write("\2\2\29\u0172\3\2\2\2;\u0179\3\2\2\2=\u0180\3\2\2\2?\u0185")
        buf.write("\3\2\2\2A\u018b\3\2\2\2C\u018f\3\2\2\2E\u0193\3\2\2\2")
        buf.write("G\u019f\3\2\2\2I\u01aa\3\2\2\2K\u01ae\3\2\2\2M\u01b1\3")
        buf.write("\2\2\2O\u01b6\3\2\2\2Q\u01b8\3\2\2\2S\u01ba\3\2\2\2U\u01bc")
        buf.write("\3\2\2\2W\u01be\3\2\2\2Y\u01c1\3\2\2\2[\u01c3\3\2\2\2")
        buf.write("]\u01c5\3\2\2\2_\u01c7\3\2\2\2a\u01c9\3\2\2\2c\u01cb\3")
        buf.write("\2\2\2e\u01cd\3\2\2\2g\u01cf\3\2\2\2i\u01d1\3\2\2\2k\u01d3")
        buf.write("\3\2\2\2m\u01d5\3\2\2\2o\u01d7\3\2\2\2q\u01d9\3\2\2\2")
        buf.write("s\u01dc\3\2\2\2u\u01df\3\2\2\2w\u01e2\3\2\2\2y\u01e4\3")
        buf.write("\2\2\2{\u01e7\3\2\2\2}\u01e9\3\2\2\2\177\u01ec\3\2\2\2")
        buf.write("\u0081\u01ee\3\2\2\2\u0083\u01f1\3\2\2\2\u0085\u01f5\3")
        buf.write("\2\2\2\u0087\u01f8\3\2\2\2\u0089\u01fb\3\2\2\2\u008b\u0202")
        buf.write("\3\2\2\2\u008d\u0208\3\2\2\2\u008f\u021d\3\2\2\2\u0091")
        buf.write("\u0220\3\2\2\2\u0093\u0226\3\2\2\2\u0095\u0229\3\2\2\2")
        buf.write("\u0097\u0232\3\2\2\2\u0099\u009e\5\5\3\2\u009a\u009e\5")
        buf.write("\7\4\2\u009b\u009e\5\t\5\2\u009c\u009e\5\13\6\2\u009d")
        buf.write("\u0099\3\2\2\2\u009d\u009a\3\2\2\2\u009d\u009b\3\2\2\2")
        buf.write("\u009d\u009c\3\2\2\2\u009e\u009f\3\2\2\2\u009f\u00a0\b")
        buf.write("\2\2\2\u00a0\4\3\2\2\2\u00a1\u00ad\t\2\2\2\u00a2\u00a9")
        buf.write("\t\3\2\2\u00a3\u00a5\7a\2\2\u00a4\u00a3\3\2\2\2\u00a4")
        buf.write("\u00a5\3\2\2\2\u00a5\u00a6\3\2\2\2\u00a6\u00a8\t\2\2\2")
        buf.write("\u00a7\u00a4\3\2\2\2\u00a8\u00ab\3\2\2\2\u00a9\u00a7\3")
        buf.write("\2\2\2\u00a9\u00aa\3\2\2\2\u00aa\u00ad\3\2\2\2\u00ab\u00a9")
        buf.write("\3\2\2\2\u00ac\u00a1\3\2\2\2\u00ac\u00a2\3\2\2\2\u00ad")
        buf.write("\6\3\2\2\2\u00ae\u00ba\7\62\2\2\u00af\u00bb\t\4\2\2\u00b0")
        buf.write("\u00b7\t\5\2\2\u00b1\u00b3\7a\2\2\u00b2\u00b1\3\2\2\2")
        buf.write("\u00b2\u00b3\3\2\2\2\u00b3\u00b4\3\2\2\2\u00b4\u00b6\t")
        buf.write("\4\2\2\u00b5\u00b2\3\2\2\2\u00b6\u00b9\3\2\2\2\u00b7\u00b5")
        buf.write("\3\2\2\2\u00b7\u00b8\3\2\2\2\u00b8\u00bb\3\2\2\2\u00b9")
        buf.write("\u00b7\3\2\2\2\u00ba\u00af\3\2\2\2\u00ba\u00b0\3\2\2\2")
        buf.write("\u00bb\b\3\2\2\2\u00bc\u00bd\7\62\2\2\u00bd\u00c9\t\6")
        buf.write("\2\2\u00be\u00ca\t\7\2\2\u00bf\u00c6\t\b\2\2\u00c0\u00c2")
        buf.write("\7a\2\2\u00c1\u00c0\3\2\2\2\u00c1\u00c2\3\2\2\2\u00c2")
        buf.write("\u00c3\3\2\2\2\u00c3\u00c5\t\7\2\2\u00c4\u00c1\3\2\2\2")
        buf.write("\u00c5\u00c8\3\2\2\2\u00c6\u00c4\3\2\2\2\u00c6\u00c7\3")
        buf.write("\2\2\2\u00c7\u00ca\3\2\2\2\u00c8\u00c6\3\2\2\2\u00c9\u00be")
        buf.write("\3\2\2\2\u00c9\u00bf\3\2\2\2\u00ca\n\3\2\2\2\u00cb\u00cc")
        buf.write("\7\62\2\2\u00cc\u00d8\t\t\2\2\u00cd\u00d9\t\n\2\2\u00ce")
        buf.write("\u00d5\7\63\2\2\u00cf\u00d1\7a\2\2\u00d0\u00cf\3\2\2\2")
        buf.write("\u00d0\u00d1\3\2\2\2\u00d1\u00d2\3\2\2\2\u00d2\u00d4\t")
        buf.write("\n\2\2\u00d3\u00d0\3\2\2\2\u00d4\u00d7\3\2\2\2\u00d5\u00d3")
        buf.write("\3\2\2\2\u00d5\u00d6\3\2\2\2\u00d6\u00d9\3\2\2\2\u00d7")
        buf.write("\u00d5\3\2\2\2\u00d8\u00cd\3\2\2\2\u00d8\u00ce\3\2\2\2")
        buf.write("\u00d9\f\3\2\2\2\u00da\u00dc\5\17\b\2\u00db\u00dd\5\21")
        buf.write("\t\2\u00dc\u00db\3\2\2\2\u00dc\u00dd\3\2\2\2\u00dd\u00df")
        buf.write("\3\2\2\2\u00de\u00e0\5\23\n\2\u00df\u00de\3\2\2\2\u00df")
        buf.write("\u00e0\3\2\2\2\u00e0\u00e6\3\2\2\2\u00e1\u00e2\5\21\t")
        buf.write("\2\u00e2\u00e3\5\23\n\2\u00e3\u00e4\b\7\3\2\u00e4\u00e6")
        buf.write("\3\2\2\2\u00e5\u00da\3\2\2\2\u00e5\u00e1\3\2\2\2\u00e6")
        buf.write("\16\3\2\2\2\u00e7\u00f3\t\2\2\2\u00e8\u00ef\t\3\2\2\u00e9")
        buf.write("\u00eb\7a\2\2\u00ea\u00e9\3\2\2\2\u00ea\u00eb\3\2\2\2")
        buf.write("\u00eb\u00ec\3\2\2\2\u00ec\u00ee\t\2\2\2\u00ed\u00ea\3")
        buf.write("\2\2\2\u00ee\u00f1\3\2\2\2\u00ef\u00ed\3\2\2\2\u00ef\u00f0")
        buf.write("\3\2\2\2\u00f0\u00f3\3\2\2\2\u00f1\u00ef\3\2\2\2\u00f2")
        buf.write("\u00e7\3\2\2\2\u00f2\u00e8\3\2\2\2\u00f3\20\3\2\2\2\u00f4")
        buf.write("\u00f8\7\60\2\2\u00f5\u00f7\t\2\2\2\u00f6\u00f5\3\2\2")
        buf.write("\2\u00f7\u00fa\3\2\2\2\u00f8\u00f6\3\2\2\2\u00f8\u00f9")
        buf.write("\3\2\2\2\u00f9\22\3\2\2\2\u00fa\u00f8\3\2\2\2\u00fb\u00fd")
        buf.write("\t\13\2\2\u00fc\u00fe\t\f\2\2\u00fd\u00fc\3\2\2\2\u00fd")
        buf.write("\u00fe\3\2\2\2\u00fe\u00ff\3\2\2\2\u00ff\u0100\5\17\b")
        buf.write("\2\u0100\24\3\2\2\2\u0101\u0104\5+\26\2\u0102\u0104\5")
        buf.write("-\27\2\u0103\u0101\3\2\2\2\u0103\u0102\3\2\2\2\u0104\26")
        buf.write("\3\2\2\2\u0105\u0109\7$\2\2\u0106\u0108\5\31\r\2\u0107")
        buf.write("\u0106\3\2\2\2\u0108\u010b\3\2\2\2\u0109\u0107\3\2\2\2")
        buf.write("\u0109\u010a\3\2\2\2\u010a\u010c\3\2\2\2\u010b\u0109\3")
        buf.write("\2\2\2\u010c\u010d\7$\2\2\u010d\30\3\2\2\2\u010e\u0111")
        buf.write("\5\33\16\2\u010f\u0111\5\35\17\2\u0110\u010e\3\2\2\2\u0110")
        buf.write("\u010f\3\2\2\2\u0111\32\3\2\2\2\u0112\u0113\n\r\2\2\u0113")
        buf.write("\34\3\2\2\2\u0114\u0115\7^\2\2\u0115\u0125\7d\2\2\u0116")
        buf.write("\u0117\7^\2\2\u0117\u0125\7h\2\2\u0118\u0119\7^\2\2\u0119")
        buf.write("\u0125\7t\2\2\u011a\u011b\7^\2\2\u011b\u0125\7p\2\2\u011c")
        buf.write("\u011d\7^\2\2\u011d\u0125\7v\2\2\u011e\u011f\7^\2\2\u011f")
        buf.write("\u0125\7)\2\2\u0120\u0121\7^\2\2\u0121\u0125\7^\2\2\u0122")
        buf.write("\u0123\7)\2\2\u0123\u0125\7$\2\2\u0124\u0114\3\2\2\2\u0124")
        buf.write("\u0116\3\2\2\2\u0124\u0118\3\2\2\2\u0124\u011a\3\2\2\2")
        buf.write("\u0124\u011c\3\2\2\2\u0124\u011e\3\2\2\2\u0124\u0120\3")
        buf.write("\2\2\2\u0124\u0122\3\2\2\2\u0125\36\3\2\2\2\u0126\u0127")
        buf.write("\7D\2\2\u0127\u0128\7t\2\2\u0128\u0129\7g\2\2\u0129\u012a")
        buf.write("\7c\2\2\u012a\u012b\7m\2\2\u012b \3\2\2\2\u012c\u012d")
        buf.write("\7E\2\2\u012d\u012e\7q\2\2\u012e\u012f\7p\2\2\u012f\u0130")
        buf.write("\7v\2\2\u0130\u0131\7k\2\2\u0131\u0132\7p\2\2\u0132\u0133")
        buf.write("\7w\2\2\u0133\u0134\7g\2\2\u0134\"\3\2\2\2\u0135\u0136")
        buf.write("\7K\2\2\u0136\u0137\7h\2\2\u0137$\3\2\2\2\u0138\u0139")
        buf.write("\7G\2\2\u0139\u013a\7n\2\2\u013a\u013b\7u\2\2\u013b\u013c")
        buf.write("\7g\2\2\u013c\u013d\7k\2\2\u013d\u013e\7h\2\2\u013e&\3")
        buf.write("\2\2\2\u013f\u0140\7G\2\2\u0140\u0141\7n\2\2\u0141\u0142")
        buf.write("\7u\2\2\u0142\u0143\7g\2\2\u0143(\3\2\2\2\u0144\u0145")
        buf.write("\7H\2\2\u0145\u0146\7q\2\2\u0146\u0147\7t\2\2\u0147\u0148")
        buf.write("\7g\2\2\u0148\u0149\7c\2\2\u0149\u014a\7e\2\2\u014a\u014b")
        buf.write("\7j\2\2\u014b*\3\2\2\2\u014c\u014d\7V\2\2\u014d\u014e")
        buf.write("\7t\2\2\u014e\u014f\7w\2\2\u014f\u0150\7g\2\2\u0150,\3")
        buf.write("\2\2\2\u0151\u0152\7H\2\2\u0152\u0153\7c\2\2\u0153\u0154")
        buf.write("\7n\2\2\u0154\u0155\7u\2\2\u0155\u0156\7g\2\2\u0156.\3")
        buf.write("\2\2\2\u0157\u0158\7C\2\2\u0158\u0159\7t\2\2\u0159\u015a")
        buf.write("\7t\2\2\u015a\u015b\7c\2\2\u015b\u015c\7{\2\2\u015c\60")
        buf.write("\3\2\2\2\u015d\u015e\7K\2\2\u015e\u015f\7p\2\2\u015f\62")
        buf.write("\3\2\2\2\u0160\u0161\7K\2\2\u0161\u0162\7p\2\2\u0162\u0163")
        buf.write("\7v\2\2\u0163\64\3\2\2\2\u0164\u0165\7H\2\2\u0165\u0166")
        buf.write("\7n\2\2\u0166\u0167\7q\2\2\u0167\u0168\7c\2\2\u0168\u0169")
        buf.write("\7v\2\2\u0169\66\3\2\2\2\u016a\u016b\7D\2\2\u016b\u016c")
        buf.write("\7q\2\2\u016c\u016d\7q\2\2\u016d\u016e\7n\2\2\u016e\u016f")
        buf.write("\7g\2\2\u016f\u0170\7c\2\2\u0170\u0171\7p\2\2\u01718\3")
        buf.write("\2\2\2\u0172\u0173\7U\2\2\u0173\u0174\7v\2\2\u0174\u0175")
        buf.write("\7t\2\2\u0175\u0176\7k\2\2\u0176\u0177\7p\2\2\u0177\u0178")
        buf.write("\7i\2\2\u0178:\3\2\2\2\u0179\u017a\7T\2\2\u017a\u017b")
        buf.write("\7g\2\2\u017b\u017c\7v\2\2\u017c\u017d\7w\2\2\u017d\u017e")
        buf.write("\7t\2\2\u017e\u017f\7p\2\2\u017f<\3\2\2\2\u0180\u0181")
        buf.write("\7P\2\2\u0181\u0182\7w\2\2\u0182\u0183\7n\2\2\u0183\u0184")
        buf.write("\7n\2\2\u0184>\3\2\2\2\u0185\u0186\7E\2\2\u0186\u0187")
        buf.write("\7n\2\2\u0187\u0188\7c\2\2\u0188\u0189\7u\2\2\u0189\u018a")
        buf.write("\7u\2\2\u018a@\3\2\2\2\u018b\u018c\7X\2\2\u018c\u018d")
        buf.write("\7c\2\2\u018d\u018e\7n\2\2\u018eB\3\2\2\2\u018f\u0190")
        buf.write("\7X\2\2\u0190\u0191\7c\2\2\u0191\u0192\7t\2\2\u0192D\3")
        buf.write("\2\2\2\u0193\u0194\7E\2\2\u0194\u0195\7q\2\2\u0195\u0196")
        buf.write("\7p\2\2\u0196\u0197\7u\2\2\u0197\u0198\7v\2\2\u0198\u0199")
        buf.write("\7t\2\2\u0199\u019a\7w\2\2\u019a\u019b\7e\2\2\u019b\u019c")
        buf.write("\7v\2\2\u019c\u019d\7q\2\2\u019d\u019e\7t\2\2\u019eF\3")
        buf.write("\2\2\2\u019f\u01a0\7F\2\2\u01a0\u01a1\7g\2\2\u01a1\u01a2")
        buf.write("\7u\2\2\u01a2\u01a3\7v\2\2\u01a3\u01a4\7t\2\2\u01a4\u01a5")
        buf.write("\7w\2\2\u01a5\u01a6\7e\2\2\u01a6\u01a7\7v\2\2\u01a7\u01a8")
        buf.write("\7q\2\2\u01a8\u01a9\7t\2\2\u01a9H\3\2\2\2\u01aa\u01ab")
        buf.write("\7P\2\2\u01ab\u01ac\7g\2\2\u01ac\u01ad\7y\2\2\u01adJ\3")
        buf.write("\2\2\2\u01ae\u01af\7D\2\2\u01af\u01b0\7{\2\2\u01b0L\3")
        buf.write("\2\2\2\u01b1\u01b2\7U\2\2\u01b2\u01b3\7g\2\2\u01b3\u01b4")
        buf.write("\7n\2\2\u01b4\u01b5\7h\2\2\u01b5N\3\2\2\2\u01b6\u01b7")
        buf.write("\7=\2\2\u01b7P\3\2\2\2\u01b8\u01b9\7<\2\2\u01b9R\3\2\2")
        buf.write("\2\u01ba\u01bb\7.\2\2\u01bbT\3\2\2\2\u01bc\u01bd\7\60")
        buf.write("\2\2\u01bdV\3\2\2\2\u01be\u01bf\7\60\2\2\u01bf\u01c0\7")
        buf.write("\60\2\2\u01c0X\3\2\2\2\u01c1\u01c2\7*\2\2\u01c2Z\3\2\2")
        buf.write("\2\u01c3\u01c4\7+\2\2\u01c4\\\3\2\2\2\u01c5\u01c6\7]\2")
        buf.write("\2\u01c6^\3\2\2\2\u01c7\u01c8\7_\2\2\u01c8`\3\2\2\2\u01c9")
        buf.write("\u01ca\7}\2\2\u01cab\3\2\2\2\u01cb\u01cc\7\177\2\2\u01cc")
        buf.write("d\3\2\2\2\u01cd\u01ce\7-\2\2\u01cef\3\2\2\2\u01cf\u01d0")
        buf.write("\7/\2\2\u01d0h\3\2\2\2\u01d1\u01d2\7,\2\2\u01d2j\3\2\2")
        buf.write("\2\u01d3\u01d4\7\61\2\2\u01d4l\3\2\2\2\u01d5\u01d6\7\'")
        buf.write("\2\2\u01d6n\3\2\2\2\u01d7\u01d8\7#\2\2\u01d8p\3\2\2\2")
        buf.write("\u01d9\u01da\7(\2\2\u01da\u01db\7(\2\2\u01dbr\3\2\2\2")
        buf.write("\u01dc\u01dd\7~\2\2\u01dd\u01de\7~\2\2\u01det\3\2\2\2")
        buf.write("\u01df\u01e0\7?\2\2\u01e0\u01e1\7?\2\2\u01e1v\3\2\2\2")
        buf.write("\u01e2\u01e3\7?\2\2\u01e3x\3\2\2\2\u01e4\u01e5\7#\2\2")
        buf.write("\u01e5\u01e6\7?\2\2\u01e6z\3\2\2\2\u01e7\u01e8\7>\2\2")
        buf.write("\u01e8|\3\2\2\2\u01e9\u01ea\7>\2\2\u01ea\u01eb\7?\2\2")
        buf.write("\u01eb~\3\2\2\2\u01ec\u01ed\7@\2\2\u01ed\u0080\3\2\2\2")
        buf.write("\u01ee\u01ef\7@\2\2\u01ef\u01f0\7?\2\2\u01f0\u0082\3\2")
        buf.write("\2\2\u01f1\u01f2\7?\2\2\u01f2\u01f3\7?\2\2\u01f3\u01f4")
        buf.write("\7\60\2\2\u01f4\u0084\3\2\2\2\u01f5\u01f6\7-\2\2\u01f6")
        buf.write("\u01f7\7\60\2\2\u01f7\u0086\3\2\2\2\u01f8\u01f9\7<\2\2")
        buf.write("\u01f9\u01fa\7<\2\2\u01fa\u0088\3\2\2\2\u01fb\u01ff\t")
        buf.write("\16\2\2\u01fc\u01fe\t\17\2\2\u01fd\u01fc\3\2\2\2\u01fe")
        buf.write("\u0201\3\2\2\2\u01ff\u01fd\3\2\2\2\u01ff\u0200\3\2\2\2")
        buf.write("\u0200\u008a\3\2\2\2\u0201\u01ff\3\2\2\2\u0202\u0204\7")
        buf.write("&\2\2\u0203\u0205\t\17\2\2\u0204\u0203\3\2\2\2\u0205\u0206")
        buf.write("\3\2\2\2\u0206\u0204\3\2\2\2\u0206\u0207\3\2\2\2\u0207")
        buf.write("\u008c\3\2\2\2\u0208\u0209\7%\2\2\u0209\u020a\7%\2\2\u020a")
        buf.write("\u020e\3\2\2\2\u020b\u020d\5\u008fH\2\u020c\u020b\3\2")
        buf.write("\2\2\u020d\u0210\3\2\2\2\u020e\u020c\3\2\2\2\u020e\u020f")
        buf.write("\3\2\2\2\u020f\u0211\3\2\2\2\u0210\u020e\3\2\2\2\u0211")
        buf.write("\u0212\7%\2\2\u0212\u0213\7%\2\2\u0213\u0214\3\2\2\2\u0214")
        buf.write("\u0215\bG\4\2\u0215\u008e\3\2\2\2\u0216\u021e\n\20\2\2")
        buf.write("\u0217\u0219\7%\2\2\u0218\u021a\n\20\2\2\u0219\u0218\3")
        buf.write("\2\2\2\u021a\u021b\3\2\2\2\u021b\u0219\3\2\2\2\u021b\u021c")
        buf.write("\3\2\2\2\u021c\u021e\3\2\2\2\u021d\u0216\3\2\2\2\u021d")
        buf.write("\u0217\3\2\2\2\u021e\u0090\3\2\2\2\u021f\u0221\t\21\2")
        buf.write("\2\u0220\u021f\3\2\2\2\u0221\u0222\3\2\2\2\u0222\u0220")
        buf.write("\3\2\2\2\u0222\u0223\3\2\2\2\u0223\u0224\3\2\2\2\u0224")
        buf.write("\u0225\bI\4\2\u0225\u0092\3\2\2\2\u0226\u0227\13\2\2\2")
        buf.write("\u0227\u0228\bJ\5\2\u0228\u0094\3\2\2\2\u0229\u022d\7")
        buf.write("$\2\2\u022a\u022c\5\31\r\2\u022b\u022a\3\2\2\2\u022c\u022f")
        buf.write("\3\2\2\2\u022d\u022b\3\2\2\2\u022d\u022e\3\2\2\2\u022e")
        buf.write("\u0230\3\2\2\2\u022f\u022d\3\2\2\2\u0230\u0231\bK\6\2")
        buf.write("\u0231\u0096\3\2\2\2\u0232\u0236\7$\2\2\u0233\u0235\n")
        buf.write("\22\2\2\u0234\u0233\3\2\2\2\u0235\u0238\3\2\2\2\u0236")
        buf.write("\u0237\3\2\2\2\u0236\u0234\3\2\2\2\u0237\u023d\3\2\2\2")
        buf.write("\u0238\u0236\3\2\2\2\u0239\u023a\7^\2\2\u023a\u023e\n")
        buf.write("\23\2\2\u023b\u023c\7)\2\2\u023c\u023e\n\22\2\2\u023d")
        buf.write("\u0239\3\2\2\2\u023d\u023b\3\2\2\2\u023e\u023f\3\2\2\2")
        buf.write("\u023f\u0240\bL\7\2\u0240\u0098\3\2\2\2%\2\u009d\u00a4")
        buf.write("\u00a9\u00ac\u00b2\u00b7\u00ba\u00c1\u00c6\u00c9\u00d0")
        buf.write("\u00d5\u00d8\u00dc\u00df\u00e5\u00ea\u00ef\u00f2\u00f8")
        buf.write("\u00fd\u0103\u0109\u0110\u0124\u01ff\u0206\u020e\u021b")
        buf.write("\u021d\u0222\u022d\u0236\u023d\b\3\2\2\3\7\3\b\2\2\3J")
        buf.write("\4\3K\5\3L\6")
        return buf.getvalue()


class D96Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    INTLIT = 1
    FLOATLIT = 2
    BOOLLIT = 3
    STRLIT = 4
    BREAK_ = 5
    CONTINUE_ = 6
    IF_ = 7
    ELSEIF_ = 8
    ELSE_ = 9
    FOREACH_ = 10
    TRUE_ = 11
    FALSE_ = 12
    ARRAY_ = 13
    IN_ = 14
    INT_ = 15
    FLOAT_ = 16
    BOOL_ = 17
    STR_ = 18
    RETURN_ = 19
    NULL_ = 20
    CLASS_ = 21
    VAL_ = 22
    VAR_ = 23
    CONSTRUCTOR_ = 24
    DESTRUCTOR_ = 25
    NEW_ = 26
    BY_ = 27
    SELF_ = 28
    SEMI = 29
    COLON = 30
    COMMA = 31
    DOT = 32
    DOUBLEDOT = 33
    LB = 34
    RB = 35
    LSB = 36
    RSB = 37
    LCB = 38
    RCB = 39
    ADDOP = 40
    SUBOP = 41
    MULOP = 42
    DIVOP = 43
    MODOP = 44
    NOTOP = 45
    ANDOP = 46
    OROP = 47
    EQCMP = 48
    ASNOP = 49
    DIFCMP = 50
    LESCMP = 51
    LEQCMP = 52
    GRECMP = 53
    GEQCMP = 54
    SEQCMP = 55
    SADDOP = 56
    CSMEM = 57
    ID = 58
    VID = 59
    COMMENT = 60
    WS = 61
    ERROR_CHAR = 62
    UNCLOSE_STRING = 63
    ILLEGAL_ESCAPE = 64

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'Break'", "'Continue'", "'If'", "'Elseif'", "'Else'", "'Foreach'", 
            "'True'", "'False'", "'Array'", "'In'", "'Int'", "'Float'", 
            "'Boolean'", "'String'", "'Return'", "'Null'", "'Class'", "'Val'", 
            "'Var'", "'Constructor'", "'Destructor'", "'New'", "'By'", "'Self'", 
            "';'", "':'", "','", "'.'", "'..'", "'('", "')'", "'['", "']'", 
            "'{'", "'}'", "'+'", "'-'", "'*'", "'/'", "'%'", "'!'", "'&&'", 
            "'||'", "'=='", "'='", "'!='", "'<'", "'<='", "'>'", "'>='", 
            "'==.'", "'+.'", "'::'" ]

    symbolicNames = [ "<INVALID>",
            "INTLIT", "FLOATLIT", "BOOLLIT", "STRLIT", "BREAK_", "CONTINUE_", 
            "IF_", "ELSEIF_", "ELSE_", "FOREACH_", "TRUE_", "FALSE_", "ARRAY_", 
            "IN_", "INT_", "FLOAT_", "BOOL_", "STR_", "RETURN_", "NULL_", 
            "CLASS_", "VAL_", "VAR_", "CONSTRUCTOR_", "DESTRUCTOR_", "NEW_", 
            "BY_", "SELF_", "SEMI", "COLON", "COMMA", "DOT", "DOUBLEDOT", 
            "LB", "RB", "LSB", "RSB", "LCB", "RCB", "ADDOP", "SUBOP", "MULOP", 
            "DIVOP", "MODOP", "NOTOP", "ANDOP", "OROP", "EQCMP", "ASNOP", 
            "DIFCMP", "LESCMP", "LEQCMP", "GRECMP", "GEQCMP", "SEQCMP", 
            "SADDOP", "CSMEM", "ID", "VID", "COMMENT", "WS", "ERROR_CHAR", 
            "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "INTLIT", "DECLIT", "OCTLIT", "HEXLIT", "BINLIT", "FLOATLIT", 
                  "INT_PART", "DEC_PART", "EXP_PART", "BOOLLIT", "STRLIT", 
                  "STR_CHAR", "REGULAR_CHAR", "SPECIAL_CHAR", "BREAK_", 
                  "CONTINUE_", "IF_", "ELSEIF_", "ELSE_", "FOREACH_", "TRUE_", 
                  "FALSE_", "ARRAY_", "IN_", "INT_", "FLOAT_", "BOOL_", 
                  "STR_", "RETURN_", "NULL_", "CLASS_", "VAL_", "VAR_", 
                  "CONSTRUCTOR_", "DESTRUCTOR_", "NEW_", "BY_", "SELF_", 
                  "SEMI", "COLON", "COMMA", "DOT", "DOUBLEDOT", "LB", "RB", 
                  "LSB", "RSB", "LCB", "RCB", "ADDOP", "SUBOP", "MULOP", 
                  "DIVOP", "MODOP", "NOTOP", "ANDOP", "OROP", "EQCMP", "ASNOP", 
                  "DIFCMP", "LESCMP", "LEQCMP", "GRECMP", "GEQCMP", "SEQCMP", 
                  "SADDOP", "CSMEM", "ID", "VID", "COMMENT", "CMT_CHAR", 
                  "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    grammarFileName = "D96 copy.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[0] = self.INTLIT_action 
            actions[5] = self.FLOATLIT_action 
            actions[72] = self.ERROR_CHAR_action 
            actions[73] = self.UNCLOSE_STRING_action 
            actions[74] = self.ILLEGAL_ESCAPE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def INTLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text.replace('_','')
     

    def FLOATLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            self.text = self.text.replace('_','')
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            raise ErrorToken(self.text)
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            raise UncloseString(self.text[1:])
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:
            raise IllegalEscape(self.text[1:])
     


