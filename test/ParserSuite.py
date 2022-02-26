import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_simple_program1(self):
        input = """Class Program {}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,200))

    def test_simple_program2(self):
        input = """Class Program { main() {} }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,201))

    def test_simple_program3(self):
        input = """Class Program { func1(){} $func2(){} }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,202))

    def test_simple_program4(self):
        input = """Class class1 { func1(){} func2(){} }
                   Class class2 { Constructor(){} Constructor(a,b,c:String){} Destructor(){} }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,203))

    def test_simple_program5(self):
        input = """Class 123 {}"""
        expect = "Error on line 1 col 6: 123"
        self.assertTrue(TestParser.test(input,expect,204))

    def test_simple_program6(self):
        input = """Class empty_class {}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,205))

    def test_simple_program7(self):
        input = """Class _ { _(){} Constructor(){} Destructor(a:Int){} }"""
        expect = "Error on line 1 col 43: a"
        self.assertTrue(TestParser.test(input,expect,206))

    def test_simple_program8(self):
        input = """Class $wrong_id { main() }"""
        expect = "Error on line 1 col 6: $wrong_id"
        self.assertTrue(TestParser.test(input,expect,207))

    def test_simple_program9(self):
        input = """Class _ { func() {}"""
        expect = "Error on line 1 col 19: <EOF>"
        self.assertTrue(TestParser.test(input,expect,208))

    def test_simple_program10(self):
        input = """Class { func(Var $abc: Int) {} }"""
        expect = "Error on line 1 col 6: {"
        self.assertTrue(TestParser.test(input,expect,209))

    def test_program_with_comment1(self):
        input = """Class ##This is a comment## _ {}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,210))

    def test_program_with_comment2(self):
        input = """##This program was written by me##
Class _ { ##There is nothing here##
    Var $attr1: String = "hello world"; ## String var attributes ##
    Var $attr2, $attr3: Boolean = True, True && False; ## Boolean var attributes ##
    func() {
        Val new_value : Int = 10 + 90; ## Declare a temporary value ##
    }
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,211))

    def test_program_with_comment3(self):
        input = """##Class Program## {$main(){Return 1;}}"""
        expect = "Error on line 1 col 18: {"
        self.assertTrue(TestParser.test(input,expect,212))

    def test_scopes1(self):
        input = """Class Program {
    func() {
        Val const: String = "a string";
        {
            Var $temp : Int = 1;
            Var $temp2, $a, $b : Boolean = True, False, !True;
            { ## Scope in scope ##
                Val pi: Float = 3.14;            
            }
        }
    }
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,213))

    def test_scopes2(self):
        input = """Class Program {
    func() {
        {}
        {}{{}}
        { ## This scope needs to be closed ##
    }
}"""
        expect = "Error on line 7 col 1: <EOF>"
        self.assertTrue(TestParser.test(input,expect,214))

    def test_decl1(self):
        input = """Class Program {
    Var $a, $b, $c; ## Declare without type specification ##
    func() {}
}"""
        expect = "Error on line 2 col 18: ;"
        self.assertTrue(TestParser.test(input,expect,215))

    def test_decl2(self):
        input = """Class Program {
    Var $abc, $variable, value: String = "var1", "var2", "val3";
    func() {}
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,216))

    def test_decl3(self):
        input = """Class Program {
    Val abc, value, variable: String = "val1", "val2", "var3";
    func() {}
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,217))

    def test_decl4(self):
        input = """Class Program {
    Var a, b, c: Int;
    Var $a, $b, $c: String;
    func() {}
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,218))

    def test_decl5(self):
        input = """Class Program {
    Val a, b, c: Int = 1 + 2, 2 + 3, a + b;
    Var $a, $b, $c: String = "hello" +. " " +. "world", "string" +. " second", "string" +. " third";
    Val temp1, temp2: Boolean = True, False;
    func() {
        Var $ABCDE: Boolean = (True && False) || (True || False) || !(temp1 && !temp2);
    }
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,219))

    def test_ifelse1(self):
        input = """Class Program {
    Var $abc, $def: Int;
    Val temp1, temp2: Boolean = True, False;
    main() {
        If (temp1 || temp2) { $abc = 10; }
        Return 10;
    }
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,220))

    def test_ifelse2(self):
        input = """Class Program {
    Var $abc, $def: Int;
    Val temp1, temp2: Boolean = True, False;
    main() {
        If (temp1 || temp2) { $abc = 10; }
        Elseif (temp1) { Return temp2; }
        Elseif (temp2) { Return temp1; }
        Else {
            If (1 + 2 == 3) { Return "This is obvious"; } 
            Elseif (1 + 2 == 4) { Return "This can never happen!"; }
            Else { Return 10; }
        }
    }
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,221))

    def test_ifelse3(self):
        input = """Class Program {
    main() {
        If ("I do not like your voice" ==. "I like your voice") {
            Return "This doesn\\'t make any sense!";
        }
        Elseif ("This is just a string") {
            Return "This return statement will never run";
        }
    }
}"""
        expect = "Error on line 6 col 39: )"
        self.assertTrue(TestParser.test(input,expect,222))

    def test_ifelse4(self):
        input = """Class Program {
    main() {
        Elseif (True) { Return "Do nothing"; }
    }
}"""
        expect = "Error on line 3 col 8: Elseif"
        self.assertTrue(TestParser.test(input,expect,223))

    def test_ifelse5(self):
        input = """Class Program {
    main() {
        If (True) { Return 1; }
        Elseif (1 + 2 == 3) { Return -1; }
        Else { Return 2; }
    }
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,224))

    def test_array1(self):
        input = """Class Program {
    Var arr: Array[Int,5];
    Var $arr: Array[String,5];
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,225))

    def test_array2(self):
        input = """Class Program {
    Val arr: Array[Int,5] = Array(1,2,3,4,5);
    Var $arr: Array[String,5] = Array("str1","str2","str3","str4","str5");
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,226))

    def test_array3(self):
        input = """Class Program {
    Val arr: Array[Int,5] = Array(1,2,3,4,5);
    Var $arr: Array[String,5] = Array("str1","str2","str3","str4","str5");
    Val temp_str: String = "Temporary string";
    main() {
        $arr[1] = "element 1 ";
        $arr[2] = "element 2 ";
        $arr[3] = "element 3 ";
        $arr[4] = $arr[1] +. $arr[2] +. "another string";
        $arr[5] = Self.temp_str;
    }
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,227))

    def test_instance1(self):
        input = """## This line does not contain anything ##
