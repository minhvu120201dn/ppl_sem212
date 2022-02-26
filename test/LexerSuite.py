import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
    def test_declit1(self):
        self.assertTrue(TestLexer.test("123456789","123456789,<EOF>",100))
    def test_declit2(self):
        self.assertTrue(TestLexer.test("0","0,<EOF>",101))
    def test_declit3(self):
        self.assertTrue(TestLexer.test("1_123_4567","11234567,<EOF>",102))
    def test_declit4(self):
        self.assertTrue(TestLexer.test("1_123__4567", "1123,__4567,<EOF>", 103))
    def test_octlit1(self):
        self.assertTrue(TestLexer.test("01234567", "01234567,<EOF>", 104))
    def test_octlit2(self):
        self.assertTrue(TestLexer.test("00", "00,<EOF>", 105))
    def test_octlit3(self):
        self.assertTrue(TestLexer.test("000", "00,0,<EOF>", 106))
    def test_octlit4(self):
        self.assertTrue(TestLexer.test("01_2_3_4_5_6_7", "01234567,<EOF>", 107))
    def test_octlit5(self):
        self.assertTrue(TestLexer.test("0_1_2_3_4_5_6_7", "0,_1_2_3_4_5_6_7,<EOF>", 108))
    def test_hexlit1(self):
        self.assertTrue(TestLexer.test("0xABCDEF123456789", "0xABCDEF123456789,<EOF>", 109))
    def test_hexlit2(self):
        self.assertTrue(TestLexer.test("0XABCDEF123456789", "0XABCDEF123456789,<EOF>", 110))
    def test_hexlit3(self):
        self.assertTrue(TestLexer.test("0x0", "0x0,<EOF>", 111))
    def test_hexlit4(self):
        self.assertTrue(TestLexer.test("0XCA_FE_12_34", "0XCAFE1234,<EOF>", 112))
    def test_binlit1(self):
        self.assertTrue(TestLexer.test("0b10011", "0b10011,<EOF>", 113))
    def test_binlit2(self):
        self.assertTrue(TestLexer.test("0b0", "0b0,<EOF>", 114))
    def test_binlit3(self):
        self.assertTrue(TestLexer.test("0b1_0_0_11", "0b10011,<EOF>", 115))
    def test_floatlit1(self):
        self.assertTrue(TestLexer.test("12345.23456", "12345.23456,<EOF>", 116))
    def test_floatlit2(self):
        self.assertTrue(TestLexer.test("12345.234e-10", "12345.234e-10,<EOF>", 117))
    def test_floatlit3(self):
        self.assertTrue(TestLexer.test("12345.234e-10e78", "12345.234e-10,e78,<EOF>", 118))
    def test_floatlit4(self):
        self.assertTrue(TestLexer.test("12_345_357.234e-10e78", "12345357.234e-10,e78,<EOF>", 119))
    def test_strlit1(self):
        self.assertTrue(TestLexer.test('"This is a string"', '"This is a string",<EOF>', 120))
    def test_strlit2(self):
        self.assertTrue(TestLexer.test('"\\b\\f\\r\\n\\t"', '"\\b\\f\\r\\n\\t",<EOF>', 121))
    def test_strlit3(self):
        self.assertTrue(TestLexer.test('"He asked me: \'"Where is John?\'""', '"He asked me: \'"Where is John?\'"",<EOF>', 122))
    def test_strlit4(self):
        self.assertTrue(TestLexer.test('"This is a string containing tab \\t"', '"This is a string containing tab \\t",<EOF>', 123))
    def test_arrlit1(self):
        self.assertTrue(TestLexer.test("Array(1,2,3,4,5)", "Array,(,1,,,2,,,3,,,4,,,5,),<EOF>", 124))
    def test_arrlit2(self):
        self.assertTrue(TestLexer.test("Array(Array(1,2,3), Array(4,5,6)", "Array,(,Array,(,1,,,2,,,3,),,,Array,(,4,,,5,,,6,),<EOF>", 125))
    def test_id1(self):
        self.assertTrue(TestLexer.test("identifier12345", "identifier12345,<EOF>", 126))
    def test_id2(self):
        self.assertTrue(TestLexer.test("id_with_underscore", "id_with_underscore,<EOF>", 127))
    def test_id3(self):
        self.assertTrue(TestLexer.test("____123", "____123,<EOF>", 128))
    def test_id4(self):
        self.assertTrue(TestLexer.test("_", "_,<EOF>", 129))
    def test_id5(self):
        self.assertTrue(TestLexer.test("____", "____,<EOF>", 130))
    def test_comment1(self):
        self.assertTrue(TestLexer.test("##This is a comment##", "<EOF>", 131))
    def test_comment2(self):
        self.assertTrue(TestLexer.test("##This is a comment with # inside ##", "<EOF>", 132))
    def test_comment3(self):
        self.assertTrue(TestLexer.test("##\nFirst line\nSecond line\nThird line\n##", "<EOF>", 133))
    def test_comment4(self):
        self.assertTrue(TestLexer.test("## This is an unterminated comment", "Error Token #", 134))
    def test_unclosed_string1(self):
        self.assertTrue(TestLexer.test('"This is un unclosed string', 'Unclosed String: This is un unclosed string', 135))
    def test_unclosed_string2(self):
        self.assertTrue(TestLexer.test('"abcde \'" abcd', 'Unclosed String: abcde \'" abcd', 136))
    def test_illegal_escape_str1(self):
        self.assertTrue(TestLexer.test(""" "abc\\\\\\ def" """, """Illegal Escape In String: abc\\\\\\ """, 137))
    def test_illegal_escape_str2(self):
        self.assertTrue(TestLexer.test(""" "abc'def gh" """, """Illegal Escape In String: abc'd""", 138))
    def test_illegal_escape_str3(self):
        self.assertTrue(TestLexer.test(""" "abc\\h def" """, """Illegal Escape In String: abc\\h""", 139))
    def test_boollit1(self):
        self.assertTrue(TestLexer.test("True", "True,<EOF>", 140))
    def test_boollit2(self):
        self.assertTrue(TestLexer.test("False", "False,<EOF>", 141))
    def test_expr1(self):
        self.assertTrue(TestLexer.test("1 + 2 / 3 * 4 - 5 % 6", "1,+,2,/,3,*,4,-,5,%,6,<EOF>", 142))
    def test_expr2(self):
        self.assertTrue(TestLexer.test("1 + 2 / 3 * 4 - 5 >= a * b", "1,+,2,/,3,*,4,-,5,>=,a,*,b,<EOF>", 143))
    def test_expr3(self):
        self.assertTrue(TestLexer.test("True && False == \t\t\nFalse", "True,&&,False,==,False,<EOF>", 144))
    def test_expr4(self):
        self.assertTrue(TestLexer.test(""" "Hello" +. " " +. "World" ==. "Hello World" """, """"Hello",+.," ",+.,"World",==.,"Hello World",<EOF>""", 145))
    def test_expr5(self):
        self.assertTrue(TestLexer.test("1.2 + 3.4 <= 5.6", "1.2,+,3.4,<=,5.6,<EOF>", 146))
    def test_expr6(self):
        self.assertTrue(TestLexer.test("(12345)", "(,12345,),<EOF>", 147))
    def test_expr7(self):
        self.assertTrue(TestLexer.test("(a + 124) * bc * _ * 12_3.5", "(,a,+,124,),*,bc,*,_,*,123.5,<EOF>", 148))
    def test_expr8(self):
        self.assertTrue(TestLexer.test("(!a && b) || (c && d)", "(,!,a,&&,b,),||,(,c,&&,d,),<EOF>", 149))
    def test_separator1(self):
        self.assertTrue(TestLexer.test("a,b,c", "a,,,b,,,c,<EOF>", 150))
    def test_separator2(self):
        self.assertTrue(TestLexer.test("(abc,def)", "(,abc,,,def,),<EOF>", 151))
    def test_separator3(self):
        self.assertTrue(TestLexer.test("{123} [456]", "{,123,},[,456,],<EOF>", 152))
    def test_separator4(self):
        self.assertTrue(TestLexer.test("1,2:3;4", "1,,,2,:,3,;,4,<EOF>", 153))
    def test_invalid_intlit1(self):
        self.assertTrue(TestLexer.test("0a12345", "0,a12345,<EOF>", 154))
    def test_invalid_intlit2(self):
        self.assertTrue(TestLexer.test("0b123_45", "0b1,2345,<EOF>", 155))
    def test_invalid_intlit3(self):
        self.assertTrue(TestLexer.test("078_912", "07,8912,<EOF>", 156))
    def test_invalid_intlit4(self):
        self.assertTrue(TestLexer.test("1__2345", "1,__2345,<EOF>", 157))
    def test_separator5(self):
        self.assertTrue(TestLexer.test("a = 345_678; b = 910", "a,=,345678,;,b,=,910,<EOF>", 158))
    def test_separator6(self):
        self.assertTrue(TestLexer.test("a.b", "a,.,b,<EOF>", 159))
    def test_separator7(self):
        self.assertTrue(TestLexer.test("class::method", "class,::,method,<EOF>", 160))
    def test_separator8(self):
        self.assertTrue(TestLexer.test("class1.class2.class3::method", "class1,.,class2,.,class3,::,method,<EOF>", 161))
    def test_keyword1(self):
        self.assertTrue(TestLexer.test("New instance_for_class()", "New,instance_for_class,(,),<EOF>", 162))
    def test_keyword2(self):
        self.assertTrue(TestLexer.test("Continue; Break;", "Continue,;,Break,;,<EOF>", 163))
    def test_keyword3(self):
        self.assertTrue(TestLexer.test("Constructor(ins1,ins2:Int){}", "Constructor,(,ins1,,,ins2,:,Int,),{,},<EOF>", 164))
    def test_keyword4(self):
        self.assertTrue(TestLexer.test("Destructor(){}", "Destructor,(,),{,},<EOF>", 165))
    def test_keyword5(self):
        self.assertTrue(TestLexer.test("Foreach", "Foreach,<EOF>", 166))
    def test_keyword6(self):
        self.assertTrue(TestLexer.test("Return", "Return,<EOF>", 167))
    def test_varid1(self):
        self.assertTrue(TestLexer.test("$abcde", "$abcde,<EOF>", 168))
    def test_varid2(self):
        self.assertTrue(TestLexer.test("$123", "$123,<EOF>", 169))
    def test_varid3(self):
        self.assertTrue(TestLexer.test("$___", "$___,<EOF>", 170))
    def test_varid4(self):
        self.assertTrue(TestLexer.test("$", "Error Token $", 171))
    def test_varid5(self):
        self.assertTrue(TestLexer.test("$$", "Error Token $", 172))
    def test_varid6(self):
        self.assertTrue(TestLexer.test("$var_id__ id___", "$var_id__,id___,<EOF>", 173))
    def test_keyword7(self):
        self.assertTrue(TestLexer.test("Val", "Val,<EOF>", 174))
    def test_keyword8(self):
        self.assertTrue(TestLexer.test("Var", "Var,<EOF>", 175))
    def test_keyword9(self):
        self.assertTrue(TestLexer.test("Val a, b, c, d: String;", "Val,a,,,b,,,c,,,d,:,String,;,<EOF>", 176))
    def test_keyword10(self):
        self.assertTrue(TestLexer.test("Var $a, $b, $c, $d: String;", "Var,$a,,,$b,,,$c,,,$d,:,String,;,<EOF>", 177))
    def test_keyword11(self):
        self.assertTrue(TestLexer.test("If", "If,<EOF>", 178))
    def test_keyword12(self):
        self.assertTrue(TestLexer.test("Elseif", "Elseif,<EOF>", 179))
    def test_keyword13(self):
        self.assertTrue(TestLexer.test("Else", "Else,<EOF>", 180))
    def test_keyword14(self):
        self.assertTrue(TestLexer.test("Class", "Class,<EOF>", 181))
    def test_keyword15(self):
        self.assertTrue(TestLexer.test("Class _ {method()}", "Class,_,{,method,(,),},<EOF>", 182))
    def test_comment5(self):
        self.assertTrue(TestLexer.test("func(## just a comment ##)", "func,(,),<EOF>", 183))
    def test_comment6(self):
        self.assertTrue(TestLexer.test("Class _{## just a comment ##}", "Class,_,{,},<EOF>", 184))
    def test_comment7(self):
        self.assertTrue(TestLexer.test("Array(1####,2####,3####,4####,5####)", "Array,(,1,,,2,,,3,,,4,,,5,),<EOF>", 185))
    def test_comment8(self):
        self.assertTrue(TestLexer.test("#####", "Error Token #", 186))
    def test_comment9(self):
        self.assertTrue(TestLexer.test("__id1__##comment##__id2__", "__id1__,__id2__,<EOF>", 187))
    def test_comment10(self):
        self.assertTrue(TestLexer.test("$id1__##comment##$id2__", "$id1__,$id2__,<EOF>", 188))
    def test_declit5(self):
        self.assertTrue(TestLexer.test("123_456_789_", "123456789,_,<EOF>", 189))
    def test_declit6(self):
        self.assertTrue(TestLexer.test("123_456__789_", "123456,__789_,<EOF>", 190))
    def test_declit7(self):
        self.assertTrue(TestLexer.test("0000000", "00,00,00,0,<EOF>", 191))
    def test_hexlit5(self):
        self.assertTrue(TestLexer.test("0xA_B_C_D_E_F", "0xABCDEF,<EOF>", 192))
    def test_hexlit6(self):
        self.assertTrue(TestLexer.test("0XCAFE_3456", "0XCAFE3456,<EOF>", 193))
    def test_binlit4(self):
        self.assertTrue(TestLexer.test("0b1001_0110", "0b10010110,<EOF>", 194))
    def test_binlit5(self):
        self.assertTrue(TestLexer.test("0b0_001", "0b0,_001,<EOF>", 195))
    def test_binlit6(self):
        self.assertTrue(TestLexer.test("0B1001_0110", "0B10010110,<EOF>", 196))
    def test_unclosed_string3(self):
        self.assertTrue(TestLexer.test('"abc', 'Unclosed String: abc', 197))
    def test_unclosed_string4(self):
        self.assertTrue(TestLexer.test('"', 'Error Token "', 198))
    def test_id6(self):
        self.assertTrue(TestLexer.test("__init__", "__init__,<EOF>", 199))