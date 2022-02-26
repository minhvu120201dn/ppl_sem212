# Generated from g:\sem_212\ppl\assignment1\src\main\d96\parser\D96.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2B")
        buf.write("\u023d\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("\7\5\7\u00dd\n\7\3\7\5\7\u00e0\n\7\3\7\3\7\3\b\3\b\3\b")
        buf.write("\5\b\u00e7\n\b\3\b\7\b\u00ea\n\b\f\b\16\b\u00ed\13\b\5")
        buf.write("\b\u00ef\n\b\3\t\3\t\7\t\u00f3\n\t\f\t\16\t\u00f6\13\t")
        buf.write("\3\n\3\n\5\n\u00fa\n\n\3\n\3\n\3\13\3\13\5\13\u0100\n")
        buf.write("\13\3\f\3\f\7\f\u0104\n\f\f\f\16\f\u0107\13\f\3\f\3\f")
        buf.write("\3\r\3\r\5\r\u010d\n\r\3\16\3\16\3\17\3\17\3\17\3\17\3")
        buf.write("\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\5\17\u0121\n\17\3\20\3\20\3\20\3\20\3\20\3\20\3")
        buf.write("\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22")
        buf.write("\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\26")
        buf.write("\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\27\3\30")
        buf.write("\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\32\3\32\3\32")
        buf.write("\3\32\3\33\3\33\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34")
        buf.write("\3\34\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3\35\3\35")
        buf.write("\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\37\3\37\3\37\3\37")
        buf.write("\3\37\3 \3 \3 \3 \3 \3 \3!\3!\3!\3!\3\"\3\"\3\"\3\"\3")
        buf.write("#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3$\3$\3$\3$\3$\3$\3")
        buf.write("$\3$\3$\3$\3$\3%\3%\3%\3%\3&\3&\3&\3\'\3\'\3\'\3\'\3\'")
        buf.write("\3(\3(\3)\3)\3*\3*\3+\3+\3,\3,\3,\3-\3-\3.\3.\3/\3/\3")
        buf.write("\60\3\60\3\61\3\61\3\62\3\62\3\63\3\63\3\64\3\64\3\65")
        buf.write("\3\65\3\66\3\66\3\67\3\67\38\38\39\39\39\3:\3:\3:\3;\3")
        buf.write(";\3;\3<\3<\3=\3=\3=\3>\3>\3?\3?\3?\3@\3@\3A\3A\3A\3B\3")
        buf.write("B\3B\3B\3C\3C\3C\3D\3D\3D\3E\3E\7E\u01fa\nE\fE\16E\u01fd")
        buf.write("\13E\3F\3F\6F\u0201\nF\rF\16F\u0202\3G\3G\3G\3G\7G\u0209")
        buf.write("\nG\fG\16G\u020c\13G\3G\3G\3G\3G\3G\3H\3H\3H\6H\u0216")
        buf.write("\nH\rH\16H\u0217\5H\u021a\nH\3I\6I\u021d\nI\rI\16I\u021e")
        buf.write("\3I\3I\3J\3J\3J\3K\3K\7K\u0228\nK\fK\16K\u022b\13K\3K")
        buf.write("\3K\3L\3L\7L\u0231\nL\fL\16L\u0234\13L\3L\3L\3L\3L\5L")
        buf.write("\u023a\nL\3L\3L\3\u0232\2M\3\3\5\2\7\2\t\2\13\2\r\4\17")
        buf.write("\2\21\2\23\2\25\5\27\6\31\2\33\2\35\2\37\7!\b#\t%\n\'")
        buf.write("\13)\f+\r-\16/\17\61\20\63\21\65\22\67\239\24;\25=\26")
        buf.write("?\27A\30C\31E\32G\33I\34K\35M\36O\37Q S!U\"W#Y$[%]&_\'")
        buf.write("a(c)e*g+i,k-m.o/q\60s\61u\62w\63y\64{\65}\66\177\67\u0081")
        buf.write("8\u00839\u0085:\u0087;\u0089<\u008b=\u008d>\u008f\2\u0091")
        buf.write("?\u0093@\u0095A\u0097B\3\2\24\3\2\62;\3\2\63;\3\2\629")
        buf.write("\3\2\639\4\2ZZzz\4\2\62;CH\4\2\63;CH\4\2DDdd\3\2\62\63")
        buf.write("\4\2GGgg\4\2--//\7\2\n\f\16\17$$))^^\5\2C\\aac|\6\2\62")
        buf.write(";C\\aac|\3\2%%\5\2\13\f\17\17\"\"\3\2$$\t\2))^^ddhhpp")
        buf.write("ttvv\2\u025a\2\3\3\2\2\2\2\r\3\2\2\2\2\25\3\2\2\2\2\27")
        buf.write("\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2")
        buf.write("\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2")
        buf.write("\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2")
        buf.write("\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2")
        buf.write("\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2")
        buf.write("\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3")
        buf.write("\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_")
        buf.write("\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2")
        buf.write("i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2")
        buf.write("\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2")
        buf.write("\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083\3")
        buf.write("\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2\2")
        buf.write("\2\u008b\3\2\2\2\2\u008d\3\2\2\2\2\u0091\3\2\2\2\2\u0093")
        buf.write("\3\2\2\2\2\u0095\3\2\2\2\2\u0097\3\2\2\2\3\u009d\3\2\2")
        buf.write("\2\5\u00ac\3\2\2\2\7\u00ae\3\2\2\2\t\u00bc\3\2\2\2\13")
        buf.write("\u00cb\3\2\2\2\r\u00da\3\2\2\2\17\u00ee\3\2\2\2\21\u00f0")
        buf.write("\3\2\2\2\23\u00f7\3\2\2\2\25\u00ff\3\2\2\2\27\u0101\3")
        buf.write("\2\2\2\31\u010c\3\2\2\2\33\u010e\3\2\2\2\35\u0120\3\2")
        buf.write("\2\2\37\u0122\3\2\2\2!\u0128\3\2\2\2#\u0131\3\2\2\2%\u0134")
        buf.write("\3\2\2\2\'\u013b\3\2\2\2)\u0140\3\2\2\2+\u0148\3\2\2\2")
        buf.write("-\u014d\3\2\2\2/\u0153\3\2\2\2\61\u0159\3\2\2\2\63\u015c")
        buf.write("\3\2\2\2\65\u0160\3\2\2\2\67\u0166\3\2\2\29\u016e\3\2")
        buf.write("\2\2;\u0175\3\2\2\2=\u017c\3\2\2\2?\u0181\3\2\2\2A\u0187")
        buf.write("\3\2\2\2C\u018b\3\2\2\2E\u018f\3\2\2\2G\u019b\3\2\2\2")
        buf.write("I\u01a6\3\2\2\2K\u01aa\3\2\2\2M\u01ad\3\2\2\2O\u01b2\3")
        buf.write("\2\2\2Q\u01b4\3\2\2\2S\u01b6\3\2\2\2U\u01b8\3\2\2\2W\u01ba")
        buf.write("\3\2\2\2Y\u01bd\3\2\2\2[\u01bf\3\2\2\2]\u01c1\3\2\2\2")
        buf.write("_\u01c3\3\2\2\2a\u01c5\3\2\2\2c\u01c7\3\2\2\2e\u01c9\3")
        buf.write("\2\2\2g\u01cb\3\2\2\2i\u01cd\3\2\2\2k\u01cf\3\2\2\2m\u01d1")
        buf.write("\3\2\2\2o\u01d3\3\2\2\2q\u01d5\3\2\2\2s\u01d8\3\2\2\2")
        buf.write("u\u01db\3\2\2\2w\u01de\3\2\2\2y\u01e0\3\2\2\2{\u01e3\3")
        buf.write("\2\2\2}\u01e5\3\2\2\2\177\u01e8\3\2\2\2\u0081\u01ea\3")
        buf.write("\2\2\2\u0083\u01ed\3\2\2\2\u0085\u01f1\3\2\2\2\u0087\u01f4")
        buf.write("\3\2\2\2\u0089\u01f7\3\2\2\2\u008b\u01fe\3\2\2\2\u008d")
        buf.write("\u0204\3\2\2\2\u008f\u0219\3\2\2\2\u0091\u021c\3\2\2\2")
        buf.write("\u0093\u0222\3\2\2\2\u0095\u0225\3\2\2\2\u0097\u022e\3")
        buf.write("\2\2\2\u0099\u009e\5\5\3\2\u009a\u009e\5\7\4\2\u009b\u009e")
        buf.write("\5\t\5\2\u009c\u009e\5\13\6\2\u009d\u0099\3\2\2\2\u009d")
        buf.write("\u009a\3\2\2\2\u009d\u009b\3\2\2\2\u009d\u009c\3\2\2\2")
        buf.write("\u009e\u009f\3\2\2\2\u009f\u00a0\b\2\2\2\u00a0\4\3\2\2")
        buf.write("\2\u00a1\u00ad\t\2\2\2\u00a2\u00a9\t\3\2\2\u00a3\u00a5")
        buf.write("\7a\2\2\u00a4\u00a3\3\2\2\2\u00a4\u00a5\3\2\2\2\u00a5")
        buf.write("\u00a6\3\2\2\2\u00a6\u00a8\t\2\2\2\u00a7\u00a4\3\2\2\2")
        buf.write("\u00a8\u00ab\3\2\2\2\u00a9\u00a7\3\2\2\2\u00a9\u00aa\3")
        buf.write("\2\2\2\u00aa\u00ad\3\2\2\2\u00ab\u00a9\3\2\2\2\u00ac\u00a1")
        buf.write("\3\2\2\2\u00ac\u00a2\3\2\2\2\u00ad\6\3\2\2\2\u00ae\u00ba")
        buf.write("\7\62\2\2\u00af\u00bb\t\4\2\2\u00b0\u00b7\t\5\2\2\u00b1")
        buf.write("\u00b3\7a\2\2\u00b2\u00b1\3\2\2\2\u00b2\u00b3\3\2\2\2")
        buf.write("\u00b3\u00b4\3\2\2\2\u00b4\u00b6\t\4\2\2\u00b5\u00b2\3")
        buf.write("\2\2\2\u00b6\u00b9\3\2\2\2\u00b7\u00b5\3\2\2\2\u00b7\u00b8")
        buf.write("\3\2\2\2\u00b8\u00bb\3\2\2\2\u00b9\u00b7\3\2\2\2\u00ba")
        buf.write("\u00af\3\2\2\2\u00ba\u00b0\3\2\2\2\u00bb\b\3\2\2\2\u00bc")
        buf.write("\u00bd\7\62\2\2\u00bd\u00c9\t\6\2\2\u00be\u00ca\t\7\2")
        buf.write("\2\u00bf\u00c6\t\b\2\2\u00c0\u00c2\7a\2\2\u00c1\u00c0")
        buf.write("\3\2\2\2\u00c1\u00c2\3\2\2\2\u00c2\u00c3\3\2\2\2\u00c3")
        buf.write("\u00c5\t\7\2\2\u00c4\u00c1\3\2\2\2\u00c5\u00c8\3\2\2\2")
        buf.write("\u00c6\u00c4\3\2\2\2\u00c6\u00c7\3\2\2\2\u00c7\u00ca\3")
        buf.write("\2\2\2\u00c8\u00c6\3\2\2\2\u00c9\u00be\3\2\2\2\u00c9\u00bf")
        buf.write("\3\2\2\2\u00ca\n\3\2\2\2\u00cb\u00cc\7\62\2\2\u00cc\u00d8")
        buf.write("\t\t\2\2\u00cd\u00d9\t\n\2\2\u00ce\u00d5\7\63\2\2\u00cf")
        buf.write("\u00d1\7a\2\2\u00d0\u00cf\3\2\2\2\u00d0\u00d1\3\2\2\2")
        buf.write("\u00d1\u00d2\3\2\2\2\u00d2\u00d4\t\n\2\2\u00d3\u00d0\3")
        buf.write("\2\2\2\u00d4\u00d7\3\2\2\2\u00d5\u00d3\3\2\2\2\u00d5\u00d6")
        buf.write("\3\2\2\2\u00d6\u00d9\3\2\2\2\u00d7\u00d5\3\2\2\2\u00d8")
        buf.write("\u00cd\3\2\2\2\u00d8\u00ce\3\2\2\2\u00d9\f\3\2\2\2\u00da")
        buf.write("\u00dc\5\17\b\2\u00db\u00dd\5\21\t\2\u00dc\u00db\3\2\2")
        buf.write("\2\u00dc\u00dd\3\2\2\2\u00dd\u00df\3\2\2\2\u00de\u00e0")
        buf.write("\5\23\n\2\u00df\u00de\3\2\2\2\u00df\u00e0\3\2\2\2\u00e0")
        buf.write("\u00e1\3\2\2\2\u00e1\u00e2\b\7\3\2\u00e2\16\3\2\2\2\u00e3")
        buf.write("\u00ef\t\2\2\2\u00e4\u00eb\t\3\2\2\u00e5\u00e7\7a\2\2")
        buf.write("\u00e6\u00e5\3\2\2\2\u00e6\u00e7\3\2\2\2\u00e7\u00e8\3")
        buf.write("\2\2\2\u00e8\u00ea\t\2\2\2\u00e9\u00e6\3\2\2\2\u00ea\u00ed")
        buf.write("\3\2\2\2\u00eb\u00e9\3\2\2\2\u00eb\u00ec\3\2\2\2\u00ec")
        buf.write("\u00ef\3\2\2\2\u00ed\u00eb\3\2\2\2\u00ee\u00e3\3\2\2\2")
        buf.write("\u00ee\u00e4\3\2\2\2\u00ef\20\3\2\2\2\u00f0\u00f4\7\60")
        buf.write("\2\2\u00f1\u00f3\t\2\2\2\u00f2\u00f1\3\2\2\2\u00f3\u00f6")
        buf.write("\3\2\2\2\u00f4\u00f2\3\2\2\2\u00f4\u00f5\3\2\2\2\u00f5")
        buf.write("\22\3\2\2\2\u00f6\u00f4\3\2\2\2\u00f7\u00f9\t\13\2\2\u00f8")
        buf.write("\u00fa\t\f\2\2\u00f9\u00f8\3\2\2\2\u00f9\u00fa\3\2\2\2")
        buf.write("\u00fa\u00fb\3\2\2\2\u00fb\u00fc\5\17\b\2\u00fc\24\3\2")
        buf.write("\2\2\u00fd\u0100\5+\26\2\u00fe\u0100\5-\27\2\u00ff\u00fd")
        buf.write("\3\2\2\2\u00ff\u00fe\3\2\2\2\u0100\26\3\2\2\2\u0101\u0105")
        buf.write("\7$\2\2\u0102\u0104\5\31\r\2\u0103\u0102\3\2\2\2\u0104")
        buf.write("\u0107\3\2\2\2\u0105\u0103\3\2\2\2\u0105\u0106\3\2\2\2")
        buf.write("\u0106\u0108\3\2\2\2\u0107\u0105\3\2\2\2\u0108\u0109\7")
        buf.write("$\2\2\u0109\30\3\2\2\2\u010a\u010d\5\33\16\2\u010b\u010d")
        buf.write("\5\35\17\2\u010c\u010a\3\2\2\2\u010c\u010b\3\2\2\2\u010d")
        buf.write("\32\3\2\2\2\u010e\u010f\n\r\2\2\u010f\34\3\2\2\2\u0110")
        buf.write("\u0111\7^\2\2\u0111\u0121\7d\2\2\u0112\u0113\7^\2\2\u0113")
        buf.write("\u0121\7h\2\2\u0114\u0115\7^\2\2\u0115\u0121\7t\2\2\u0116")
        buf.write("\u0117\7^\2\2\u0117\u0121\7p\2\2\u0118\u0119\7^\2\2\u0119")
        buf.write("\u0121\7v\2\2\u011a\u011b\7^\2\2\u011b\u0121\7)\2\2\u011c")
        buf.write("\u011d\7^\2\2\u011d\u0121\7^\2\2\u011e\u011f\7)\2\2\u011f")
        buf.write("\u0121\7$\2\2\u0120\u0110\3\2\2\2\u0120\u0112\3\2\2\2")
        buf.write("\u0120\u0114\3\2\2\2\u0120\u0116\3\2\2\2\u0120\u0118\3")
        buf.write("\2\2\2\u0120\u011a\3\2\2\2\u0120\u011c\3\2\2\2\u0120\u011e")
        buf.write("\3\2\2\2\u0121\36\3\2\2\2\u0122\u0123\7D\2\2\u0123\u0124")
        buf.write("\7t\2\2\u0124\u0125\7g\2\2\u0125\u0126\7c\2\2\u0126\u0127")
        buf.write("\7m\2\2\u0127 \3\2\2\2\u0128\u0129\7E\2\2\u0129\u012a")
        buf.write("\7q\2\2\u012a\u012b\7p\2\2\u012b\u012c\7v\2\2\u012c\u012d")
        buf.write("\7k\2\2\u012d\u012e\7p\2\2\u012e\u012f\7w\2\2\u012f\u0130")
        buf.write("\7g\2\2\u0130\"\3\2\2\2\u0131\u0132\7K\2\2\u0132\u0133")
        buf.write("\7h\2\2\u0133$\3\2\2\2\u0134\u0135\7G\2\2\u0135\u0136")
        buf.write("\7n\2\2\u0136\u0137\7u\2\2\u0137\u0138\7g\2\2\u0138\u0139")
        buf.write("\7k\2\2\u0139\u013a\7h\2\2\u013a&\3\2\2\2\u013b\u013c")
        buf.write("\7G\2\2\u013c\u013d\7n\2\2\u013d\u013e\7u\2\2\u013e\u013f")
        buf.write("\7g\2\2\u013f(\3\2\2\2\u0140\u0141\7H\2\2\u0141\u0142")
        buf.write("\7q\2\2\u0142\u0143\7t\2\2\u0143\u0144\7g\2\2\u0144\u0145")
        buf.write("\7c\2\2\u0145\u0146\7e\2\2\u0146\u0147\7j\2\2\u0147*\3")
        buf.write("\2\2\2\u0148\u0149\7V\2\2\u0149\u014a\7t\2\2\u014a\u014b")
        buf.write("\7w\2\2\u014b\u014c\7g\2\2\u014c,\3\2\2\2\u014d\u014e")
        buf.write("\7H\2\2\u014e\u014f\7c\2\2\u014f\u0150\7n\2\2\u0150\u0151")
        buf.write("\7u\2\2\u0151\u0152\7g\2\2\u0152.\3\2\2\2\u0153\u0154")
        buf.write("\7C\2\2\u0154\u0155\7t\2\2\u0155\u0156\7t\2\2\u0156\u0157")
        buf.write("\7c\2\2\u0157\u0158\7{\2\2\u0158\60\3\2\2\2\u0159\u015a")
        buf.write("\7K\2\2\u015a\u015b\7p\2\2\u015b\62\3\2\2\2\u015c\u015d")
        buf.write("\7K\2\2\u015d\u015e\7p\2\2\u015e\u015f\7v\2\2\u015f\64")
        buf.write("\3\2\2\2\u0160\u0161\7H\2\2\u0161\u0162\7n\2\2\u0162\u0163")
        buf.write("\7q\2\2\u0163\u0164\7c\2\2\u0164\u0165\7v\2\2\u0165\66")
        buf.write("\3\2\2\2\u0166\u0167\7D\2\2\u0167\u0168\7q\2\2\u0168\u0169")
        buf.write("\7q\2\2\u0169\u016a\7n\2\2\u016a\u016b\7g\2\2\u016b\u016c")
        buf.write("\7c\2\2\u016c\u016d\7p\2\2\u016d8\3\2\2\2\u016e\u016f")
        buf.write("\7U\2\2\u016f\u0170\7v\2\2\u0170\u0171\7t\2\2\u0171\u0172")
        buf.write("\7k\2\2\u0172\u0173\7p\2\2\u0173\u0174\7i\2\2\u0174:\3")
        buf.write("\2\2\2\u0175\u0176\7T\2\2\u0176\u0177\7g\2\2\u0177\u0178")
        buf.write("\7v\2\2\u0178\u0179\7w\2\2\u0179\u017a\7t\2\2\u017a\u017b")
        buf.write("\7p\2\2\u017b<\3\2\2\2\u017c\u017d\7P\2\2\u017d\u017e")
        buf.write("\7w\2\2\u017e\u017f\7n\2\2\u017f\u0180\7n\2\2\u0180>\3")
        buf.write("\2\2\2\u0181\u0182\7E\2\2\u0182\u0183\7n\2\2\u0183\u0184")
        buf.write("\7c\2\2\u0184\u0185\7u\2\2\u0185\u0186\7u\2\2\u0186@\3")
        buf.write("\2\2\2\u0187\u0188\7X\2\2\u0188\u0189\7c\2\2\u0189\u018a")
        buf.write("\7n\2\2\u018aB\3\2\2\2\u018b\u018c\7X\2\2\u018c\u018d")
        buf.write("\7c\2\2\u018d\u018e\7t\2\2\u018eD\3\2\2\2\u018f\u0190")
        buf.write("\7E\2\2\u0190\u0191\7q\2\2\u0191\u0192\7p\2\2\u0192\u0193")
        buf.write("\7u\2\2\u0193\u0194\7v\2\2\u0194\u0195\7t\2\2\u0195\u0196")
        buf.write("\7w\2\2\u0196\u0197\7e\2\2\u0197\u0198\7v\2\2\u0198\u0199")
        buf.write("\7q\2\2\u0199\u019a\7t\2\2\u019aF\3\2\2\2\u019b\u019c")
        buf.write("\7F\2\2\u019c\u019d\7g\2\2\u019d\u019e\7u\2\2\u019e\u019f")
        buf.write("\7v\2\2\u019f\u01a0\7t\2\2\u01a0\u01a1\7w\2\2\u01a1\u01a2")
        buf.write("\7e\2\2\u01a2\u01a3\7v\2\2\u01a3\u01a4\7q\2\2\u01a4\u01a5")
        buf.write("\7t\2\2\u01a5H\3\2\2\2\u01a6\u01a7\7P\2\2\u01a7\u01a8")
        buf.write("\7g\2\2\u01a8\u01a9\7y\2\2\u01a9J\3\2\2\2\u01aa\u01ab")
        buf.write("\7D\2\2\u01ab\u01ac\7{\2\2\u01acL\3\2\2\2\u01ad\u01ae")
        buf.write("\7U\2\2\u01ae\u01af\7g\2\2\u01af\u01b0\7n\2\2\u01b0\u01b1")
        buf.write("\7h\2\2\u01b1N\3\2\2\2\u01b2\u01b3\7=\2\2\u01b3P\3\2\2")
        buf.write("\2\u01b4\u01b5\7<\2\2\u01b5R\3\2\2\2\u01b6\u01b7\7.\2")
        buf.write("\2\u01b7T\3\2\2\2\u01b8\u01b9\7\60\2\2\u01b9V\3\2\2\2")
        buf.write("\u01ba\u01bb\7\60\2\2\u01bb\u01bc\7\60\2\2\u01bcX\3\2")
        buf.write("\2\2\u01bd\u01be\7*\2\2\u01beZ\3\2\2\2\u01bf\u01c0\7+")
        buf.write("\2\2\u01c0\\\3\2\2\2\u01c1\u01c2\7]\2\2\u01c2^\3\2\2\2")
        buf.write("\u01c3\u01c4\7_\2\2\u01c4`\3\2\2\2\u01c5\u01c6\7}\2\2")
        buf.write("\u01c6b\3\2\2\2\u01c7\u01c8\7\177\2\2\u01c8d\3\2\2\2\u01c9")
        buf.write("\u01ca\7-\2\2\u01caf\3\2\2\2\u01cb\u01cc\7/\2\2\u01cc")
        buf.write("h\3\2\2\2\u01cd\u01ce\7,\2\2\u01cej\3\2\2\2\u01cf\u01d0")
        buf.write("\7\61\2\2\u01d0l\3\2\2\2\u01d1\u01d2\7\'\2\2\u01d2n\3")
        buf.write("\2\2\2\u01d3\u01d4\7#\2\2\u01d4p\3\2\2\2\u01d5\u01d6\7")
        buf.write("(\2\2\u01d6\u01d7\7(\2\2\u01d7r\3\2\2\2\u01d8\u01d9\7")
        buf.write("~\2\2\u01d9\u01da\7~\2\2\u01dat\3\2\2\2\u01db\u01dc\7")
        buf.write("?\2\2\u01dc\u01dd\7?\2\2\u01ddv\3\2\2\2\u01de\u01df\7")
        buf.write("?\2\2\u01dfx\3\2\2\2\u01e0\u01e1\7#\2\2\u01e1\u01e2\7")
        buf.write("?\2\2\u01e2z\3\2\2\2\u01e3\u01e4\7>\2\2\u01e4|\3\2\2\2")
        buf.write("\u01e5\u01e6\7>\2\2\u01e6\u01e7\7?\2\2\u01e7~\3\2\2\2")
        buf.write("\u01e8\u01e9\7@\2\2\u01e9\u0080\3\2\2\2\u01ea\u01eb\7")
        buf.write("@\2\2\u01eb\u01ec\7?\2\2\u01ec\u0082\3\2\2\2\u01ed\u01ee")
        buf.write("\7?\2\2\u01ee\u01ef\7?\2\2\u01ef\u01f0\7\60\2\2\u01f0")
        buf.write("\u0084\3\2\2\2\u01f1\u01f2\7-\2\2\u01f2\u01f3\7\60\2\2")
        buf.write("\u01f3\u0086\3\2\2\2\u01f4\u01f5\7<\2\2\u01f5\u01f6\7")
        buf.write("<\2\2\u01f6\u0088\3\2\2\2\u01f7\u01fb\t\16\2\2\u01f8\u01fa")
        buf.write("\t\17\2\2\u01f9\u01f8\3\2\2\2\u01fa\u01fd\3\2\2\2\u01fb")
        buf.write("\u01f9\3\2\2\2\u01fb\u01fc\3\2\2\2\u01fc\u008a\3\2\2\2")
        buf.write("\u01fd\u01fb\3\2\2\2\u01fe\u0200\7&\2\2\u01ff\u0201\t")
        buf.write("\17\2\2\u0200\u01ff\3\2\2\2\u0201\u0202\3\2\2\2\u0202")
        buf.write("\u0200\3\2\2\2\u0202\u0203\3\2\2\2\u0203\u008c\3\2\2\2")
        buf.write("\u0204\u0205\7%\2\2\u0205\u0206\7%\2\2\u0206\u020a\3\2")
        buf.write("\2\2\u0207\u0209\5\u008fH\2\u0208\u0207\3\2\2\2\u0209")
        buf.write("\u020c\3\2\2\2\u020a\u0208\3\2\2\2\u020a\u020b\3\2\2\2")
        buf.write("\u020b\u020d\3\2\2\2\u020c\u020a\3\2\2\2\u020d\u020e\7")
        buf.write("%\2\2\u020e\u020f\7%\2\2\u020f\u0210\3\2\2\2\u0210\u0211")
        buf.write("\bG\4\2\u0211\u008e\3\2\2\2\u0212\u021a\n\20\2\2\u0213")
        buf.write("\u0215\7%\2\2\u0214\u0216\n\20\2\2\u0215\u0214\3\2\2\2")
        buf.write("\u0216\u0217\3\2\2\2\u0217\u0215\3\2\2\2\u0217\u0218\3")
        buf.write("\2\2\2\u0218\u021a\3\2\2\2\u0219\u0212\3\2\2\2\u0219\u0213")
        buf.write("\3\2\2\2\u021a\u0090\3\2\2\2\u021b\u021d\t\21\2\2\u021c")
        buf.write("\u021b\3\2\2\2\u021d\u021e\3\2\2\2\u021e\u021c\3\2\2\2")
        buf.write("\u021e\u021f\3\2\2\2\u021f\u0220\3\2\2\2\u0220\u0221\b")
        buf.write("I\4\2\u0221\u0092\3\2\2\2\u0222\u0223\13\2\2\2\u0223\u0224")
        buf.write("\bJ\5\2\u0224\u0094\3\2\2\2\u0225\u0229\7$\2\2\u0226\u0228")
        buf.write("\5\31\r\2\u0227\u0226\3\2\2\2\u0228\u022b\3\2\2\2\u0229")
        buf.write("\u0227\3\2\2\2\u0229\u022a\3\2\2\2\u022a\u022c\3\2\2\2")
        buf.write("\u022b\u0229\3\2\2\2\u022c\u022d\bK\6\2\u022d\u0096\3")
        buf.write("\2\2\2\u022e\u0232\7$\2\2\u022f\u0231\n\22\2\2\u0230\u022f")
        buf.write("\3\2\2\2\u0231\u0234\3\2\2\2\u0232\u0233\3\2\2\2\u0232")
        buf.write("\u0230\3\2\2\2\u0233\u0239\3\2\2\2\u0234\u0232\3\2\2\2")
        buf.write("\u0235\u0236\7^\2\2\u0236\u023a\n\23\2\2\u0237\u0238\7")
        buf.write(")\2\2\u0238\u023a\n\22\2\2\u0239\u0235\3\2\2\2\u0239\u0237")
        buf.write("\3\2\2\2\u023a\u023b\3\2\2\2\u023b\u023c\bL\7\2\u023c")
        buf.write("\u0098\3\2\2\2$\2\u009d\u00a4\u00a9\u00ac\u00b2\u00b7")
        buf.write("\u00ba\u00c1\u00c6\u00c9\u00d0\u00d5\u00d8\u00dc\u00df")
        buf.write("\u00e6\u00eb\u00ee\u00f4\u00f9\u00ff\u0105\u010c\u0120")
        buf.write("\u01fb\u0202\u020a\u0217\u0219\u021e\u0229\u0232\u0239")
        buf.write("\b\3\2\2\3\7\3\b\2\2\3J\4\3K\5\3L\6")
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

    grammarFileName = "D96.g4"

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
     