Class tempClass {
    Var immutable: String = "immutable attribute";
    Var $mutable: String = "mutable attribute";

    Constructor() {}
    Destructor() {}
}
Class Program {
    Var instance: tempClass = New tempClass();
    main() {
        instance.immutable = "another string";
        instance.immutable = tempClass::$mutable;
    }
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,228))

    def test_instance2(self):
        input = """## This line does not contain anything ##
Class tempClass {
    Var immutable: String = "immutable attribute";
    Var $mutable: String = "mutable attribute";

    Constructor() {}
    Destructor() {}
}
Class Program {
    Var instance: tempClass = New tempClass();
    main() {
        tempClass.$mutable = "unavailable assignment statement";
    }
}"""
        expect = "Error on line 12 col 18: $mutable"
        self.assertTrue(TestParser.test(input,expect,229))

#     def test_instance3(self):
#         input = """## This line does not contain anything ##
# Class tempClass {
#     Var immutable: String = "immutable attribute";

#     Constructor() {}
#     immutableFunc() { immutable = "immutable"; Return "immutable function"; }
#     $mutableFunc() { Return "mutable function"; }
#     Destructor() {}
# }
# Class Program {
#     Var instance: tempClass = New tempClass();
#     main() {
#         instance.immutable = instance.immutableFunc();
#         instance.immutable = tempClass::$mutableFunc();
#         Var tempStr: String = "hello world";
#         tempStr = instance.immutable = instance.immutableFunc();
#     }
# }"""
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,230))

    def test_instance4(self):
        input = """## This line does not contain anything ##
Class tempClass {
    Var immutable: String = "immutable attribute";

    Constructor() {}
    Constructor(actualStr: String) { immutable = actualStr +. "hello"; }
    immutableFunc() { immutable = "immutable"; Return "immutable function"; }
    $mutableFunc() { Return "mutable function"; }
    Destructor() {}
}
Class Program {
    Var instance: tempClass = New tempClass();
    main() {
        tempClass::$mutableFunc();
        instance.immutableFunc();
        Var instance2: tempClass = New tempClass("let\\'s change things \'\"a little bit\'\"");
        instance2 = instance.immutableFunc();
    }
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,231))

    def test_array4(self):
        input = """Class Program {
    Var arr: Array[Array[Int,5],5];
    main() {}
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,232))

    def test_array5(self):
        input = """Class Program {
    Var arr: Array[String,100.5];
    main() {}
}"""
        expect = "Error on line 2 col 26: 100.5"
        self.assertTrue(TestParser.test(input,expect,233))

    def test_array6(self):
        input = """Class Program {
    Var arr: Array[Array[Int,5],5] = Array(Array(1,2,3,4,5),Array(1,2,3,4,5),Array(1,2,3,4,5),Array(1,2,3,4,5),Array(1,2,3,4,5));
    main() {}
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,234))

    def test_array7(self):
        input = """Class Program {
    Var arr: Array[Array[Int,5],5] = Array(Array(1,2,3,4,5),Array(1,2,3,4,5),Array(1,2,3,4,5),Array(1,2,3,4,5),Array(1,2,3,4,5));
    main() {
        arr[1][1] = arr[2][2] + arr[3][3];
        arr[1] = Array(4,5,6,7,8);
    }
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,235))

