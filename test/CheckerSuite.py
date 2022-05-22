import unittest
from StaticError import *
from TestUtils import TestChecker
from AST import *


OK = '[]'

class CheckerSuite(unittest.TestCase):
    def test_class_declare1(self):
        input = """Class a{} Class a{}"""
        expect = str(Redeclared(Class(),'a'))
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_class_declare2(self):
        input = """Class a : b{}"""
        expect = str(Undeclared(Class(),'b'))
        self.assertTrue(TestChecker.test(input,expect,401))

    def test_class_declare3(self):
        input = """Class b{} Class a : b{} Class a{}"""
        expect = str(Redeclared(Class(),'a'))
        self.assertTrue(TestChecker.test(input,expect,402))

    def test_class_declare4(self):
        input = """Class a{} Class b : a{} Class c : b{} Class c"""
        expect = str(Redeclared(Class(),'c'))
        self.assertTrue(TestChecker.test(input,expect,403))

    def test_class_declare5(self):
        input = """Class a{} Class b : a{} Class c : b{} Class d : c{} Class e : f{}"""
        expect = str(Undeclared(Class(),'f'))
        self.assertTrue(TestChecker.test(input,expect,404))

    def test_attribute_declare1(self):
        input = """Class A{Var a: Int; Var a: Int;}"""
        expect = str(Redeclared(Attribute(),'a'))
        self.assertTrue(TestChecker.test(input,expect,405))

    def test_attribute_declare2(self):
        input = """Class A{Var a: Int; Var b, a: Float;}"""
        expect = str(Redeclared(Attribute(),'a'))
        self.assertTrue(TestChecker.test(input,expect,406))

    def test_attribute_declare3(self):
        input = """Class A{Var a, a: Int;}"""
        expect = str(Redeclared(Attribute(),'a'))
        self.assertTrue(TestChecker.test(input,expect,407))

    def test_attribute_declare4(self):
        input = """Class A{Var a: Int; Var b: Float; Var c, a: String;}"""
        expect = str(Redeclared(Attribute(),'a'))
        self.assertTrue(TestChecker.test(input,expect,408))

    def test_attribute_declare5(self):
        input = """Class A{Var a: Int; Var b: Float; Var c, a: String;}"""
        expect = str(Redeclared(Attribute(),'a'))
        self.assertTrue(TestChecker.test(input,expect,409))

    def test_attribute_declare6(self):
        input = """Class A{Var a: B;}"""
        expect = str(Undeclared(Class(),'B'))
        self.assertTrue(TestChecker.test(input,expect,410))

    def test_attribute_declare7(self):
        input = """Class A{Var a: A; Var b: B;}"""
        expect = str(Undeclared(Class(),'B'))
        self.assertTrue(TestChecker.test(input,expect,411))

    def test_attribute_declare8(self):
        input = """Class A{Var a: A;} Class B{Var a: A; Var b: B; Var c: C;}"""
        expect = str(Undeclared(Class(),'C'))
        self.assertTrue(TestChecker.test(input,expect,412))

    def test_attribute_declare9(self):
        input = """Class A{Var a: A;} Class B : D{Var a: A; Var b: B; Var c: C;}"""
        expect = str(Undeclared(Class(),'D'))
        self.assertTrue(TestChecker.test(input,expect,413))

    def test_attribute_declare10(self):
        input = """Class A{Var arr: Array[Int,5]; Var a: B;}"""
        expect = str(Undeclared(Class(),'B'))
        self.assertTrue(TestChecker.test(input,expect,414))

    def test_attribute_declare11(self):
        input = """Class A{Var arr: Array[Array[Int,6],5]; Var a: B;}"""
        expect = str(Undeclared(Class(),'B'))
        self.assertTrue(TestChecker.test(input,expect,415))

    def test_attribute_declare12(self):
        input = """Class A{Var arr: Array[Array[A,6],5]; Var a: B;}"""
        expect = str(Undeclared(Class(),'B'))
        self.assertTrue(TestChecker.test(input,expect,416))

    def test_attribute_declare13(self):
        input = """Class A{Var arr: Array[Array[B,6],5]; Var a: A;}"""
        expect = str(Undeclared(Class(),'B'))
        self.assertTrue(TestChecker.test(input,expect,417))

    def test_attribute_declare14(self):
        input = """Class A{Var x: Int = 5.0;}"""
        expect = str(TypeMismatchInStatement(VarDecl(Id('x'),IntType(),FloatLiteral('5.0'))))
        self.assertTrue(TestChecker.test(input,expect,418))

    def test_attribute_declare15(self):
        input = """Class A{Var x: String = "hello world"; Var y: Int = "hello world"}"""
        expect = str(TypeMismatchInStatement(VarDecl(Id('y'),IntType(),StringLiteral('hello world'))))
        self.assertTrue(TestChecker.test(input,expect,419))

    def test_attribute_declare16(self):
        input = """Class A{Var x: Array[Int,3] = Array(1,2,"");}"""
        expect = str(IllegalArrayLiteral(ArrayLiteral([IntLiteral('1'),IntLiteral('2'),StringLiteral('')])))
        self.assertTrue(TestChecker.test(input,expect,420))

    def test_attribute_declare17(self):
        input = """Class A{Var x: Array[Int,3] = Array(1.0,2.0,3.0);}"""
        expect = str(TypeMismatchInStatement(VarDecl(Id('x'),ArrayType(3,IntType()),ArrayLiteral([FloatLiteral('1.0'),FloatLiteral('2.0'),FloatLiteral('3.0')]))))
        self.assertTrue(TestChecker.test(input,expect,421))

    def test_entry_point1(self):
        input = """Class A{}"""
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input,expect,422))

    def test_entry_point2(self):
        input = """Class Program{}"""
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input,expect,423))

    def test_entry_point3(self):
        input = """Class Program{main(){}}"""
        expect = OK
        self.assertTrue(TestChecker.test(input,expect,424))

    def test_entry_point4(self):
        input = """Class Program{not_main(){}} Class not_Program{main(){}}"""
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input,expect,425))

    def test_entry_point5(self):
        input = """Class Program{$main(){}}"""
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input,expect,426))

    def test_operator1(self):
        input = """Class Program{ Var x: Float = 1.0 + True; }"""
        expect = str(TypeMismatchInExpression(BinaryOp('+',FloatLiteral('1.0'),BooleanLiteral('True'))))
        self.assertTrue(TestChecker.test(input,expect,427))

    def test_operator2(self):
        input = """Class Program{ Var x: Int = 1.0 + 2.0; }"""
        expect = str(TypeMismatchInStatement(VarDecl(Id('x'),IntType(),BinaryOp('+',FloatLiteral('1.0'),FloatLiteral('2.0')))))
        self.assertTrue(TestChecker.test(input,expect,428))

    def test_operator3(self):
        input = """Class Program{ Var x: String = "hello" + "world"; }"""
        expect = str(TypeMismatchInExpression(BinaryOp('+',StringLiteral('hello'),StringLiteral('world'))))
        self.assertTrue(TestChecker.test(input,expect,429))

    def test_operator4(self):
        input = """Class Program{ main(){} Var x: String = "hello" +. "world"; }"""
        expect = OK
        self.assertTrue(TestChecker.test(input,expect,430))

    def test_operator5(self):
        input = """Class Program{ main(){} Var x: Float = (-1 + 2.0) * 3 / 4; }"""
        expect = OK
        self.assertTrue(TestChecker.test(input,expect,431))

    def test_operator6(self):
        input = """Class Program{ main(){} Var x: Int = 3 / 4; }"""
        expect = OK
        self.assertTrue(TestChecker.test(input,expect,432))

    def test_operator7(self):
        input = """Class Program{ main(){} Var x: Boolean = ((3 / 4) < 5) || !True || False; }"""
        expect = OK
        self.assertTrue(TestChecker.test(input,expect,433))

    def test_operator8(self):
        input = """Class Program{ main(){} Var x: Boolean = "hello" +. "world" ==. "helloworld"; }"""
        expect = OK
        self.assertTrue(TestChecker.test(input,expect,434))

    def test_operator9(self):
        input = """Class Program{ main(){} Var x: Boolean = (1.0 == 2.0) && False; }"""
        expect = str(TypeMismatchInExpression(BinaryOp('==',FloatLiteral('1.0'),FloatLiteral('2.0'))))
        self.assertTrue(TestChecker.test(input,expect,435))

    def test_operator10(self):
        input = """Class Program{ main(){} Var x: Boolean = (True == False) || (1 != 2) && False; }"""
        expect = OK
        self.assertTrue(TestChecker.test(input,expect,436))

    def test_operator11(self):
        input = """Class Program{ main(){} Var x: String = 1 == 2; }"""
        expect = str(TypeMismatchInStatement(VarDecl(Id('x'),StringType(),BinaryOp('==',IntLiteral('1'),IntLiteral('2')))))
        self.assertTrue(TestChecker.test(input,expect,437))
    
    def test_id1(self):
        input = """Class Program{ main(){} Var x, y: Int = 1, x + 1; }"""
        expect = OK
        self.assertTrue(TestChecker.test(input,expect,438))

    def test_id2(self):
        input = """Class Program{ main(){} Var x: String; Val y: Int = x + 1; }"""
        expect = str(TypeMismatchInExpression(BinaryOp('+',Id('x'),IntLiteral('1'))))
        self.assertTrue(TestChecker.test(input,expect,439))

    def test_id3(self):
        input = """Class Program{ main(){} Val y: Int = x + 1; }"""
        expect = str(Undeclared(Identifier(),'x'))
        self.assertTrue(TestChecker.test(input,expect,440))

    def test_attribute_declare18(self):
        input = """Class A{Val x: Int;}"""
        expect = str(IllegalConstantExpression(None))
        self.assertTrue(TestChecker.test(input,expect,441))

    def test_attribute_declare19(self):
        input = """Class A{Var x: Int; Val y: Int = x}"""
        expect = str(IllegalConstantExpression(Id('x')))
        self.assertTrue(TestChecker.test(input,expect,442))

    def test_arraycell1(self):
        input = """Class Program{ main(){} Var x: Int = Array(1,2)[0]; }"""
        expect = OK
        self.assertTrue(TestChecker.test(input,expect,443))

    def test_arraycell2(self):
        input = """Class Program{ main(){} Var x: Array[Array[Int,2],2] = Array(Array(1,2),Array(3,4)); Var y: Int = x[1][1]; }"""
        expect = OK
        self.assertTrue(TestChecker.test(input,expect,444))

    def test_arraycell3(self):
        input = """Class Program{ main(){} Var x: Array[Array[Int,2],2] = Array(Array(1,2),Array(3,4)); Var y: Int = x[1][1][1]; }"""
        expect = str(TypeMismatchInExpression(ArrayCell(Id('x'),[IntLiteral('1'),IntLiteral('1'),IntLiteral('1')])))
        self.assertTrue(TestChecker.test(input,expect,445))

    def test_arraycell4(self):
        input = """Class Program{ main(){} Var x: Array[Array[Int,2],2] = Array(Array(1,2),Array(3,4)); Var y: String = x[1][1]; }"""
        expect = str(TypeMismatchInStatement(VarDecl(Id('y'),StringType(),ArrayCell(Id('x'),[IntLiteral('1'),IntLiteral('1')]))))
        self.assertTrue(TestChecker.test(input,expect,446))

    def test_attribute_declare20(self):
        input = """Class A{Var x: Int;} Class B{Var x: Int;}"""
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input,expect,447))
    
    def test_basic_method1(self):
        input = """Class Program{main(){} Var main: Int;}"""
        expect = OK
        self.assertTrue(TestChecker.test(input,expect,448))

    def test_attribute_declare21(self):
        input = """Class A{Var x: Int;} Class B{Var x: Int = A;}"""
        expect = str(Undeclared(Identifier(), 'A'))
        self.assertTrue(TestChecker.test(input,expect,449))
    
    def test_return_statement1(self):
        input = """Class Program{ main(){Return;} }"""
        expect = OK
        self.assertTrue(TestChecker.test(input,expect,450))
    
    def test_return_statement2(self):
        input = """Class Program{ main(){Return 123;} }"""
        expect = str(TypeMismatchInStatement(Return(IntLiteral('123'))))
        self.assertTrue(TestChecker.test(input,expect,451))
    
    def test_return_statement3(self):
        input = """Class Program{ func(){Return 1; Return 2;} main(){} }"""
        expect = OK
        self.assertTrue(TestChecker.test(input,expect,452))
    
    def test_return_statement4(self):
        input = """Class Program{ func(){Return 1; Return "";} main(){} }"""
        expect = str(TypeMismatchInStatement(Return(StringLiteral(''))))
        self.assertTrue(TestChecker.test(input,expect,453))
    
    def test_return_statement5(self):
        input = """Class Program{ func(){Return 1; {Return "";}} main(){} }"""
        expect = str(TypeMismatchInStatement(Return(StringLiteral(''))))
        self.assertTrue(TestChecker.test(input,expect,454))
    
    def test_return_statement6(self):
        input = """Class Program{ func(){Return 1; If(True){Return "";}} main(){} }"""
        expect = str(TypeMismatchInStatement(Return(StringLiteral(''))))
        self.assertTrue(TestChecker.test(input,expect,455))
    
    def test_return_statement7(self):
        input = """
        Class Program {
            func() {
                Return 1;
                {
                    Return 2;
                    {
                        Return 0b3;
                        Return 04;
                    }
                    Return 0x567;
                    {
                        Return 891011;
                    }
                }
                Var i: Int;
                Foreach(i In 1 .. 100) {
                    Return "";
                }
            }
            main() {}
        }
        """
        expect = str(TypeMismatchInStatement(Return(StringLiteral(''))))
        self.assertTrue(TestChecker.test(input,expect,456))

    def test_callexpr1(self):
        input = """
        Class A { $method(){} }
        Class Program { main(){ A::$method(); } }
        """
        expect = OK
        self.assertTrue(TestChecker.test(input,expect,457))

    def test_callexpr2(self):
        input = """
        Class A { $method(x,y:Int;z:Float){ Return 1; } }
        Class Program { main(){} Var x: String = A::$method(1,2,2.0)}
        """
        expect = str(TypeMismatchInStatement(VarDecl(Id('x'),StringType(),CallExpr(Id('A'),Id('$method'),[IntLiteral('1'),IntLiteral('2'),FloatLiteral('2.0')]))))
        self.assertTrue(TestChecker.test(input,expect,458))

    def test_callexpr3(self):
        input = """
        Class A { $method(x,y:Int;z:Float){ Return 1; } }
        Class Program { main(){} Var x: Int = A::$method(1,2)}
        """
        expect = str(IllegalMemberAccess(CallExpr(Id('A'),Id('$method'),[IntLiteral('1'),IntLiteral('2')])))
        self.assertTrue(TestChecker.test(input,expect,459))
    
    def test_if_stmt1(self):
        input = """
        Class Program {
            main() {
                Val x: Boolean = True;
                If (x) {
                    If (1) {
                    }
                    Return;
                }
            }
        }
        """
        expect = str(TypeMismatchInStatement(If(IntLiteral('1'),Block([]))))
        self.assertTrue(TestChecker.test(input,expect,460))
    
    def test_if_stmt2(self):
        input = """
        Class Program {
            main() {
                If (1 + 1 == 2) {
                    If (!False || ("hello" +. "world" ==. "helloworld")) {
                    }
                    Return;
                }
            }
        }
        """
        expect = OK
        self.assertTrue(TestChecker.test(input,expect,461))
    
    def test_if_stmt3(self):
        input = """
        Class Program {
            main() {
                If (1 + 1 == 2) {
                    If (!False || ("hello" +. "world" ==. "helloworld")) {}
                    Elseif(True) {}
                    Else {}
                    Return;
                }
            }
        }
        """
        expect = OK
        self.assertTrue(TestChecker.test(input,expect,462))
    
    def test_for_stmt1(self):
        input = """
        Class Program {
            main() {
                Var i: Int;
                Foreach(i In 1 .. 100) {}
            }
        }
        """
        expect = OK
        self.assertTrue(TestChecker.test(input,expect,463))
    
    def test_for_stmt2(self):
        input = """
        Class Program {
            main() {
                Val i: Int = 1;
                Foreach(i In 1 .. 100) {}
            }
        }
        """
        expect = str(CannotAssignToConstant(Assign(Id('i'),IntLiteral('1'))))
        self.assertTrue(TestChecker.test(input,expect,464))
    
    def test_for_stmt3(self):
        input = """
        Class Program {
            main() {
                Var i: Int = 1;
                Foreach(i In i .. i+100 By 1*i) {}
            }
        }
        """
        expect = OK
        self.assertTrue(TestChecker.test(input,expect,465))
    
    def test_for_stmt4(self):
        input = """
        Class Program {
            main() {
                Var i: Int = 1;
                Foreach(i In True .. i+100) {}
            }
        }
        """
        expect = str(TypeMismatchInStatement(For(Id('i'),BooleanLiteral('True'),BinaryOp('+',Id('i'),IntLiteral('100')),Block([]))))
        self.assertTrue(TestChecker.test(input,expect,466))
    
    def test_newexpr1(self):
        input = """
        Class A {}
        Class Program {
            main() {
                Var x: A = New A();
            }
        }
        """
        expect = OK
        self.assertTrue(TestChecker.test(input,expect,467))
    
    def test_newexpr2(self):
        input = """
        Class A {
            Constructor(x:Int) {}
        }
        Class Program {
            main() {
                Var x: A = New A(0);
            }
        }
        """
        expect = OK
        self.assertTrue(TestChecker.test(input,expect,468))
    
    def test_newexpr3(self):
        input = """
        Class A {}
        Class Program {
            main() {
                Var x: A = New A(0);
            }
        }
        """
        expect = str(TypeMismatchInExpression(NewExpr(Id('A'),[IntLiteral('0')])))
        self.assertTrue(TestChecker.test(input,expect,469))
    
    def test_newexpr4(self):
        input = """
        Class A {
            Constructor(x:Int) {}
        }
        Class Program {
            main() {
                Var x: A = New A();
            }
        }
        """
        expect = str(TypeMismatchInExpression(NewExpr(Id('A'),[])))
        self.assertTrue(TestChecker.test(input,expect,470))
    
    def test_newexpr5(self):
        input = """
        Class Program {
            main() {
                Var x: A = New A();
            }
        }
        """
        expect = str(Undeclared(Class(),'A'))
        self.assertTrue(TestChecker.test(input,expect,471))
    
    def test_newexpr6(self):
        input = """
        Class Program {
            Val A: Int = 1; ## This is a variable with name A, not class A ##
            main() {
                Var x: A = New A();
            }
        }
        """
        expect = str(Undeclared(Class(),'A'))
        self.assertTrue(TestChecker.test(input,expect,472))
    
    def test_newexpr7(self):
        input = """
        Class Program {
            Var i: Int;
            Var next: Program = New Program();
            main() {}
        }
        """
        expect = OK
        self.assertTrue(TestChecker.test(input,expect,473))
    
    def test_newexpr8(self):
        input = """
        Class Program {
            Constructor(x:Int) {}
            Var i: Int;
            Var next: Program = New Program(1);
            main() {}
        }
        """
        expect = OK
        self.assertTrue(TestChecker.test(input,expect,474))
    
    def test_callexpr4(self):
        input = """
        Class A {
            $func(x:String) {Return 1;}
            func(x:String) {Return 1;}
        }
        Class Program {
            Var x, y: Int = A::$func(""), (New A()).func("");
            main() {}
        }
        """
        expect = OK
        self.assertTrue(TestChecker.test(input,expect,475))

    def test_basic_method2(self):
        input = """
        Class Program {
            func(x:Int;x:Int) {}
            main() {}
        }
        """
        expect = str(Redeclared(Parameter(),'x'))
        self.assertTrue(TestChecker.test(input,expect,476))
    
    def test_callexpr5(self):
        input = """
        Class Program {
            Var x: Int = A::$func("");
            main() {}
        }
        """
        expect = str(Undeclared(Class(),'A'))
        self.assertTrue(TestChecker.test(input,expect,477))
    
    def test_callexpr6(self):
        input = """
        Class Program {
            Var x: Int = a.func("");
            main() {}
        }
        """
        expect = str(Undeclared(Identifier(),'a'))
        self.assertTrue(TestChecker.test(input,expect,478))
    
    def test_callexpr7(self):
        input = """
        Class A {}
        Class B {
            func() {
                Return New A();
            }
        }
        Class C {
            func() {
                Return New B();
            }
        }
        Class Program {
            Var a: A = (New C()).func().func();
            main() {}
        }
        """
        expect = OK
        self.assertTrue(TestChecker.test(input,expect,479))
    
    def test_callexpr8(self):
        input = """
        Class A {}
        Class Program {
            Var a: A = True.func();
            main() {}
        }
        """
        expect = str(TypeMismatchInExpression(CallExpr(BooleanLiteral('True'),Id('func'),[])))
        self.assertTrue(TestChecker.test(input,expect,480))
    
    def test_fieldaccess1(self):
        input = """
        Class A {
            Var x, $x: Int;
        }
        Class Program {
            Var x, y: Int = (New A()).x, A::$x;
            main() {}
        }
        """
        expect = OK
        self.assertTrue(TestChecker.test(input,expect,481))
    
    def test_fieldaccess2(self):
        input = """
        Class A {}
        Class Program {
            Var x: Int = (New A()).x;
            main() {}
        }
        """
        expect = str(Undeclared(Attribute(),'x'))
        self.assertTrue(TestChecker.test(input,expect,482))
    
    def test_loop1(self):
        input = """
        Class Program {
            main() {
                Break;
            }
        }
        """
        expect = str(MustInLoop(Break()))
        self.assertTrue(TestChecker.test(input,expect,483))
    
    def test_loop2(self):
        input = """
        Class Program {
            main() {
                Var i: Int;
                Foreach (i In 1 .. 100) {
                    Break;
                }
            }
        }
        """
        expect = OK
        self.assertTrue(TestChecker.test(input,expect,484))
    
    def test_loop3(self):
        input = """
        Class Program {
            main() {
                Var i: Int;
                Foreach (i In 1 .. 100) {
                    Var j: Int;
                    Foreach  (j In 1 .. 100) {
                        Break;
                        Continue;
                    }
                    If (True) { Break; }
                    Elseif (False) { Continue; }
                    Else { Continue; }
                    {
                        If (True) { Break; }
                    }
                }
            }
        }
        """
        expect = OK
        self.assertTrue(TestChecker.test(input,expect,485))

    def test_loop4(self):
        input = """
        Class Program {
            main() {
                If (True) {
                    Break;
                }
            }
        }
        """
        expect = str(MustInLoop(Break()))
        self.assertTrue(TestChecker.test(input,expect,486))

    def test_callstmt1(self):
        input = """
        Class Program {
            func() {}
            main() {
                Self.func();
            }
        }
        """
        expect = OK
        self.assertTrue(TestChecker.test(input,expect,487))

    def test_callstmt2(self):
        input = """
        Class Program {
            func() {}
            main() {
                Self.func0();
            }
        }
        """
        expect = str(Undeclared(Method(),'func0'))
        self.assertTrue(TestChecker.test(input,expect,488))

    def test_callstmt3(self):
        input = """
        Class Program {
            func(x:Int) {}
            main() {
                Self.func();
            }
        }
        """
        expect = str(TypeMismatchInStatement(CallStmt(SelfLiteral(),Id('func'),[])))
        self.assertTrue(TestChecker.test(input,expect,489))

    def test_callstmt4(self):
        input = """
        Class Program {
            func() { Return 1; }
            main() {
                Self.func();
            }
        }
        """
        expect = str(TypeMismatchInStatement(CallStmt(SelfLiteral(),Id('func'),[])))
        self.assertTrue(TestChecker.test(input,expect,489))
    
    def test_callexpr9(self):
        input = """
        Class Program {
            func() { Return 1; }
            main() {
                Var x: String = Self.func();
            }
        }
        """
        expect = str(TypeMismatchInStatement(VarDecl(Id('x'),StringType(),CallExpr(SelfLiteral(),Id('func'),[]))))
        self.assertTrue(TestChecker.test(input,expect,490))
    
    def test_callexpr9(self):
        input = """
        Class Program {
            func() { Return 1; }
            main() {
                Var x: String = Self.func();
            }
        }
        """
        expect = str(TypeMismatchInStatement(VarDecl(Id('x'),StringType(),CallExpr(SelfLiteral(),Id('func'),[]))))
        self.assertTrue(TestChecker.test(input,expect,491))

    def test_arrayliteral(self):
        input = """
        Class Program {
            main() {
                Var arr: Array[Int,5] = Array(1,2,3,4);
            }
        }
        """
        expect = str(TypeMismatchInStatement(VarDecl(Id('arr'),ArrayType(5,IntType()),ArrayLiteral([IntLiteral('1'),IntLiteral('2'),IntLiteral('3'),IntLiteral('4')]))))
        self.assertTrue(TestChecker.test(input,expect,492))
    
    def test_complex_program1(self):
        input = """
        Class A {}
        Class Program {
            Var arr: Array[A,5] = Array(New A(), New A(), Null, Null, New A());
            main() {}
        }
        """
        expect = OK
        self.assertTrue(TestChecker.test(input,expect,493))
    
    def test_complex_program2(self):
        input = """
        Class A {
            Var $arr: Array[Int,3];
        }
        Class Program {
            Var x: Array[Int,4] = A::$arr;
            main() {}
        }
        """
        expect = str(TypeMismatchInStatement(VarDecl(Id('x'),ArrayType(4,IntType()),FieldAccess(Id('A'),Id('$arr')))))
        self.assertTrue(TestChecker.test(input,expect,494))
    
    def test_complex_program3(self):
        input = """
        Class B {
            func() {}
        }
        Class A {
            Var arr: Array[B,5];
        }
        Class class {
            Var $a: A = New A();
        }
        Class Program {
            main() {
                class::$a.arr[1].func();
            }
        }
        """
        expect = OK
        self.assertTrue(TestChecker.test(input,expect,495))
    
    def test_complex_program4(self):
        input = """
        Class B {
            func() {}
        }
        Class A {
            Var arr: Array[B,5];
        }
        Class class {
            Var $a: A = New A();
        }
        Class Program {
            main() {
                Var x: A = class::$a.arr[1].func();
            }
        }
        """
        expect = str(TypeMismatchInStatement(VarDecl(Id('x'),ClassType(Id('A')),CallExpr(ArrayCell(FieldAccess(FieldAccess(Id('class'),Id('$a')),Id('arr')),[IntLiteral(1)]),Id('func'),[]))))
        self.assertTrue(TestChecker.test(input,expect,496))
    
    def test_complex_program5(self):
        input = """
        Class Node {
            Var x: Int = 0;
            Var next: Node = Null;
            Constructor(x:Int;next:Node) {
                Self.x = x;
                Self.next = next;
            }
        }
        Class Program {
            main() {
                Var head: Node = New Node(1,
                                 New Node(2,
                                 New Node(3,
                                 New Node(4,
                                 New Node(5,
                                    Null)))));
            }
        }
        """
        expect = OK
        self.assertTrue(TestChecker.test(input,expect,497))
    
    def test_complex_program6(self):
        input = """
        Class Math {
            Var $pi: Float = 3.14;
            $fact(n:Int) {
                If (n <= 1) { Return 1; }
                Else { Return Math::$fact(n-1) * n; }
            }
            $P(n,k:Int) {
                Return Math::$fact(n) / Math::$fact(n-k);
            }
            $C(n,k:Int) {
                Return Math::$fact(n) / (Math::$fact(k) * Math::$fact(n-k));
            }
        }
        Class Program {
            main() {
                Var x: Int = Math::$C(10000,5);
                x = Math::$P(10000,5);
                Math::$pi = 3.141592653589;
            }
        }
        """
        expect = OK
        self.assertTrue(TestChecker.test(input,expect,498))

    def test_assign_stmt(self):
        input = """
        Class A {}
        Class Program {
            main() {
                A::$x = 12345;
            }
        }
        """
        expect = str(Undeclared(Attribute(),'$x'))
        self.assertTrue(TestChecker.test(input,expect,499))