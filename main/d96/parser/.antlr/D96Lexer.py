# Generated from g:\sem_212\ppl\assignment1\src\main\d96\parser\D96.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2A")
        buf.write("\u0236\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\3\2")
        buf.write("\3\2\3\2\3\2\5\2\u009c\n\2\3\2\3\2\3\3\3\3\3\3\5\3\u00a3")
        buf.write("\n\3\3\3\7\3\u00a6\n\3\f\3\16\3\u00a9\13\3\5\3\u00ab\n")
        buf.write("\3\3\4\3\4\3\4\3\4\5\4\u00b1\n\4\3\4\7\4\u00b4\n\4\f\4")
        buf.write("\16\4\u00b7\13\4\5\4\u00b9\n\4\3\5\3\5\3\5\3\5\3\5\5\5")
        buf.write("\u00c0\n\5\3\5\7\5\u00c3\n\5\f\5\16\5\u00c6\13\5\5\5\u00c8")
        buf.write("\n\5\3\6\3\6\3\6\3\6\3\6\5\6\u00cf\n\6\3\6\7\6\u00d2\n")
        buf.write("\6\f\6\16\6\u00d5\13\6\5\6\u00d7\n\6\3\7\3\7\5\7\u00db")
        buf.write("\n\7\3\7\5\7\u00de\n\7\3\7\3\7\3\b\3\b\3\b\5\b\u00e5\n")
        buf.write("\b\3\b\7\b\u00e8\n\b\f\b\16\b\u00eb\13\b\5\b\u00ed\n\b")
        buf.write("\3\t\3\t\7\t\u00f1\n\t\f\t\16\t\u00f4\13\t\3\n\3\n\5\n")
        buf.write("\u00f8\n\n\3\n\3\n\3\13\3\13\5\13\u00fe\n\13\3\f\3\f\7")
        buf.write("\f\u0102\n\f\f\f\16\f\u0105\13\f\3\f\3\f\3\r\3\r\5\r\u010b")
        buf.write("\n\r\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\5\17\u011f\n")
        buf.write("\17\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\27\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30")
        buf.write("\3\30\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\33\3\33\3\33")
        buf.write("\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34")
        buf.write("\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\36")
        buf.write("\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3\37\3 \3 \3 \3 \3")
        buf.write(" \3 \3!\3!\3!\3!\3\"\3\"\3\"\3\"\3#\3#\3#\3#\3#\3#\3#")
        buf.write("\3#\3#\3#\3#\3#\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3%\3")
        buf.write("%\3%\3%\3&\3&\3&\3\'\3\'\3(\3(\3)\3)\3*\3*\3+\3+\3+\3")
        buf.write(",\3,\3-\3-\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3\62\3\62\3")
        buf.write("\63\3\63\3\64\3\64\3\65\3\65\3\66\3\66\3\67\3\67\38\3")
        buf.write("8\38\39\39\39\3:\3:\3:\3;\3;\3<\3<\3<\3=\3=\3>\3>\3>\3")
        buf.write("?\3?\3@\3@\3@\3A\3A\3A\3A\3B\3B\3B\3C\3C\3C\3D\3D\7D\u01f3")
        buf.write("\nD\fD\16D\u01f6\13D\3E\3E\6E\u01fa\nE\rE\16E\u01fb\3")
        buf.write("F\3F\3F\3F\7F\u0202\nF\fF\16F\u0205\13F\3F\3F\3F\3F\3")
        buf.write("F\3G\3G\3G\6G\u020f\nG\rG\16G\u0210\5G\u0213\nG\3H\6H")
        buf.write("\u0216\nH\rH\16H\u0217\3H\3H\3I\3I\3I\3J\3J\7J\u0221\n")
        buf.write("J\fJ\16J\u0224\13J\3J\3J\3K\3K\7K\u022a\nK\fK\16K\u022d")
        buf.write("\13K\3K\3K\3K\3K\5K\u0233\nK\3K\3K\3\u022b\2L\3\3\5\2")
        buf.write("\7\2\t\2\13\2\r\4\17\2\21\2\23\2\25\5\27\6\31\2\33\2\35")
        buf.write("\2\37\7!\b#\t%\n\'\13)\f+\r-\16/\17\61\20\63\21\65\22")
        buf.write("\67\239\24;\25=\26?\27A\30C\31E\32G\33I\34K\35M\36O\37")
        buf.write("Q S!U\"W#Y$[%]&_\'a(c)e*g+i,k-m.o/q\60s\61u\62w\63y\64")
        buf.write("{\65}\66\177\67\u00818\u00839\u0085:\u0087;\u0089<\u008b")
        buf.write("=\u008d\2\u008f>\u0091?\u0093@\u0095A\3\2\24\3\2\62;\3")
        buf.write("\2\63;\3\2\629\3\2\639\4\2ZZzz\4\2\62;CH\4\2\63;CH\4\2")
        buf.write("DDdd\3\2\62\63\4\2GGgg\4\2--//\7\2\n\f\16\17$$))^^\5\2")
        buf.write("C\\aac|\6\2\62;C\\aac|\3\2%%\5\2\13\f\17\17\"\"\3\2$$")
        buf.write("\t\2))^^ddhhppttvv\2\u0253\2\3\3\2\2\2\2\r\3\2\2\2\2\25")
        buf.write("\3\2\2\2\2\27\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2")
        buf.write("\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2")
        buf.write("\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2")
        buf.write("\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2")
        buf.write("\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3")
        buf.write("\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S")
        buf.write("\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2")
        buf.write("]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2")
        buf.write("\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2")
        buf.write("\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2")
        buf.write("\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2")
        buf.write("\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2\2\2\u0089")
        buf.write("\3\2\2\2\2\u008b\3\2\2\2\2\u008f\3\2\2\2\2\u0091\3\2\2")
        buf.write("\2\2\u0093\3\2\2\2\2\u0095\3\2\2\2\3\u009b\3\2\2\2\5\u00aa")
        buf.write("\3\2\2\2\7\u00ac\3\2\2\2\t\u00ba\3\2\2\2\13\u00c9\3\2")
        buf.write("\2\2\r\u00d8\3\2\2\2\17\u00ec\3\2\2\2\21\u00ee\3\2\2\2")
        buf.write("\23\u00f5\3\2\2\2\25\u00fd\3\2\2\2\27\u00ff\3\2\2\2\31")
        buf.write("\u010a\3\2\2\2\33\u010c\3\2\2\2\35\u011e\3\2\2\2\37\u0120")
        buf.write("\3\2\2\2!\u0126\3\2\2\2#\u012f\3\2\2\2%\u0132\3\2\2\2")
        buf.write("\'\u0139\3\2\2\2)\u013e\3\2\2\2+\u0146\3\2\2\2-\u014b")
        buf.write("\3\2\2\2/\u0151\3\2\2\2\61\u0157\3\2\2\2\63\u015a\3\2")
        buf.write("\2\2\65\u015e\3\2\2\2\67\u0164\3\2\2\29\u016c\3\2\2\2")
        buf.write(";\u0173\3\2\2\2=\u017a\3\2\2\2?\u017f\3\2\2\2A\u0185\3")
        buf.write("\2\2\2C\u0189\3\2\2\2E\u018d\3\2\2\2G\u0199\3\2\2\2I\u01a4")
        buf.write("\3\2\2\2K\u01a8\3\2\2\2M\u01ab\3\2\2\2O\u01ad\3\2\2\2")
        buf.write("Q\u01af\3\2\2\2S\u01b1\3\2\2\2U\u01b3\3\2\2\2W\u01b6\3")
        buf.write("\2\2\2Y\u01b8\3\2\2\2[\u01ba\3\2\2\2]\u01bc\3\2\2\2_\u01be")
        buf.write("\3\2\2\2a\u01c0\3\2\2\2c\u01c2\3\2\2\2e\u01c4\3\2\2\2")
        buf.write("g\u01c6\3\2\2\2i\u01c8\3\2\2\2k\u01ca\3\2\2\2m\u01cc\3")
        buf.write("\2\2\2o\u01ce\3\2\2\2q\u01d1\3\2\2\2s\u01d4\3\2\2\2u\u01d7")
        buf.write("\3\2\2\2w\u01d9\3\2\2\2y\u01dc\3\2\2\2{\u01de\3\2\2\2")
        buf.write("}\u01e1\3\2\2\2\177\u01e3\3\2\2\2\u0081\u01e6\3\2\2\2")
        buf.write("\u0083\u01ea\3\2\2\2\u0085\u01ed\3\2\2\2\u0087\u01f0\3")
        buf.write("\2\2\2\u0089\u01f7\3\2\2\2\u008b\u01fd\3\2\2\2\u008d\u0212")
        buf.write("\3\2\2\2\u008f\u0215\3\2\2\2\u0091\u021b\3\2\2\2\u0093")
        buf.write("\u021e\3\2\2\2\u0095\u0227\3\2\2\2\u0097\u009c\5\5\3\2")
        buf.write("\u0098\u009c\5\7\4\2\u0099\u009c\5\t\5\2\u009a\u009c\5")
        buf.write("\13\6\2\u009b\u0097\3\2\2\2\u009b\u0098\3\2\2\2\u009b")
        buf.write("\u0099\3\2\2\2\u009b\u009a\3\2\2\2\u009c\u009d\3\2\2\2")
        buf.write("\u009d\u009e\b\2\2\2\u009e\4\3\2\2\2\u009f\u00ab\t\2\2")
        buf.write("\2\u00a0\u00a7\t\3\2\2\u00a1\u00a3\7a\2\2\u00a2\u00a1")
        buf.write("\3\2\2\2\u00a2\u00a3\3\2\2\2\u00a3\u00a4\3\2\2\2\u00a4")
        buf.write("\u00a6\t\2\2\2\u00a5\u00a2\3\2\2\2\u00a6\u00a9\3\2\2\2")
        buf.write("\u00a7\u00a5\3\2\2\2\u00a7\u00a8\3\2\2\2\u00a8\u00ab\3")
        buf.write("\2\2\2\u00a9\u00a7\3\2\2\2\u00aa\u009f\3\2\2\2\u00aa\u00a0")
        buf.write("\3\2\2\2\u00ab\6\3\2\2\2\u00ac\u00b8\7\62\2\2\u00ad\u00b9")
        buf.write("\t\4\2\2\u00ae\u00b5\t\5\2\2\u00af\u00b1\7a\2\2\u00b0")
        buf.write("\u00af\3\2\2\2\u00b0\u00b1\3\2\2\2\u00b1\u00b2\3\2\2\2")
        buf.write("\u00b2\u00b4\t\4\2\2\u00b3\u00b0\3\2\2\2\u00b4\u00b7\3")
        buf.write("\2\2\2\u00b5\u00b3\3\2\2\2\u00b5\u00b6\3\2\2\2\u00b6\u00b9")
        buf.write("\3\2\2\2\u00b7\u00b5\3\2\2\2\u00b8\u00ad\3\2\2\2\u00b8")
        buf.write("\u00ae\3\2\2\2\u00b9\b\3\2\2\2\u00ba\u00bb\7\62\2\2\u00bb")
        buf.write("\u00c7\t\6\2\2\u00bc\u00c8\t\7\2\2\u00bd\u00c4\t\b\2\2")
        buf.write("\u00be\u00c0\7a\2\2\u00bf\u00be\3\2\2\2\u00bf\u00c0\3")
        buf.write("\2\2\2\u00c0\u00c1\3\2\2\2\u00c1\u00c3\t\7\2\2\u00c2\u00bf")
        buf.write("\3\2\2\2\u00c3\u00c6\3\2\2\2\u00c4\u00c2\3\2\2\2\u00c4")
        buf.write("\u00c5\3\2\2\2\u00c5\u00c8\3\2\2\2\u00c6\u00c4\3\2\2\2")
        buf.write("\u00c7\u00bc\3\2\2\2\u00c7\u00bd\3\2\2\2\u00c8\n\3\2\2")
        buf.write("\2\u00c9\u00ca\7\62\2\2\u00ca\u00d6\t\t\2\2\u00cb\u00d7")
        buf.write("\t\n\2\2\u00cc\u00d3\7\63\2\2\u00cd\u00cf\7a\2\2\u00ce")
        buf.write("\u00cd\3\2\2\2\u00ce\u00cf\3\2\2\2\u00cf\u00d0\3\2\2\2")
        buf.write("\u00d0\u00d2\t\n\2\2\u00d1\u00ce\3\2\2\2\u00d2\u00d5\3")
        buf.write("\2\2\2\u00d3\u00d1\3\2\2\2\u00d3\u00d4\3\2\2\2\u00d4\u00d7")
        buf.write("\3\2\2\2\u00d5\u00d3\3\2\2\2\u00d6\u00cb\3\2\2\2\u00d6")
        buf.write("\u00cc\3\2\2\2\u00d7\f\3\2\2\2\u00d8\u00da\5\17\b\2\u00d9")
        buf.write("\u00db\5\21\t\2\u00da\u00d9\3\2\2\2\u00da\u00db\3\2\2")
        buf.write("\2\u00db\u00dd\3\2\2\2\u00dc\u00de\5\23\n\2\u00dd\u00dc")
        buf.write("\3\2\2\2\u00dd\u00de\3\2\2\2\u00de\u00df\3\2\2\2\u00df")
        buf.write("\u00e0\b\7\3\2\u00e0\16\3\2\2\2\u00e1\u00ed\t\2\2\2\u00e2")
        buf.write("\u00e9\t\3\2\2\u00e3\u00e5\7a\2\2\u00e4\u00e3\3\2\2\2")
        buf.write("\u00e4\u00e5\3\2\2\2\u00e5\u00e6\3\2\2\2\u00e6\u00e8\t")
        buf.write("\2\2\2\u00e7\u00e4\3\2\2\2\u00e8\u00eb\3\2\2\2\u00e9\u00e7")
        buf.write("\3\2\2\2\u00e9\u00ea\3\2\2\2\u00ea\u00ed\3\2\2\2\u00eb")
        buf.write("\u00e9\3\2\2\2\u00ec\u00e1\3\2\2\2\u00ec\u00e2\3\2\2\2")
        buf.write("\u00ed\20\3\2\2\2\u00ee\u00f2\7\60\2\2\u00ef\u00f1\t\2")
        buf.write("\2\2\u00f0\u00ef\3\2\2\2\u00f1\u00f4\3\2\2\2\u00f2\u00f0")
        buf.write("\3\2\2\2\u00f2\u00f3\3\2\2\2\u00f3\22\3\2\2\2\u00f4\u00f2")
        buf.write("\3\2\2\2\u00f5\u00f7\t\13\2\2\u00f6\u00f8\t\f\2\2\u00f7")
        buf.write("\u00f6\3\2\2\2\u00f7\u00f8\3\2\2\2\u00f8\u00f9\3\2\2\2")
        buf.write("\u00f9\u00fa\5\17\b\2\u00fa\24\3\2\2\2\u00fb\u00fe\5+")
        buf.write("\26\2\u00fc\u00fe\5-\27\2\u00fd\u00fb\3\2\2\2\u00fd\u00fc")
        buf.write("\3\2\2\2\u00fe\26\3\2\2\2\u00ff\u0103\7$\2\2\u0100\u0102")
        buf.write("\5\31\r\2\u0101\u0100\3\2\2\2\u0102\u0105\3\2\2\2\u0103")
        buf.write("\u0101\3\2\2\2\u0103\u0104\3\2\2\2\u0104\u0106\3\2\2\2")
        buf.write("\u0105\u0103\3\2\2\2\u0106\u0107\7$\2\2\u0107\30\3\2\2")
        buf.write("\2\u0108\u010b\5\33\16\2\u0109\u010b\5\35\17\2\u010a\u0108")
        buf.write("\3\2\2\2\u010a\u0109\3\2\2\2\u010b\32\3\2\2\2\u010c\u010d")
        buf.write("\n\r\2\2\u010d\34\3\2\2\2\u010e\u010f\7^\2\2\u010f\u011f")
        buf.write("\7d\2\2\u0110\u0111\7^\2\2\u0111\u011f\7h\2\2\u0112\u0113")
        buf.write("\7^\2\2\u0113\u011f\7t\2\2\u0114\u0115\7^\2\2\u0115\u011f")
        buf.write("\7p\2\2\u0116\u0117\7^\2\2\u0117\u011f\7v\2\2\u0118\u0119")
        buf.write("\7^\2\2\u0119\u011f\7)\2\2\u011a\u011b\7^\2\2\u011b\u011f")
        buf.write("\7^\2\2\u011c\u011d\7)\2\2\u011d\u011f\7$\2\2\u011e\u010e")
        buf.write("\3\2\2\2\u011e\u0110\3\2\2\2\u011e\u0112\3\2\2\2\u011e")
        buf.write("\u0114\3\2\2\2\u011e\u0116\3\2\2\2\u011e\u0118\3\2\2\2")
        buf.write("\u011e\u011a\3\2\2\2\u011e\u011c\3\2\2\2\u011f\36\3\2")
        buf.write("\2\2\u0120\u0121\7D\2\2\u0121\u0122\7t\2\2\u0122\u0123")
        buf.write("\7g\2\2\u0123\u0124\7c\2\2\u0124\u0125\7m\2\2\u0125 \3")
        buf.write("\2\2\2\u0126\u0127\7E\2\2\u0127\u0128\7q\2\2\u0128\u0129")
        buf.write("\7p\2\2\u0129\u012a\7v\2\2\u012a\u012b\7k\2\2\u012b\u012c")
        buf.write("\7p\2\2\u012c\u012d\7w\2\2\u012d\u012e\7g\2\2\u012e\"")
        buf.write("\3\2\2\2\u012f\u0130\7K\2\2\u0130\u0131\7h\2\2\u0131$")
        buf.write("\3\2\2\2\u0132\u0133\7G\2\2\u0133\u0134\7n\2\2\u0134\u0135")
        buf.write("\7u\2\2\u0135\u0136\7g\2\2\u0136\u0137\7k\2\2\u0137\u0138")
        buf.write("\7h\2\2\u0138&\3\2\2\2\u0139\u013a\7G\2\2\u013a\u013b")
        buf.write("\7n\2\2\u013b\u013c\7u\2\2\u013c\u013d\7g\2\2\u013d(\3")
        buf.write("\2\2\2\u013e\u013f\7H\2\2\u013f\u0140\7q\2\2\u0140\u0141")
        buf.write("\7t\2\2\u0141\u0142\7g\2\2\u0142\u0143\7c\2\2\u0143\u0144")
        buf.write("\7e\2\2\u0144\u0145\7j\2\2\u0145*\3\2\2\2\u0146\u0147")
        buf.write("\7V\2\2\u0147\u0148\7t\2\2\u0148\u0149\7w\2\2\u0149\u014a")
        buf.write("\7g\2\2\u014a,\3\2\2\2\u014b\u014c\7H\2\2\u014c\u014d")
        buf.write("\7c\2\2\u014d\u014e\7n\2\2\u014e\u014f\7u\2\2\u014f\u0150")
        buf.write("\7g\2\2\u0150.\3\2\2\2\u0151\u0152\7C\2\2\u0152\u0153")
        buf.write("\7t\2\2\u0153\u0154\7t\2\2\u0154\u0155\7c\2\2\u0155\u0156")
        buf.write("\7{\2\2\u0156\60\3\2\2\2\u0157\u0158\7K\2\2\u0158\u0159")
        buf.write("\7p\2\2\u0159\62\3\2\2\2\u015a\u015b\7K\2\2\u015b\u015c")
        buf.write("\7p\2\2\u015c\u015d\7v\2\2\u015d\64\3\2\2\2\u015e\u015f")
        buf.write("\7H\2\2\u015f\u0160\7n\2\2\u0160\u0161\7q\2\2\u0161\u0162")
        buf.write("\7c\2\2\u0162\u0163\7v\2\2\u0163\66\3\2\2\2\u0164\u0165")
        buf.write("\7D\2\2\u0165\u0166\7q\2\2\u0166\u0167\7q\2\2\u0167\u0168")
        buf.write("\7n\2\2\u0168\u0169\7g\2\2\u0169\u016a\7c\2\2\u016a\u016b")
        buf.write("\7p\2\2\u016b8\3\2\2\2\u016c\u016d\7U\2\2\u016d\u016e")
        buf.write("\7v\2\2\u016e\u016f\7t\2\2\u016f\u0170\7k\2\2\u0170\u0171")
        buf.write("\7p\2\2\u0171\u0172\7i\2\2\u0172:\3\2\2\2\u0173\u0174")
        buf.write("\7T\2\2\u0174\u0175\7g\2\2\u0175\u0176\7v\2\2\u0176\u0177")
        buf.write("\7w\2\2\u0177\u0178\7t\2\2\u0178\u0179\7p\2\2\u0179<\3")
        buf.write("\2\2\2\u017a\u017b\7P\2\2\u017b\u017c\7w\2\2\u017c\u017d")
        buf.write("\7n\2\2\u017d\u017e\7n\2\2\u017e>\3\2\2\2\u017f\u0180")
        buf.write("\7E\2\2\u0180\u0181\7n\2\2\u0181\u0182\7c\2\2\u0182\u0183")
        buf.write("\7u\2\2\u0183\u0184\7u\2\2\u0184@\3\2\2\2\u0185\u0186")
        buf.write("\7X\2\2\u0186\u0187\7c\2\2\u0187\u0188\7n\2\2\u0188B\3")
        buf.write("\2\2\2\u0189\u018a\7X\2\2\u018a\u018b\7c\2\2\u018b\u018c")
        buf.write("\7t\2\2\u018cD\3\2\2\2\u018d\u018e\7E\2\2\u018e\u018f")
        buf.write("\7q\2\2\u018f\u0190\7p\2\2\u0190\u0191\7u\2\2\u0191\u0192")
        buf.write("\7v\2\2\u0192\u0193\7t\2\2\u0193\u0194\7w\2\2\u0194\u0195")
        buf.write("\7e\2\2\u0195\u0196\7v\2\2\u0196\u0197\7q\2\2\u0197\u0198")
        buf.write("\7t\2\2\u0198F\3\2\2\2\u0199\u019a\7F\2\2\u019a\u019b")
        buf.write("\7g\2\2\u019b\u019c\7u\2\2\u019c\u019d\7v\2\2\u019d\u019e")
        buf.write("\7t\2\2\u019e\u019f\7w\2\2\u019f\u01a0\7e\2\2\u01a0\u01a1")
        buf.write("\7v\2\2\u01a1\u01a2\7q\2\2\u01a2\u01a3\7t\2\2\u01a3H\3")
        buf.write("\2\2\2\u01a4\u01a5\7P\2\2\u01a5\u01a6\7g\2\2\u01a6\u01a7")
        buf.write("\7y\2\2\u01a7J\3\2\2\2\u01a8\u01a9\7D\2\2\u01a9\u01aa")
        buf.write("\7{\2\2\u01aaL\3\2\2\2\u01ab\u01ac\7=\2\2\u01acN\3\2\2")
        buf.write("\2\u01ad\u01ae\7<\2\2\u01aeP\3\2\2\2\u01af\u01b0\7.\2")
        buf.write("\2\u01b0R\3\2\2\2\u01b1\u01b2\7\60\2\2\u01b2T\3\2\2\2")
        buf.write("\u01b3\u01b4\7\60\2\2\u01b4\u01b5\7\60\2\2\u01b5V\3\2")
        buf.write("\2\2\u01b6\u01b7\7*\2\2\u01b7X\3\2\2\2\u01b8\u01b9\7+")
        buf.write("\2\2\u01b9Z\3\2\2\2\u01ba\u01bb\7]\2\2\u01bb\\\3\2\2\2")
        buf.write("\u01bc\u01bd\7_\2\2\u01bd^\3\2\2\2\u01be\u01bf\7}\2\2")
        buf.write("\u01bf`\3\2\2\2\u01c0\u01c1\7\177\2\2\u01c1b\3\2\2\2\u01c2")
        buf.write("\u01c3\7-\2\2\u01c3d\3\2\2\2\u01c4\u01c5\7/\2\2\u01c5")
        buf.write("f\3\2\2\2\u01c6\u01c7\7,\2\2\u01c7h\3\2\2\2\u01c8\u01c9")
        buf.write("\7\61\2\2\u01c9j\3\2\2\2\u01ca\u01cb\7\'\2\2\u01cbl\3")
        buf.write("\2\2\2\u01cc\u01cd\7#\2\2\u01cdn\3\2\2\2\u01ce\u01cf\7")
        buf.write("(\2\2\u01cf\u01d0\7(\2\2\u01d0p\3\2\2\2\u01d1\u01d2\7")
        buf.write("~\2\2\u01d2\u01d3\7~\2\2\u01d3r\3\2\2\2\u01d4\u01d5\7")
        buf.write("?\2\2\u01d5\u01d6\7?\2\2\u01d6t\3\2\2\2\u01d7\u01d8\7")
        buf.write("?\2\2\u01d8v\3\2\2\2\u01d9\u01da\7#\2\2\u01da\u01db\7")
        buf.write("?\2\2\u01dbx\3\2\2\2\u01dc\u01dd\7>\2\2\u01ddz\3\2\2\2")
        buf.write("\u01de\u01df\7>\2\2\u01df\u01e0\7?\2\2\u01e0|\3\2\2\2")
        buf.write("\u01e1\u01e2\7@\2\2\u01e2~\3\2\2\2\u01e3\u01e4\7@\2\2")
        buf.write("\u01e4\u01e5\7?\2\2\u01e5\u0080\3\2\2\2\u01e6\u01e7\7")
        buf.write("?\2\2\u01e7\u01e8\7?\2\2\u01e8\u01e9\7\60\2\2\u01e9\u0082")
        buf.write("\3\2\2\2\u01ea\u01eb\7-\2\2\u01eb\u01ec\7\60\2\2\u01ec")
        buf.write("\u0084\3\2\2\2\u01ed\u01ee\7<\2\2\u01ee\u01ef\7<\2\2\u01ef")
        buf.write("\u0086\3\2\2\2\u01f0\u01f4\t\16\2\2\u01f1\u01f3\t\17\2")
        buf.write("\2\u01f2\u01f1\3\2\2\2\u01f3\u01f6\3\2\2\2\u01f4\u01f2")
        buf.write("\3\2\2\2\u01f4\u01f5\3\2\2\2\u01f5\u0088\3\2\2\2\u01f6")
        buf.write("\u01f4\3\2\2\2\u01f7\u01f9\7&\2\2\u01f8\u01fa\t\17\2\2")
        buf.write("\u01f9\u01f8\3\2\2\2\u01fa\u01fb\3\2\2\2\u01fb\u01f9\3")
        buf.write("\2\2\2\u01fb\u01fc\3\2\2\2\u01fc\u008a\3\2\2\2\u01fd\u01fe")
        buf.write("\7%\2\2\u01fe\u01ff\7%\2\2\u01ff\u0203\3\2\2\2\u0200\u0202")
        buf.write("\5\u008dG\2\u0201\u0200\3\2\2\2\u0202\u0205\3\2\2\2\u0203")
        buf.write("\u0201\3\2\2\2\u0203\u0204\3\2\2\2\u0204\u0206\3\2\2\2")
        buf.write("\u0205\u0203\3\2\2\2\u0206\u0207\7%\2\2\u0207\u0208\7")
        buf.write("%\2\2\u0208\u0209\3\2\2\2\u0209\u020a\bF\4\2\u020a\u008c")
        buf.write("\3\2\2\2\u020b\u0213\n\20\2\2\u020c\u020e\7%\2\2\u020d")
        buf.write("\u020f\n\20\2\2\u020e\u020d\3\2\2\2\u020f\u0210\3\2\2")
        buf.write("\2\u0210\u020e\3\2\2\2\u0210\u0211\3\2\2\2\u0211\u0213")
        buf.write("\3\2\2\2\u0212\u020b\3\2\2\2\u0212\u020c\3\2\2\2\u0213")
        buf.write("\u008e\3\2\2\2\u0214\u0216\t\21\2\2\u0215\u0214\3\2\2")
        buf.write("\2\u0216\u0217\3\2\2\2\u0217\u0215\3\2\2\2\u0217\u0218")
        buf.write("\3\2\2\2\u0218\u0219\3\2\2\2\u0219\u021a\bH\4\2\u021a")
        buf.write("\u0090\3\2\2\2\u021b\u021c\13\2\2\2\u021c\u021d\bI\5\2")
        buf.write("\u021d\u0092\3\2\2\2\u021e\u0222\7$\2\2\u021f\u0221\5")
        buf.write("\31\r\2\u0220\u021f\3\2\2\2\u0221\u0224\3\2\2\2\u0222")
        buf.write("\u0220\3\2\2\2\u0222\u0223\3\2\2\2\u0223\u0225\3\2\2\2")
        buf.write("\u0224\u0222\3\2\2\2\u0225\u0226\bJ\6\2\u0226\u0094\3")
        buf.write("\2\2\2\u0227\u022b\7$\2\2\u0228\u022a\n\22\2\2\u0229\u0228")
        buf.write("\3\2\2\2\u022a\u022d\3\2\2\2\u022b\u022c\3\2\2\2\u022b")
        buf.write("\u0229\3\2\2\2\u022c\u0232\3\2\2\2\u022d\u022b\3\2\2\2")
        buf.write("\u022e\u022f\7^\2\2\u022f\u0233\n\23\2\2\u0230\u0231\7")
        buf.write(")\2\2\u0231\u0233\n\22\2\2\u0232\u022e\3\2\2\2\u0232\u0230")
        buf.write("\3\2\2\2\u0233\u0234\3\2\2\2\u0234\u0235\bK\7\2\u0235")
        buf.write("\u0096\3\2\2\2$\2\u009b\u00a2\u00a7\u00aa\u00b0\u00b5")
        buf.write("\u00b8\u00bf\u00c4\u00c7\u00ce\u00d3\u00d6\u00da\u00dd")
        buf.write("\u00e4\u00e9\u00ec\u00f2\u00f7\u00fd\u0103\u010a\u011e")
        buf.write("\u01f4\u01fb\u0203\u0210\u0212\u0217\u0222\u022b\u0232")
        buf.write("\b\3\2\2\3\7\3\b\2\2\3I\4\3J\5\3K\6")
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
    SEMI = 28
    COLON = 29
    COMMA = 30
    DOT = 31
    DOUBLEDOT = 32
    LB = 33
    RB = 34
    LSB = 35
    RSB = 36
    LCB = 37
    RCB = 38
    ADDOP = 39
    SUBOP = 40
    MULOP = 41
    DIVOP = 42
    MODOP = 43
    NOTOP = 44
    ANDOP = 45
    OROP = 46
    EQCMP = 47
    ASNOP = 48
    DIFCMP = 49
    LESCMP = 50
    LEQCMP = 51
    GRECMP = 52
    GEQCMP = 53
    SEQCMP = 54
    SADDOP = 55
    CSMEM = 56
    ID = 57
    VID = 58
    COMMENT = 59
    WS = 60
    ERROR_CHAR = 61
    UNCLOSE_STRING = 62
    ILLEGAL_ESCAPE = 63

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'Break'", "'Continue'", "'If'", "'Elseif'", "'Else'", "'Foreach'", 
            "'True'", "'False'", "'Array'", "'In'", "'Int'", "'Float'", 
            "'Boolean'", "'String'", "'Return'", "'Null'", "'Class'", "'Val'", 
            "'Var'", "'Constructor'", "'Destructor'", "'New'", "'By'", "';'", 
            "':'", "','", "'.'", "'..'", "'('", "')'", "'['", "']'", "'{'", 
            "'}'", "'+'", "'-'", "'*'", "'/'", "'%'", "'!'", "'&&'", "'||'", 
            "'=='", "'='", "'!='", "'<'", "'<='", "'>'", "'>='", "'==.'", 
            "'+.'", "'::'" ]

    symbolicNames = [ "<INVALID>",
            "INTLIT", "FLOATLIT", "BOOLLIT", "STRLIT", "BREAK_", "CONTINUE_", 
            "IF_", "ELSEIF_", "ELSE_", "FOREACH_", "TRUE_", "FALSE_", "ARRAY_", 
            "IN_", "INT_", "FLOAT_", "BOOL_", "STR_", "RETURN_", "NULL_", 
            "CLASS_", "VAL_", "VAR_", "CONSTRUCTOR_", "DESTRUCTOR_", "NEW_", 
            "BY_", "SEMI", "COLON", "COMMA", "DOT", "DOUBLEDOT", "LB", "RB", 
            "LSB", "RSB", "LCB", "RCB", "ADDOP", "SUBOP", "MULOP", "DIVOP", 
            "MODOP", "NOTOP", "ANDOP", "OROP", "EQCMP", "ASNOP", "DIFCMP", 
            "LESCMP", "LEQCMP", "GRECMP", "GEQCMP", "SEQCMP", "SADDOP", 
            "CSMEM", "ID", "VID", "COMMENT", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE" ]

    ruleNames = [ "INTLIT", "DECLIT", "OCTLIT", "HEXLIT", "BINLIT", "FLOATLIT", 
                  "INT_PART", "DEC_PART", "EXP_PART", "BOOLLIT", "STRLIT", 
                  "STR_CHAR", "REGULAR_CHAR", "SPECIAL_CHAR", "BREAK_", 
                  "CONTINUE_", "IF_", "ELSEIF_", "ELSE_", "FOREACH_", "TRUE_", 
                  "FALSE_", "ARRAY_", "IN_", "INT_", "FLOAT_", "BOOL_", 
                  "STR_", "RETURN_", "NULL_", "CLASS_", "VAL_", "VAR_", 
                  "CONSTRUCTOR_", "DESTRUCTOR_", "NEW_", "BY_", "SEMI", 
                  "COLON", "COMMA", "DOT", "DOUBLEDOT", "LB", "RB", "LSB", 
                  "RSB", "LCB", "RCB", "ADDOP", "SUBOP", "MULOP", "DIVOP", 
                  "MODOP", "NOTOP", "ANDOP", "OROP", "EQCMP", "ASNOP", "DIFCMP", 
                  "LESCMP", "LEQCMP", "GRECMP", "GEQCMP", "SEQCMP", "SADDOP", 
                  "CSMEM", "ID", "VID", "COMMENT", "CMT_CHAR", "WS", "ERROR_CHAR", 
                  "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

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
            actions[71] = self.ERROR_CHAR_action 
            actions[72] = self.UNCLOSE_STRING_action 
            actions[73] = self.ILLEGAL_ESCAPE_action 
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
     