#     def test_array8(self):
#         input = """Class Program {
#     Var arr: Array[Int,5] = Array(1,2,3,4,"expected an integer, got a string instead");
#     main() {
#         Return "Expected an error";
#     }
# }"""
#         expect = "Error on line 2 col 42: \"expected an integer, got a string instead\""
#         self.assertTrue(TestParser.test(input,expect,236))

    def test_instance5(self):
        input = """## This line does not contain anything ##
Class tempClass {
    Var immutable: String = "immutable attribute";

    Constructor() {}
    Constructor(actualStr: String) { immutable = actualStr; }
    immutableFunc() { immutable = "immutable"; Return "immutable function"; }
    $mutableFunc(a:String) { Return "mutable function"; }
    Destructor() {}
}
Class Program {
    main() {
        New tempClass("hello world").immutableFunc();
        Var str: String = New tempClass("hello world").immutable;
        Var str2: String = New tempClass("hello world").immutableFunc();
        tempClass::$mutableFunc("hello");
    }
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,237))

    def test_function1(self):
        input = """Class Program {
    func(a,b,c:Int; d:String; e:Boolean) { Return 0; }
    main() {
        Val num : Int = func(1,2,3,"hello",True);
        Var var : Int = num + 12345;
    }
}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,238))

    def test_function2(self):
        input = """## This line does not contain anything ##
Class _ {
    Constructor() {}
    $func() { Return 0; }
    func(a,b,c:Int) { Return "null"; }    
}
Class Program {
    main() {
        Var ins : _ = New _();
        ins.func(_::$func(), _::$func(), (_::$func()+1)*2);
    }
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,239))

    def test_instance6(self):
        input = """## This line does not contain anything ##
Class tempClass {
    Constructor() {}
}
Class Program {
    main() {
        Var ins1 : tempClass = Null;
        Var ins2 : tempClass = New tempClass();
    }
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,240))

    def test_loop1(self):
        input = """Class Program {
    main() {
        Foreach(i In 1 .. 100) {}
    }
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,241))

    def test_loop2(self):
        input = """Class Program {
    main() {
        Var sum: Int = 0;
        Foreach(i In 1 .. 100) {
            sum = sum + i;
            Foreach(j In 1 .. 100 By 1000) { sum = sum + j; }
            If (sum >= 1000) { Break; }
            Elseif (sum <= 500) { Continue; }
        }
    }
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,242))

    def test_loop3(self):
        input = """Class Program {
    main() {
        Continue; ## Continue statement cannot be put here. ##
    }
}"""
        expect = "Error on line 3 col 8: Continue"
        self.assertTrue(TestParser.test(input,expect,243))

    def test_loop4(self):
        input = """Class Program {
    main() {
        Break; ## Break statement cannot be put here. ##
    }
}"""
        expect = "Error on line 3 col 8: Break"
        self.assertTrue(TestParser.test(input,expect,244))

    def test_loop5(self):
        input = """Class Program {
    main() {
        Foreach(i In 1 .. 1000 By 100) Continue;
    }
}"""
        expect = "Error on line 3 col 39: Continue"
        self.assertTrue(TestParser.test(input,expect,245))

    def test_loop6(self):
        input = """Class Program {
    main() {
        Foreach(i In 0 .. 1 By 0) {
            If ("hello" +. " " +. "world" ==. "hello world") { Break; }
            Else { Return "There can\\'t be any other way"; }
        }
        Return 0;
    }
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,246))

    def test_loop7(self):
        input = """Class Program {
    main() {
        Foreach(i In 0 .. (100 % 1_0_0_0) By 10 / 5) {}
        Return 0;
    }
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,247))

    def test_loop8(self):
        input = """Class Program {
    main() {
        Foreach(i In 0 .. 100.2 By 3) {}
        Return 0;
    }
}"""
        expect = "Error on line 3 col 26: 100.2"
        self.assertTrue(TestParser.test(input,expect,248))

    def test_loop9(self):
        input = """Class Program {
    main() {
        Foreach(i In 0b1111 .. 0xCAFE_1234 By 01) {}
        Return 0;
    }
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,249))

    def test_function3(self):
        input = """Class Program {
    func(a,b,c,d,e:String) {}
    main() {
        func("1","2","3","4","5"
    }
}"""
        expect = "Error on line 5 col 4: }"
        self.assertTrue(TestParser.test(input,expect,250))

    def test_expression1(self):
        input = """Class Program {
    Var a, b: Int = (1 + 2) * 0x3, a % 1000;
    Var c: Float = 1000 * 5;
    Var d: String = "legal string" +. "legal operation";
    Var e, f: Boolean = True, False;
    main() {}
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,251))

    def test_expression2(self):
        input = """Class Program {
    Var a, b: Float = (1 + 2) * 3, 1000;
    main() {}
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,252))

    def test_expression3(self):
        input = """Class Program {
    Var a, b: Float = (1 + 2) * 3, a % 1000;
    main() {}
}"""
        expect = "Error on line 2 col 37: %"
        self.assertTrue(TestParser.test(input,expect,253))

    def test_expression4(self):
        input = """Class Program {
    Val wrong_formula, right_formula: Boolean = 1 + 2 >= 3 + 4, "hello " +. "world" ==. "hello world";
    main() {}
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,254))

    def test_expression5(self):
        input = """Class Program {
    Val wrong_formula, right_formula: Boolean = 1 + 2 >= 3 + 4, "hello " +. "world" ==. "hello world";
    main() {
        If (!wrong_formula || !(1 + 2 == 3)) { Return True; }
        Else { Return "This case can never happen!!!"; }
    }
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,255))

    def test_expression6(self):
        input = """Class Program {
    Var illegalStr: String = "Hello" + "World";
    main() {}
}"""
        expect = "Error on line 2 col 37: +"
        self.assertTrue(TestParser.test(input,expect,256))

    def test_expression7(self):
        input = """Class Program {
    Val val1, val2: String = "first string", "second string";
    Var illegalStr: String = val1 + val2;
    main() {}
}"""
        expect = "Error on line 3 col 34: +"
        self.assertTrue(TestParser.test(input,expect,257))

    def test_expression8(self):
        input = """Class Program {
    Val val1, val2: Int = 1, 2;
    Var wrongExpression: Boolean = val1 + val2;
    main() {}
}"""
        expect = "Error on line 3 col 46: ;"
        self.assertTrue(TestParser.test(input,expect,258))

    def test_expression9(self):
        input = """## This line does not contain anything ##
Class tempClass {
    Constructor(){}
}
Class Program {
    Var instance: tempClass = "Wrong string expression";
    main() {}
}"""
        expect = "Error on line 6 col 30: \"Wrong string expression\""
        self.assertTrue(TestParser.test(input,expect,259))

    def test_expression10(self):
        input = """Class Program {
    Var attribute_of_type_int: Int = Null;
    main() {}
}"""
        expect = "Error on line 2 col 41: ;"
        self.assertTrue(TestParser.test(input,expect,260))

    def test_expression11(self):
        input = """Class Program {
    Var arr: Array[Int,5] = Array(0,1,2,3,4);
    Var a,b,c: Int = arr[1], arr[2], arr[3] * arr[4] % arr[5];
    main() {}
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,261))

    def test_expression12(self):
        input = """Class Program {
    Var arr: Array[String,5] = Array("str0","str1","str2","str3","str4");
    Var a,b,c: String = arr[1], arr[2], arr[3] +. arr[4] +. arr[5];
    main() {}
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,262))

    def test_complex_program1(self):
        input = """## This line does not contain anything ##
Class _ {
    $fact(n:Int) {
        If (n < 0) { Return "Type error"; }
        Else {
            If (n == 0) { Return 1; }
            Else { Return $face(n-1) * n; }
        }
    }
}
Class Program {
    main() {}
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,263))

    def test_complex_program2(self):
        input = """## This line does not contain anything ##
Class _ {
    $fact(n:Int) {
        If (n < 0) { Return "Type error"; }
        Else {
            If (n == 0) { Return 1; }
            Else { Return $face(n-1) * n; }
        }
    }
    $P(n,k:Int) {
        Return $fact(n) / $fact(k);
    }
    $C(n,k:Int) {
        Return $fact(n) / ($fact(k) * $fact(n-k));
    }
}

Class Program {
    main() {
        If (_::$fact(0) != 1) { Return; }
        Elseif (_::$P(1,0) != 1) { Return; }
        Return;
    }
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,264))

    def test_complex_program3(self):
        input = """## This line does not contain anything##
Class Shape {
    Var area: Float;
}
Class Rectangle : Shape {
    Var height, width: Float;
    Constructor(h,w:Int) {
        Self.height = h;
        Self.width = w;
        Self.area = h * w;
    }
    Destructor() {}
}
Class Program {
    main() {
        Val rect: Rectangle = New Rectangle(10,20);
        Val myarea1: Float = rect.area;
        Val myarea2: Float = New Rectangle(100,200).area;
        Val myarea3: Float = Null.area;
        Return;
    }
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,265))

#     def test_complex_program4(self):
#         input = """## This line does not contain anything##
# Class Program {
#     Var var1, var2, $var3: String = "variable 1", "variable 2", "variable 3";    
#     Val $val1, $val2, val3: String = "constant 1", "constant 2", "constant 3";
#     main() {
#         Val not_global_value: String = "hehehe";
#         Var not_global_variable: String;
#         not_global_variable = var1 = var2 = $var3 = $val1;
#         Return;
#     }
# }"""
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,266))

    def test_complex_program5(self):
        input = """## This line does not contain anything##
Class Program {
    Val val1, val2: Int = 5, 0x123_456_ABC_DEF;
    main() {
        Return;
        Return;
        If (5 == 1 || 4 == 2) { Return; }
    }
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,267))

    def test_complex_program6(self):
        input = """## This line does not contain anything##
Class Program {
    Val val1, val2: Int = 5, 0x123_456_ABC_DEF;
    main() {
        Var sum: Int = 0;
        Val expected_sum: Int = 1_000_000_000;
        Foreach (i In 1 .. val2 By val1) {
            If (sum == expected_sum) { Return; }
            Else { sum = sum + i; }
        }
    }
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,268))

    def test_complex_program7(self):
        input = """## This line does not contain anything##
Class Program {
    Val val1, val2: Int = 5, 0x123_456_ABC_DEF;
    main() {
        Var sum: Int = 0;
        Val expected_sum: Int = 1_000_000_000;
        Var announcement: String = "";
        Foreach (i In 1 .. val2 + val1 By val1) {
            If (sum == expected_sum) { Return; }
            Else { sum = sum + 1; }
            announcement = announcement +. "This is not the end yet\\n";
            Continue;
        }
    }
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,269))

    def test_complex_program8(self):
        input = """## This line does not contain anything##
Class class1 {}
Class class2 : class1 {}
Class class3 : class2 {}
Class class4 : class3 { func(){} }
Class Program {
    main() {
        Var ins3: class3 = New class3();
        Var ins4: class4 = Null;
    }
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,270))

    def test_complex_program9(self):
        input = """## This line does not contain anything##
Class _ {
    Val $static_attribute: String = "static attribute";
}
Class Program {
    main() {
        _::$static_attribute = "non-static attribute";
        Return;
    }
}"""
        expect = "Error on line 7 col 29: ="
        self.assertTrue(TestParser.test(input,expect,271))

    def test_complex_program10(self):
        input = """## This line does not contain anything##
Class _ {
    $staticFunc() { Return "static function"; }
}
Class Program {
    main() {
        Val str1: String = _::$staticFunc();
        Val str2: String = _.$staticFunc();
        Return;
    }
}"""
        expect = "Error on line 8 col 29: $staticFunc"
        self.assertTrue(TestParser.test(input,expect,272))

    def test_complex_program11(self):
        input = """Class Program {
    main() {
        Var x1, x2, x3, x4: Int = 1,2,3;
        Return;
    }
}"""
        expect = "Error on line 3 col 39: ;"
        self.assertTrue(TestParser.test(input,expect,273))

    def test_complex_program12(self):
        input = """Class big_class {
    Class class_in_class {
        func() {
            Return "This class is not legal!!!";
        }
    }
}"""
        expect = "Error on line 2 col 4: Class"
        self.assertTrue(TestParser.test(input,expect,274))

    def test_complex_program13(self):
        input = """Class Program {
    main() {
        Var message: String = "I forgot to close the scope, "
                              +. "and it leads to an error";
}"""
        expect = "Error on line 5 col 1: <EOF>"
        self.assertTrue(TestParser.test(input,expect,275))

    def test_complex_program14(self):
        input = """Class Program {
    main() {
        Var sum: Int = 0;
        Foreach(i In 1 .. 100) {
            Foreach(j In 1 .. 100) {
                sum = sum + 1;
            Continue;
        }
    }
}"""
        expect = "Error on line 10 col 1: <EOF>"
        self.assertTrue(TestParser.test(input,expect,276))

    def test_complex_program15(self):
        input = """Class Program {
    main() {
        Var sum: Int = 0;
        Foreach(i In 1 .. 100) {
            Foreach(j In 1 .. 100 By 1 {
                sum = sum + 1;
                Continue
            }
            Continue;
        }
    }
}"""
        expect = "Error on line 5 col 39: {"
        self.assertTrue(TestParser.test(input,expect,277))

    def test_complex_program16(self):
        input = """Class Program {
    $pow(a,n:Int) {
        Var powa, ans: Int = a, 1;
        Foreach(temp In 0 .. 1 By 0) {
            If (n % 2 == 1) { ans = ans * powa; }
            n = n / 2; powa = powa * powa;
            If (n == 0) { Break; }
        }
        Return ans;
    }
    main() {
        Var temp_variable: Int = $pow(100,200000);
        Return;
    }
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,278))

    def test_complex_program17(self):
        input = """Class Program {
    $pow(a,n:Int) {
        Var powa, ans: Int = a, 1;
        Foreach(temp In 0 .. 1 By 0) {
            If (n % 2 == 1) { ans = ans * powa; }
            n = n / 2; powa = powa * powa;
            If (n == 0) { Break; }
        }
        Return ans;
    }
    main() {
        Var temp_variable: Int = $pow(100,200000);
        {
            Var temp_variable: Int = $pow(2000,200000);
            Return;
        }
        {} {} {{}}
        {{{}}}
        {{}{}}
    }
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,279))

    def test_complex_program18(self):
        input = """Class Cookie {
    Var message: String;
    Constructor() { message = "Don\\'t ask me why!!"; }
    $askForPermission() { Return True; }
    $collectFromUser() { Return New Cookie(); Return Null; }
}
Class Program {
    Var userCookie: Cookie;
    main() {
        If (Cookie::$askForPermission()) { userCookie = Cookie::$collectFromUser(); }
        Else { Return; }
    }
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,280))

    def test_complex_program19(self):
        input = """Class Program {
    main(## main function should have no parameter ##) {
        Return ## main function does not return anything ##;
    }
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,281))

    def test_complex_program20(self):
        input = """Class Program {
    main() {
        System::$Println("Looking for trouble to troubleshoot");
        System::$Sleep("5 minutes");
        System::$Println("No problem found");
        Return;
    }
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,282))

    def test_complex_program21(self):
        input = """Class Program {
    main(i:Int) { Return "This is not the main function!!!"; }
    main() {
        If (main(0xCAFE_1234) == main(0)) { Return; }
    }
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,283))

    def test_complex_program22(self):
        input = """## This line does not contain anything##
Class member {
    Constructor() {}
}
Class Program {
    Var arr: Array[member,5] = Array(Null, New member(), Null, New member(), Null);
    main() {}
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,284))

    def test_complex_program23(self):
        input = """## This line does not contain anything##
Class member {
    Constructor() {}
    Constructor(i:Int) {}
}
Class Program {
    Var arr: Array[Array[member,5],5] = Array(Array(Null, New member(), Null, New member(0), Null),
                                              Array(Null, New member(), Null, New member(1), Null),
                                              Array(Null, New member(), Null, New member(2), Null),
                                              Array(Null, New member(), Null, New member(3), Null),
                                              Array(Null, New member(), Null, New member(4), Null));
    main() {}
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,285))

    def test_complex_program24(self):
        input = """## This line does not contain anything##
Class member {
    Constructor() {}
    message() { Return "hello world"; }
}
Class Program {
    Var arr: Array[member,5] = Array(Null, New member(), Null, New member(), Null);
    main() {
        Foreach (i In 1 .. 5) {
            arr[i].message();
        }
    }
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,286))

    def test_complex_program25(self):
        input = """## This line does not contain anything##
Class member {
    Constructor() {}
    Var message: String;
    message() { Return "hello world"; }
}
Class Program {
    Var arr: Array[member,5] = Array(Null, New member(), Null, New member(), Null);
    main() {
        Foreach (i In 1 .. 5) {
            arr[i].message = arr[i].message();
        }
    }
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,287))

    def test_complex_program26(self):
        input = """## This line does not contain anything##
Class member {
    Constructor() {}
    Var message: String;
    message() { Return "hello world"; }
}
Class Program {
    Var arr: Array[member,5];
    main() {
        Foreach (i In 1 .. 5) { arr[i] = Null; }
        Foreach (i In 1 .. 5) { arr[i] = New member(); }
    }
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,288))

    def test_complex_program27(self):
        input = """## This line does not contain anything##
Class member {
    Constructor() {}
    Var message: String;
    message() { Return "hello world"; }
}
Class subclass : member {}
Class Program {
    Var arr: Array[subclass,5];
    main() {
        Foreach (i In 1 .. 5) { arr[i] = Null; }
        Foreach (i In 1 .. 5) { arr[i] = New subclass(); }
        Foreach (i In 1 .. 5) { arr[i] = New member(); }
    }
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,289))


    def test_complex_program28(self):
        input = """Class Program {}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,290))

    def test_complex_program29(self):
        input = """Class Program { main() {} }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,291))

    def test_complex_program30(self):
        input = """Class Program { func1(){} $func2(){} }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,292))

    def test_complex_program31(self):
        input = """Class class1 { func1(){} func2(){} }
                   Class class2 { Constructor(){} Constructor(a,b,c:String){} Destructor(){} }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,293))

    def test_complex_program32(self):
        input = """Class 123 {}"""
        expect = "Error on line 1 col 6: 123"
        self.assertTrue(TestParser.test(input,expect,294))

    def test_complex_program33(self):
        input = """Class empty_class {}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,295))

    def test_complex_program34(self):
        input = """Class _ { _(){} Constructor(){} Destructor(a:Int){} }"""
        expect = "Error on line 1 col 43: a"
        self.assertTrue(TestParser.test(input,expect,296))

    def test_complex_program35(self):
        input = """Class $wrong_id { main() }"""
        expect = "Error on line 1 col 6: $wrong_id"
        self.assertTrue(TestParser.test(input,expect,297))

    def test_complex_program36(self):
        input = """Class _ { func() {}"""
        expect = "Error on line 1 col 19: <EOF>"
        self.assertTrue(TestParser.test(input,expect,298))

    def test_complex_program37(self):
        input = """Class { func(Var $abc: Int) {} }"""
        expect = "Error on line 1 col 6: {"
        self.assertTrue(TestParser.test(input,expect,299))