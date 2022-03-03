from array import ArrayType
from msilib.schema import Binary, Class
import unittest
from attr import Attribute

from pandas import BooleanDtype
from TestUtils import TestAST
from AST import *
from main.d96.astgen.AST import ArrayCell, ArrayLiteral, ClassType, FieldAccess, NewExpr, NullLiteral
from main.d96.utils.AST import AST, AttributeDecl, BinaryOp, BoolType, BooleanLiteral, ClassDecl, ConstDecl,  FloatLiteral, FloatType, Id, Instance, IntLiteral, IntType, Program, Static, StringLiteral, StringType, UnaryOp, VarDecl
 
class ASTGenSuite(unittest.TestCase):

    def test_simple_program1(self):
        input = ""
        expect = str(Program([]))
        self.assertTrue(TestAST.test(input,expect,300))

    def test_simple_program2(self):
        input = """
Class class1{}
Class class2{}
Class class3 : parent{}
"""
        expect = str(Program([ClassDecl(Id('class1'),[]),
                              ClassDecl(Id('class2'),[]),
                              ClassDecl(Id('class3'),[],Id('parent'))]))
        self.assertTrue(TestAST.test(input,expect,301))


    def test_primitivetype_attributes1(self):
        input = """
Class Program {
    Var a, b: Int;
    Var $c: Float;
    Var $d: Boolean;
    Var e, $f: String;
}"""
        expect = str(Program([
ClassDecl(Id('Program'),[
    AttributeDecl(Instance(), VarDecl( Id('a'), IntType() )),
    AttributeDecl(Instance(), VarDecl( Id('b'), IntType() )),
    AttributeDecl(Static(), VarDecl( Id('$c'), FloatType() )),
    AttributeDecl(Static(), VarDecl( Id('$d'), BoolType() )),
    AttributeDecl(Instance(), VarDecl( Id('e'), StringType() )),
    AttributeDecl(Static(), VarDecl( Id('$f'), StringType() ))
])
]))
        self.assertTrue(TestAST.test(input,expect,302))


    def test_primitivetype_attributes2(self):
        input = """
Class _class1 {
    Var a, b: Int;
    Var $c: Float;
}
Class _class2 {
    Var $d: Boolean;
    Var e, $f: String;
}
"""
        expect = str(Program([
ClassDecl(Id('_class1'),[
    AttributeDecl(Instance(), VarDecl( Id('a'), IntType() )),
    AttributeDecl(Instance(), VarDecl( Id('b'), IntType() )),
    AttributeDecl(Static(), VarDecl( Id('$c'), FloatType() )),\
]),
ClassDecl(Id('_class2'),[    
    AttributeDecl(Static(), VarDecl( Id('$d'), BoolType() )),
    AttributeDecl(Instance(), VarDecl( Id('e'), StringType() )),
    AttributeDecl(Static(), VarDecl( Id('$f'), StringType() ))
])
]))
        self.assertTrue(TestAST.test(input,expect,303))


    def test_primitivetype_attributes3(self):
        input = """
Class Program {
    Var a, b: Int = 123, 0xCA_FE;
    Val $c: Float = 0.3141592653589e1;
    Var $d: Boolean = True;
    Val e, $f: String = "first", "second";
}
"""
        expect = str(Program([
ClassDecl(Id('Program'),[
    AttributeDecl(Instance(), VarDecl( Id('a'), IntType(), IntLiteral('123') )),
    AttributeDecl(Instance(), VarDecl( Id('b'), IntType(), IntLiteral('0xCAFE') )),
    AttributeDecl(Static(), ConstDecl( Id('$c'), FloatType(), FloatLiteral('0.3141592653589e1') )),
    AttributeDecl(Static(), VarDecl( Id('$d'), BoolType(), BooleanLiteral('True') )),
    AttributeDecl(Instance(), ConstDecl( Id('e'), StringType(), StringLiteral('"first"') )),
    AttributeDecl(Static(), ConstDecl( Id('$f'), StringType(), StringLiteral('"second"') ))
])
]))
        self.assertTrue(TestAST.test(input,expect,304))

    
    def test_primitivetype_attributes4(self):
        input = """
Class Program {
    Val a, b: Int = -1, 2+3;
    Var $a, $b: Int = 1+2*3, (1+2)*3;
    Val c: Int = 0123 + 0xCAFE * 0b1001  + 1_000;
    Var $c: Int = a / b;
}
"""
        expect = str(Program([
ClassDecl(Id('Program'),[
    AttributeDecl(Instance(), ConstDecl( Id('a'), IntType(), UnaryOp('-',IntLiteral('1')) )),
    AttributeDecl(Instance(), ConstDecl( Id('b'), IntType(), BinaryOp('+',IntLiteral('2'),IntLiteral('3')) )),    
    AttributeDecl(Static(), VarDecl( Id('$a'), IntType(), BinaryOp('+',IntLiteral('1'),BinaryOp('*',IntLiteral('2'),IntLiteral('3'))) )),
    AttributeDecl(Static(), VarDecl( Id('$b'), IntType(), BinaryOp('*',BinaryOp('+',IntLiteral('1'),IntLiteral('2')),IntLiteral('3')) )),
    AttributeDecl(Instance(), ConstDecl( Id('c'), IntType(), BinaryOp('+',BinaryOp('+',IntLiteral('0123'),BinaryOp('*',IntLiteral('0xCAFE'),IntLiteral('0b1001'))),IntLiteral('1000')))),
    AttributeDecl(Static(), VarDecl( Id('$c'), IntType(), BinaryOp('/',Id('a'),Id('b'))))
])
]))
        self.assertTrue(TestAST.test(input,expect,305))

    
    def test_primitivetype_attributes5(self):
        input = """
Class Program {
    Val a, b: Float = -1.5, 2.0+3e5;
    Var $a, $b: Float = 1_0.0+2.9e1*3, (1+2)*3;
    Val c: Float = 1_2_3 + 12.34e-1 * 123  + 1_000.0e0;
    Var $c: Float = a / b;
}
"""
        expect = str(Program([
ClassDecl(Id('Program'),[
    AttributeDecl(Instance(), ConstDecl( Id('a'), FloatType(), UnaryOp('-',FloatLiteral('1.5')) )),
    AttributeDecl(Instance(), ConstDecl( Id('b'), FloatType(), BinaryOp('+',FloatLiteral('2.0'),FloatLiteral('3e5')) )),    
    AttributeDecl(Static(), VarDecl( Id('$a'), FloatType(), BinaryOp('+',FloatLiteral('10.0'),BinaryOp('*',FloatLiteral('2.9e1'),IntLiteral('3'))) )),
    AttributeDecl(Static(), VarDecl( Id('$b'), FloatType(), BinaryOp('*',BinaryOp('+',IntLiteral('1'),IntLiteral('2')),IntLiteral('3')) )),
    AttributeDecl(Instance(), ConstDecl( Id('c'), FloatType(), BinaryOp('+',BinaryOp('+',IntLiteral('123'),BinaryOp('*',FloatLiteral('12.34e-1'),IntLiteral('123'))),FloatLiteral('1000.0e0')))),
    AttributeDecl(Static(), VarDecl( Id('$c'), FloatType(), BinaryOp('/',Id('a'),Id('b')))),
])
]))
        self.assertTrue(TestAST.test(input,expect,306))

    
    def test_primitivetype_attributes6(self):
        input = """
Class Program {
    Val a, b: String = "hello" +. "world", "hello" +. "hcmut";
    Var $a: String = a +. b +. "abcde\\n";
}
"""
        expect = str(Program([
ClassDecl(Id('Program'),[
    AttributeDecl(Instance(), ConstDecl( Id('a'), StringType(), BinaryOp('+.',StringLiteral('"hello"'),StringLiteral('"world"')) )),
    AttributeDecl(Instance(), ConstDecl( Id('b'), StringType(), BinaryOp('+.',StringLiteral('"hello"'),StringLiteral('"hcmut"')) )),
    AttributeDecl(Static(), VarDecl( Id('$a'), StringType(), BinaryOp('+.',BinaryOp('+.',Id('a'),Id('b')),StringLiteral('"abcde\\n"')) ))
])
]))
        self.assertTrue(TestAST.test(input,expect,307))

    
    def test_primitivetype_attributes7(self):
        input = """
Class Program {
    Val a, b: Boolean = !True, !False;
    Var $a, $b, $c, $d, $e, $f: Boolean = 1 + 1.0 == 10, 1 + 1.0 != 10, 1 + 1.0 < 10, 1 + 1.0 <= 10, 1 + 1.0 > 10, 1 + 1.0 >= 10;
    Var $g: Boolean = "hello" +. "world" ==. "helloworld";
    Val c, d: Boolean = $a || $b, $c && $d;
    Val xor: Boolean = (!c && d) || (c && !d);
}
"""
        expect = str(Program([
ClassDecl(Id('Program'),[
    AttributeDecl(Instance(), ConstDecl( Id('a'), BoolType(), UnaryOp('!',BooleanLiteral('True')) )),
    AttributeDecl(Instance(), ConstDecl( Id('b'), BoolType(), UnaryOp('!',BooleanLiteral('False')) )),
    AttributeDecl(Static(), VarDecl( Id('$a'), BoolType(), BinaryOp('==',BinaryOp('+',IntLiteral('1'),FloatLiteral('1.0')),IntLiteral('10')) )),
    AttributeDecl(Static(), VarDecl( Id('$b'), BoolType(), BinaryOp('!=',BinaryOp('+',IntLiteral('1'),FloatLiteral('1.0')),IntLiteral('10')) )),
    AttributeDecl(Static(), VarDecl( Id('$c'), BoolType(), BinaryOp('<',BinaryOp('+',IntLiteral('1'),FloatLiteral('1.0')),IntLiteral('10')) )),
    AttributeDecl(Static(), VarDecl( Id('$d'), BoolType(), BinaryOp('<=',BinaryOp('+',IntLiteral('1'),FloatLiteral('1.0')),IntLiteral('10')) )),
    AttributeDecl(Static(), VarDecl( Id('$e'), BoolType(), BinaryOp('>',BinaryOp('+',IntLiteral('1'),FloatLiteral('1.0')),IntLiteral('10')) )),
    AttributeDecl(Static(), VarDecl( Id('$f'), BoolType(), BinaryOp('>=',BinaryOp('+',IntLiteral('1'),FloatLiteral('1.0')),IntLiteral('10')) )),
    AttributeDecl(Static(), VarDecl( Id('$g'), BoolType(), BinaryOp('==.',BinaryOp('+.',StringLiteral('"hello"'),StringLiteral('"world"')),StringLiteral('"helloworld"')) )),
    AttributeDecl(Instance(), ConstDecl( Id('c'), BoolType(), BinaryOp('||',Id('$a'),Id('$b')) )),
    AttributeDecl(Instance(), ConstDecl( Id('d'), BoolType(), BinaryOp('&&',Id('$c'),Id('$d')) )),
    AttributeDecl(Instance(), ConstDecl( Id('xor'), BoolType(), BinaryOp('||',BinaryOp('&&',UnaryOp('!',Id('c')),Id('d')),BinaryOp('&&',Id('c'),UnaryOp('!',Id('d')))) )),
])
]))
        self.assertTrue(TestAST.test(input,expect,308))


    def test_arraytype_attributes1(self):
        input = """
Class Program {
    Var a, $a: Array[Int,5];
    Var b, $b: Array[Float,5];
    Var c: Array[Array[Boolean,5],5];
    Var $c: Array[Array[String,5],5];
}
"""
        expect = str(Program([
ClassDecl(Id('Program'),[
    AttributeDecl(Instance(), VarDecl(Id('a'),ArrayType(5,IntType()))),
    AttributeDecl(Static(), VarDecl(Id('$a'),ArrayType(5,IntType()))),
    AttributeDecl(Instance(), VarDecl(Id('b'),ArrayType(5,FloatType()))),
    AttributeDecl(Static(), VarDecl(Id('$b'),ArrayType(5,FloatType()))),
    AttributeDecl(Instance(), VarDecl(Id('c'),ArrayType(5,ArrayType(5,BoolType())))),
    AttributeDecl(Static(), VarDecl(Id('$c'),ArrayType(5,ArrayType(5,StringType()))))
])
]))
        self.assertTrue(TestAST.test(input,expect,309))


    def test_arraytype_attributes2(self):
        input = """
Class Program {
    Var _: Array[Int,5] = Array(1,2,3,4,2+3);
    Val $_: Array[Array[Int,2],2] = Array(Array(1,2),Array(3,4));
}
"""
        expect = str(Program([
ClassDecl(Id('Program'),[
    AttributeDecl(Instance(), VarDecl(Id('_'), ArrayType(5,IntType()), ArrayLiteral([IntLiteral('1'),IntLiteral('2'),IntLiteral('3'),IntLiteral('4'),BinaryOp('+',IntLiteral('2'),IntLiteral('3'))]))),
    AttributeDecl(Static(), ConstDecl(Id('$_'), ArrayType(2,ArrayType(2,IntType())), ArrayLiteral([ArrayLiteral([IntLiteral('1'),IntLiteral('2')]),ArrayLiteral([IntLiteral('3'),IntLiteral('4')])])))
])
]))
        self.assertTrue(TestAST.test(input,expect,310))


    def test_arraytype_attributes3(self):
        input = """
Class Program {
    Val $_: Array[Array[Int,2],2] = Array(Array(1,2),Array(3,4));
    Val _: Array[Int,4] = Array($_[0][0], $_[0][1], $_[1][0], $_[1][1*1]);
}
"""
        expect = str(Program([
ClassDecl(Id('Program'),[
    AttributeDecl(Static(), ConstDecl(Id('$_'), ArrayType(2,ArrayType(2,IntType())), ArrayLiteral([ArrayLiteral([IntLiteral('1'),IntLiteral('2')]),ArrayLiteral([IntLiteral('3'),IntLiteral('4')])]))),
    AttributeDecl(Instance(), ConstDecl(Id('_'), ArrayType(4,IntType()), ArrayLiteral([ArrayCell(Id('$_'),[IntLiteral('0'),IntLiteral('0')]),
                                                                                       ArrayCell(Id('$_'),[IntLiteral('0'),IntLiteral('1')]),
                                                                                       ArrayCell(Id('$_'),[IntLiteral('1'),IntLiteral('0')]),
                                                                                       ArrayCell(Id('$_'),[IntLiteral('1'),BinaryOp('*',IntLiteral('1'),IntLiteral('1'))])
                                                                                      ])))
])
]))
        self.assertTrue(TestAST.test(input,expect,311))


    def test_arraytype_attributes4(self):
        input = """
Class Program {
    Var x: Int = Array(1,2,3,4,5)[0];
}
"""
        expect = str(Program([
ClassDecl(Id('Program'),[
    AttributeDecl(Instance(), VarDecl(Id('x'), IntType(),
                    ArrayCell(ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3),IntLiteral(4),IntLiteral(5)]),
                                [IntLiteral(0)]) ))
])
]))
        self.assertTrue(TestAST.test(input,expect,312))


    def test_arraytype_attributes5(self):
        input = """
Class Program {
    Val $_: Array[Array[Float,2],2] = Array(Array(1,2),Array(3,4));
    Val _: Array[Float,4] = Array($_[0][0.0], $_[0][1.0], $_[1][0], $_[1][1*1]);
}
"""
        expect = str(Program([
ClassDecl(Id('Program'),[
    AttributeDecl(Static(), ConstDecl(Id('$_'), ArrayType(2,ArrayType(2,FloatType())), ArrayLiteral([ArrayLiteral([IntLiteral('1'),IntLiteral('2')]),ArrayLiteral([IntLiteral('3'),IntLiteral('4')])]))),
    AttributeDecl(Instance(), ConstDecl(Id('_'), ArrayType(4,FloatType()), ArrayLiteral([ArrayCell(Id('$_'),[IntLiteral('0'),FloatLiteral('0.0')]),
                                                                                         ArrayCell(Id('$_'),[IntLiteral('0'),FloatLiteral('1.0')]),
                                                                                         ArrayCell(Id('$_'),[IntLiteral('1'),IntLiteral('0')]),
                                                                                         ArrayCell(Id('$_'),[IntLiteral('1'),BinaryOp('*',IntLiteral('1'),IntLiteral('1'))])
                                                                                        ])))
])
]))
        self.assertTrue(TestAST.test(input,expect,313))


    def test_arraytype_attributes6(self):
        input = """
Class Program {
    Val arr: Array[String,3] = Array("hello", "world", "hello" +. "world");
}
"""
        expect = str(Program([
ClassDecl(Id('Program'),[
    AttributeDecl(Instance(), ConstDecl(Id('arr'), ArrayType(3,StringType()),
                        ArrayLiteral([StringLiteral('"hello"'), StringLiteral('"world"'), BinaryOp('+.', StringLiteral('"hello"'), StringLiteral('"world"'))])))
])
]))
        self.assertTrue(TestAST.test(input,expect,314))
    

    def test_complex_attributes1(self):
        input = """
Class _class {}
Class Program {
    Var x, $x: _class;
    Val y, $y: _class = New _class(), New _class();
}
"""
        expect = str(Program([
ClassDecl(Id('_class'), []),
ClassDecl(Id('Program'), [
    AttributeDecl(Instance(), VarDecl(Id('x'), ClassType(Id('_class')))),
    AttributeDecl(Static(), VarDecl(Id('$x'), ClassType(Id('_class')))),
    AttributeDecl(Instance(), ConstDecl(Id('y'), ClassType(Id('_class')), NewExpr(Id('_class'),[]))),
    AttributeDecl(Static(), ConstDecl(Id('$y'), ClassType(Id('_class')), NewExpr(Id('_class'),[])))
])
]))
        self.assertTrue(TestAST.test(input,expect,315))
    

    def test_complex_attributes2(self):
        input = """
Class _class {
    Var x, $x: Int = 1, 1;
}
Class Program {
    Var obj: _class = New _class();
    Var x: Int = obj.x;
    Var y: Int = _class::$x;
}
"""
        expect = str(Program([
ClassDecl(Id('_class'), [
    AttributeDecl(Instance(), VarDecl(Id('x'), IntType(), IntLiteral(1))),
    AttributeDecl(Static(), VarDecl(Id('$x'), IntType(), IntLiteral(1)))
]),
ClassDecl(Id('Program'), [
    AttributeDecl(Instance(), VarDecl(Id('obj'), ClassType(Id('_class')), NewExpr(Id('_class'),[]))),
    AttributeDecl(Instance(), VarDecl(Id('x'), IntType(), FieldAccess(Id('obj'),Id('x')))),
    AttributeDecl(Instance(), VarDecl(Id('y'), IntType(), FieldAccess(Id('_class'),Id('$x'))))
])
]))
        self.assertTrue(TestAST.test(input,expect,316))
    

    def test_complex_attributes3(self):
        input = """
Class _class {
    Var x, $x: Int = 1, 1;
}
Class Program {
    Val obj: _class = Null;
    Var x: Int = New _class().x;
    Var $x: Int = _class::$x;
}
"""
        expect = str(Program([
ClassDecl(Id('_class'), [
    AttributeDecl(Instance(), VarDecl(Id('x'), IntType(), IntLiteral(1))),
    AttributeDecl(Static(), VarDecl(Id('$x'), IntType(), IntLiteral(1)))
]),
ClassDecl(Id('Program'), [
    AttributeDecl(Instance(), ConstDecl(Id('obj'), ClassType(Id('_class')), NullLiteral())),
    AttributeDecl(Instance(), VarDecl(Id('x'), IntType(), FieldAccess(NewExpr(Id('_class'),[]),Id('x')))),
    AttributeDecl(Static(), VarDecl(Id('$x'), IntType(), FieldAccess(Id('_class'),Id('$x'))))
])
]))
        self.assertTrue(TestAST.test(input,expect,317))
    

    def test_complex_attributes4(self):
        input = """
Class _class {
    Var x: Int = 1;
}
Class Program {
    Var objs: Array[_class,5];
    Var x: Int = objs[4].x;
}
"""
        expect = str(Program([
ClassDecl(Id('_class'), [
    AttributeDecl(Instance(), VarDecl(Id('x'), IntType(), IntLiteral(1))),
]),
ClassDecl(Id('Program'), [
    AttributeDecl(Instance(), VarDecl(Id('objs'), ArrayType(5,ClassType(Id('_class'))))),
    AttributeDecl(Instance(), VarDecl(Id('x'), IntType(), FieldAccess(ArrayCell(Id('objs'),[IntLiteral(4)]),Id('x'))))
])
]))
        self.assertTrue(TestAST.test(input,expect,318))
    

    def test_complex_attributes5(self):
        input = """
Class Program {
    Var x: String = _class::$obj1[1].obj2.obj3[3].obj4[4].obj5;
}
"""
        expect = str(Program([
ClassDecl(Id('Program'), [
    AttributeDecl(Instance(), VarDecl(Id('x'), StringType(),
                                FieldAccess(
                                    ArrayCell(
                                    FieldAccess(
                                        ArrayCell(
                                        FieldAccess(
                                            FieldAccess(
                                                ArrayCell(
                                                FieldAccess(Id('_class'),
                                                Id('$obj1')),[IntLiteral('1')]),
                                            Id('obj2')),
                                        Id('obj3')), [IntLiteral('3')]),
                                    Id('obj4')), [IntLiteral('4')]),
                                Id('obj5'))
    ))
])
]))
        self.assertTrue(TestAST.test(input,expect,319))
    
    def test_empty_methods(self):
        input = """
Class Program {
    main() {}
    $main() {}
    Constructor(a,b:Int; c:Float) {}
    Destructor() {}
}"""
        expect = str(Program([
ClassDecl(Id('Program'),[
    MethodDecl(Static(), Id('main'), [], Block([])),
    MethodDecl(Static(), Id('$main'), [], Block([])),
    MethodDecl(Instance(), Id('Constructor'), [VarDecl(Id('a'),IntType()), VarDecl(Id('b'),IntType()), VarDecl(Id('c'),FloatType())], Block([])),
    MethodDecl(Instance(), Id('Destructor'), [], Block([]))
])
]))
        self.assertTrue(TestAST.test(input,expect,320))
    
    def test_assign_statements1(self):
        input = """
Class Program {
    Var x, $x: Int;
    main() {
        x = 5;
        $x = 10;
    }
}"""
        expect = str(Program([
ClassDecl(Id('Program'),[
    AttributeDecl(Instance(), VarDecl(Id('x'), IntType())),
    AttributeDecl(Static(), VarDecl(Id('$x'), IntType())),
    MethodDecl(Static(), Id('main'), [], Block([
        Assign(Id('x'), IntLiteral('5')),
        Assign(Id('$x'), IntLiteral('10')),
    ]))
])
]))
        self.assertTrue(TestAST.test(input,expect,321))
    
    def test_assign_statements2(self):
        input = """
Class Program {
    Var x, $x: Boolean;
    main() {
        x = True;
        $x = False || x;
    }
}"""
        expect = str(Program([
ClassDecl(Id('Program'),[
    AttributeDecl(Instance(), VarDecl(Id('x'), BoolType())),
    AttributeDecl(Static(), VarDecl(Id('$x'), BoolType())),
    MethodDecl(Static(), Id('main'), [], Block([
        Assign(Id('x'), BooleanLiteral('True')),
        Assign(Id('$x'), BinaryOp('||',BooleanLiteral('False'),Id('x'))),
    ]))
])
]))
        self.assertTrue(TestAST.test(input,expect,322))
    
    def test_assign_statements3(self):
        input = """
Class Program {
    Var x: Array[Int,5];
    main() {
        x[0] = 1;
        x[1] = 2;
        x[2] = 3;
        x[3] = 4;
        x[4] = 5;
    }
}"""
        expect = str(Program([
ClassDecl(Id('Program'),[
    AttributeDecl(Instance(), VarDecl(Id('x'), ArrayType(5,IntType()))),
    MethodDecl(Static(), Id('main'), [], Block([
        Assign(ArrayCell(Id('x'),[IntLiteral('0')]), IntLiteral('1')),
        Assign(ArrayCell(Id('x'),[IntLiteral('1')]), IntLiteral('2')),
        Assign(ArrayCell(Id('x'),[IntLiteral('2')]), IntLiteral('3')),
        Assign(ArrayCell(Id('x'),[IntLiteral('3')]), IntLiteral('4')),
        Assign(ArrayCell(Id('x'),[IntLiteral('4')]), IntLiteral('5'))
    ]))
])
]))
        self.assertTrue(TestAST.test(input,expect,323))

    
    def test_assign_statements4(self):
        input = """
Class _class {
    Var x, $x: Int;
    Constructor() {}
}
Class Program {
    Var obj: _class;
    main() {
        obj = New _class();
        obj.x = 0;
        _class::$x = 0;
    }
}"""
        expect = str(Program([
ClassDecl(Id('_class'),[
    AttributeDecl(Instance(), VarDecl(Id('x'), IntType())),
    AttributeDecl(Static(), VarDecl(Id('$x'), IntType())),
    MethodDecl(Instance(), Id('Constructor'), [], Block([]))
]),
ClassDecl(Id('Program'),[
    AttributeDecl(Instance(), VarDecl(Id('obj'), ClassType(Id('_class')))),
    MethodDecl(Static(), Id('main'), [], Block([
        Assign(Id('obj'), NewExpr(Id('_class'),[])),
        Assign(FieldAccess(Id('obj'),Id('x')), IntLiteral('0')),
        Assign(FieldAccess(Id('_class'),Id('$x')), IntLiteral('0'))
    ]))
])
]))
        self.assertTrue(TestAST.test(input,expect,324))


    def test_assign_statements5(self):
        input = """
Class Program {
    main() {
        _class::$obj1[1].obj2.obj3[3].obj4[4].obj5 = "an object";
    }
}
"""
        expect = str(Program([
ClassDecl(Id('Program'), [
    MethodDecl(Static(), Id('main'), [], Block([
        Assign(FieldAccess(
                    ArrayCell(
                    FieldAccess(
                        ArrayCell(
                        FieldAccess(
                            FieldAccess(
                                ArrayCell(
                                FieldAccess(Id('_class'),
                                Id('$obj1')),[IntLiteral('1')]),
                            Id('obj2')),
                        Id('obj3')), [IntLiteral('3')]),
                    Id('obj4')), [IntLiteral('4')]),
                Id('obj5')),
            StringLiteral('"an object"'))
    ]))
])
]))
        self.assertTrue(TestAST.test(input,expect,325))


    def test_call_statements1(self):
        input = """
Class _class {
    insMethod() {}
    $staMethod() {}
    Constructor() {}
}
Class Program {
    Val obj: _class = New _class();
    main() {
        obj.insMethod();
        _class::$staMethod();
    }
}
"""
        expect = str(Program([
ClassDecl(Id('_class'), [
    MethodDecl(Instance(), Id('insMethod'), [], Block([])),
    MethodDecl(Static(), Id('$staMethod'), [], Block([])),
    MethodDecl(Instance(), Id('Constructor'), [], Block([]))
]),
ClassDecl(Id('Program'), [
    AttributeDecl(Instance(), ConstDecl(Id('obj'), ClassType(Id('_class')), NewExpr(Id('_class'),[]))),
    MethodDecl(Static(), Id('main'), [], Block([
        CallStmt(Id('obj'), Id('insMethod'), []),
        CallStmt(Id('_class'), Id('$staMethod'), [])
    ]))
])
]))
        self.assertTrue(TestAST.test(input,expect,326))


    def test_call_statements2(self):
        input = """
Class _class {
    insMethod() {}
    $staMethod() {}
    Constructor() {}
}
Class Program {
    Var obj: Array[_class,5];
    main() {
        Self.obj[1].insMethod();
        _class::$staMethod();
    }
}
"""
        expect = str(Program([
ClassDecl(Id('_class'), [
    MethodDecl(Instance(), Id('insMethod'), [], Block([])),
    MethodDecl(Static(), Id('$staMethod'), [], Block([])),
    MethodDecl(Instance(), Id('Constructor'), [], Block([]))
]),
ClassDecl(Id('Program'), [
    AttributeDecl(Instance(), VarDecl(Id('obj'), ArrayType(5,ClassType(Id('_class'))))),
    MethodDecl(Static(), Id('main'), [], Block([
        CallStmt(ArrayCell(FieldAccess(SelfLiteral(),Id('obj')),[IntLiteral('1')]), Id('insMethod'), []),
        CallStmt(Id('_class'), Id('$staMethod'), [])
    ]))
])
]))
        self.assertTrue(TestAST.test(input,expect,327))


    def test_call_statements3(self):
        input = """
Class Program {
    main() {
        _class::$obj1[1].obj2.obj3[3].obj4[4].obj5.method(1,2,x);
    }
}
"""
        expect = str(Program([
ClassDecl(Id('Program'), [
    MethodDecl(Static(), Id('main'), [], Block([
        CallStmt(FieldAccess(
                    ArrayCell(
                    FieldAccess(
                        ArrayCell(
                        FieldAccess(
                            FieldAccess(
                                ArrayCell(
                                FieldAccess(Id('_class'),
                                Id('$obj1')),[IntLiteral('1')]),
                            Id('obj2')),
                        Id('obj3')), [IntLiteral('3')]),
                    Id('obj4')), [IntLiteral('4')]),
                Id('obj5')),
            Id('method'), [IntLiteral('1'), IntLiteral('2'), Id('x')])
    ]))
])
]))
        self.assertTrue(TestAST.test(input,expect,328))
    

    def test_return_statements1(self):
        input = """
Class Program {
    main() {
        Return;
        Return 1;
        Return Array(1,2,3);
        Return Null;
    }
}
"""
        expect = str(Program([
ClassDecl(Id('Program'), [
    MethodDecl(Static(), Id('main'), [], Block([
        Return(),
        Return(IntLiteral('1')),
        Return(ArrayLiteral([IntLiteral('1'),IntLiteral('2'),IntLiteral('3')])),
        Return(NullLiteral())
    ]))
])
]))
        self.assertTrue(TestAST.test(input,expect,329))
    

    def test_return_statements2(self):
        input = """
Class Program {
    Constructor() {}
    main() {
        Return;
        Return 1+1*2.0;
        Return Self.main();
        Return New Program();
    }
}
"""
        expect = str(Program([
ClassDecl(Id('Program'), [
    MethodDecl(Instance(), Id('Constructor'), [], Block([])),
    MethodDecl(Static(), Id('main'), [], Block([
        Return(),
        Return(BinaryOp('+',IntLiteral('1'),BinaryOp('*',IntLiteral('1'),FloatLiteral('2.0')))),
        Return(CallExpr(SelfLiteral(),Id('main'),[])),
        Return(NewExpr(Id('Program'),[]))
    ]))
])
]))
        self.assertTrue(TestAST.test(input,expect,330))
    
    def test_blocks(self):
        input = """
Class Program {
    main() {
        {}{}
        {{}}
        {{}{}{{}}}
    }
}        
"""
        expect = str(Program([
ClassDecl(Id('Program'), [
    MethodDecl(Static(), Id('main'), [], Block([
        Block([]), Block([]),
        Block([Block([])]),
        Block([Block([]), Block([]), Block([Block([])])])
    ]))
])
]))
        self.assertTrue(TestAST.test(input,expect,331))
    
    
    def test_declare_statements1(self):
        input = """
Class Program {
    main() {
        Var a, b: Int;
        Val c: Float = 1;
        Var d: Boolean = True && False;
        Var e, f: String;
    }
}
"""
        expect = str(Program([
ClassDecl(Id('Program'), [
    MethodDecl(Static(), Id('main'), [], Block([
        VarDecl(Id('a'), IntType()),
        VarDecl(Id('b'), IntType()),
        ConstDecl(Id('c'), FloatType(), IntLiteral('1')),
        VarDecl(Id('d'), BoolType(), BinaryOp('&&',BooleanLiteral('True'),BooleanLiteral('False'))),
        VarDecl(Id('e'), StringType()),
        VarDecl(Id('f'), StringType())
    ]))
])
]))
        self.assertTrue(TestAST.test(input,expect,332))
    
    
    def test_declare_statements2(self):
        input = """
Class Program {
    main() {
        Var a, b: Int;
        {
            Val c: Float = 1;
            Var d: Boolean = True && False;
        }
        Var e, f: String;
    }
}
"""
        expect = str(Program([
ClassDecl(Id('Program'), [
    MethodDecl(Static(), Id('main'), [], Block([
        VarDecl(Id('a'), IntType()),
        VarDecl(Id('b'), IntType()),
        Block([
            ConstDecl(Id('c'), FloatType(), IntLiteral('1')),
            VarDecl(Id('d'), BoolType(), BinaryOp('&&',BooleanLiteral('True'),BooleanLiteral('False')))
        ]),
        VarDecl(Id('e'), StringType()),
        VarDecl(Id('f'), StringType())
    ]))
])
]))
        self.assertTrue(TestAST.test(input,expect,333))

    
    def test_declare_statements3(self):
        input = """
Class Program {
    main() {
        Val a, b: Int = -1, 2+3;
        Var c, d: Int = 1+2*3, (1+2)*3;
        Val e: Int = 0123 + 0xCAFE * 0b1001  + 1_000;
        Var f: Int = a / b;
    }
}
"""
        expect = str(Program([
ClassDecl(Id('Program'),[
    MethodDecl(Static(), Id('main'), [], Block([
        ConstDecl( Id('a'), IntType(), UnaryOp('-',IntLiteral('1')) ),
        ConstDecl( Id('b'), IntType(), BinaryOp('+',IntLiteral('2'),IntLiteral('3')) ),    
        VarDecl( Id('c'), IntType(), BinaryOp('+',IntLiteral('1'),BinaryOp('*',IntLiteral('2'),IntLiteral('3'))) ),
        VarDecl( Id('d'), IntType(), BinaryOp('*',BinaryOp('+',IntLiteral('1'),IntLiteral('2')),IntLiteral('3')) ),
        ConstDecl( Id('e'), IntType(), BinaryOp('+',BinaryOp('+',IntLiteral('0123'),BinaryOp('*',IntLiteral('0xCAFE'),IntLiteral('0b1001'))),IntLiteral('1000')) ),
        VarDecl( Id('f'), IntType(), BinaryOp('/',Id('a'),Id('b')) )
    ]))
])
]))
        self.assertTrue(TestAST.test(input,expect,334))

    
    def test_declare_statements4(self):
        input = """
Class Program {
    main() {
        Val a, b: Boolean = !True, !False;
        Var c, d, e, f, g, h: Boolean = 1 + 1.0 == 10, 1 + 1.0 != 10, 1 + 1.0 < 10, 1 + 1.0 <= 10, 1 + 1.0 > 10, 1 + 1.0 >= 10;
        Var i: Boolean = "hello" +. "world" ==. "helloworld";
        Val j, k: Boolean = c || d, e && f;
        Val l: Boolean = (!c && d) || (c && !d);
    }
}
"""
        expect = str(Program([
ClassDecl(Id('Program'),[
    MethodDecl(Static(), Id('main'), [], Block([
        ConstDecl( Id('a'), BoolType(), UnaryOp('!',BooleanLiteral('True')) ),
        ConstDecl( Id('b'), BoolType(), UnaryOp('!',BooleanLiteral('False')) ),
        VarDecl( Id('c'), BoolType(), BinaryOp('==',BinaryOp('+',IntLiteral('1'),FloatLiteral('1.0')),IntLiteral('10')) ),
        VarDecl( Id('d'), BoolType(), BinaryOp('!=',BinaryOp('+',IntLiteral('1'),FloatLiteral('1.0')),IntLiteral('10')) ),
        VarDecl( Id('e'), BoolType(), BinaryOp('<',BinaryOp('+',IntLiteral('1'),FloatLiteral('1.0')),IntLiteral('10')) ),
        VarDecl( Id('f'), BoolType(), BinaryOp('<=',BinaryOp('+',IntLiteral('1'),FloatLiteral('1.0')),IntLiteral('10')) ),
        VarDecl( Id('g'), BoolType(), BinaryOp('>',BinaryOp('+',IntLiteral('1'),FloatLiteral('1.0')),IntLiteral('10')) ),
        VarDecl( Id('h'), BoolType(), BinaryOp('>=',BinaryOp('+',IntLiteral('1'),FloatLiteral('1.0')),IntLiteral('10')) ),
        VarDecl( Id('i'), BoolType(), BinaryOp('==.',BinaryOp('+.',StringLiteral('"hello"'),StringLiteral('"world"')),StringLiteral('"helloworld"')) ),
        ConstDecl( Id('j'), BoolType(), BinaryOp('||',Id('c'),Id('d')) ),
        ConstDecl( Id('k'), BoolType(), BinaryOp('&&',Id('e'),Id('f')) ),
        ConstDecl( Id('l'), BoolType(), BinaryOp('||',BinaryOp('&&',UnaryOp('!',Id('c')),Id('d')),BinaryOp('&&',Id('c'),UnaryOp('!',Id('d')))) ),
    ]))
])
]))
        self.assertTrue(TestAST.test(input,expect,335))


    def test_declare_statements5(self):
        input = """
Class Program {
    main() {
        Var a: Array[Int,5];
        Var b: Array[Float,5];
        Var c: Array[Array[Boolean,5],5];
    }
}
"""
        expect = str(Program([
ClassDecl(Id('Program'),[
    MethodDecl(Static(), Id('main'), [], Block([
        VarDecl(Id('a'),ArrayType(5,IntType())),
        VarDecl(Id('b'),ArrayType(5,FloatType())),
        VarDecl(Id('c'),ArrayType(5,ArrayType(5,BoolType())))
    ]))
])
]))
        self.assertTrue(TestAST.test(input,expect,336))
    

    def test_declare_statements6(self):
        input = """
Class _class {
    Var x: Int = 1;
}
Class Program {
    main() {
        Var objs: Array[_class,5];
        Var x: Int = objs[4].x;
    }
}
"""
        expect = str(Program([
ClassDecl(Id('_class'), [
    AttributeDecl(Instance(), VarDecl(Id('x'), IntType(), IntLiteral(1))),
]),
ClassDecl(Id('Program'), [
    MethodDecl(Static(), Id('main'), [], Block([
        VarDecl(Id('objs'), ArrayType(5,ClassType(Id('_class')))),
        VarDecl(Id('x'), IntType(), FieldAccess(ArrayCell(Id('objs'),[IntLiteral(4)]),Id('x')))
    ]))
])
]))
        self.assertTrue(TestAST.test(input,expect,337))
    

    def test_declare_statements7(self):
        input = """
Class Program {
    main() {
        Var x: String = _class::$obj1[1].obj2.obj3[3].obj4[4].obj5;
    }
}
"""
        expect = str(Program([
ClassDecl(Id('Program'), [
    MethodDecl(Static(), Id('main'), [], Block([
        VarDecl(Id('x'), StringType(),
            FieldAccess(
                ArrayCell(
                FieldAccess(
                    ArrayCell(
                    FieldAccess(
                        FieldAccess(
                            ArrayCell(
                            FieldAccess(Id('_class'),
                            Id('$obj1')),[IntLiteral('1')]),
                        Id('obj2')),
                    Id('obj3')), [IntLiteral('3')]),
                Id('obj4')), [IntLiteral('4')]),
            Id('obj5')
        ))
    ]))
])
]))
        self.assertTrue(TestAST.test(input,expect,338))
    
    
    def test_if_statements1(self):
        input = """
Class Program {
    main() {
        If (True) {}
    }
}
"""
        expect = str(Program([
ClassDecl(Id('Program'), [
    MethodDecl(Static(), Id('main'), [], Block([
        If(BooleanLiteral('True'), Block([]))
    ]))
])
]))
        self.assertTrue(TestAST.test(input,expect,339))
    
    
    def test_if_statements2(self):
        input = """
Class Program {
    main() {
        If (True) {}
        Else {}
    }
}
"""
        expect = str(Program([
ClassDecl(Id('Program'), [
    MethodDecl(Static(), Id('main'), [], Block([
        If(BooleanLiteral('True'), Block([]),
        Block([]))
    ]))
])
]))
        self.assertTrue(TestAST.test(input,expect,340))
    
    
    def test_if_statements3(self):
        input = """
Class Program {
    main() {
        If (True) {}
        Elseif (False) {}
        Else {}
    }
}
"""
        expect = str(Program([
ClassDecl(Id('Program'), [
    MethodDecl(Static(), Id('main'), [], Block([
        If(BooleanLiteral('True'), Block([]),
        If(BooleanLiteral('False'), Block([]),
        Block([])))
    ]))
])
]))
        self.assertTrue(TestAST.test(input,expect,341))
    
    
    def test_if_statements4(self):
        input = """
Class Program {
    main() {
        If (True) {}
        Elseif (False) {}
        Elseif (1+1==2) {}
        Else {}
    }
}
"""
        expect = str(Program([
ClassDecl(Id('Program'), [
    MethodDecl(Static(), Id('main'), [], Block([
        If(BooleanLiteral('True'), Block([]),
        If(BooleanLiteral('False'), Block([]),
        If(BinaryOp('==',BinaryOp('+',IntLiteral('1'),IntLiteral('1')),IntLiteral('2')), Block([]),
        Block([]))))
    ]))
])
]))
        self.assertTrue(TestAST.test(input,expect,342))
    
    
    def test_if_statements5(self):
        input = """
Class Program {
    main() {
        If(True) {}
        Elseif(False) {}
        Elseif(1+1==2) {
            If(True) {}
            Else {}
        }
        Else {}
    }
}
"""
        expect = str(Program([
ClassDecl(Id('Program'), [
    MethodDecl(Static(), Id('main'), [], Block([
        If(BooleanLiteral('True'), Block([]),
        If(BooleanLiteral('False'), Block([]),
        If(BinaryOp('==',BinaryOp('+',IntLiteral('1'),IntLiteral('1')),IntLiteral('2')), Block([
            If(BooleanLiteral('True'), Block([]),
            Block([]))
        ]),
        Block([]))))
    ]))
])
]))
        self.assertTrue(TestAST.test(input,expect,343))
    
    
    def test_if_statements5(self):
        input = """
Class Program {
    $isOdd(x:Int) {
        If (x % 2 == 1) {
            Return True;
        }
        Return False;
    }
    main() {
        Var result: Boolean = Program::$isOdd(0xCAFE);
    }
}
"""
        expect = str(Program([
ClassDecl(Id('Program'), [
    MethodDecl(Static(), Id('$isOdd'), [VarDecl(Id('x'),IntType())], Block([
        If(BinaryOp('==',BinaryOp('%',Id('x'),IntLiteral('2')),IntLiteral('1')), Block([
            Return(BooleanLiteral('True'))
        ])),
        Return(BooleanLiteral('False'))
    ])),
    MethodDecl(Static(), Id('main'), [], Block([
        VarDecl(Id('result'), BoolType(), CallExpr(Id('Program'),Id('$isOdd'),[IntLiteral('0xCAFE')]))
    ]))
])
]))
        self.assertTrue(TestAST.test(input,expect,343))
    
    
    def test_main_function(self):
        input = """
Class _ {
    main() {}
}
Class Program {
    main() {}
    main(x:Int) {}
}
"""
        expect = str(Program([
ClassDecl(Id('_'), [
    MethodDecl(Instance(), Id('main'), [], Block([]))
]),
ClassDecl(Id('Program'), [
    MethodDecl(Static(), Id('main'), [], Block([])),
    MethodDecl(Instance(), Id('main'), [VarDecl(Id('x'),IntType())], Block([]))
])
]))
        self.assertTrue(TestAST.test(input,expect,344))
    
    
    def test_for_statements1(self):
        input = """
Class Program {
    main() {
        Foreach (i In 1 .. 100) {}
    }
}
"""
        expect = str(Program([
ClassDecl(Id('Program'), [
    MethodDecl(Static(), Id('main'), [], Block([
        For(Id('i'), IntLiteral('1'), IntLiteral('100'), Block([]))
    ]))
])
]))
        self.assertTrue(TestAST.test(input,expect,345))
    
    
    def test_for_statements2(self):
        input = """
Class Program {
    main() {
        Foreach (i In 1 .. 100) {
            Break;
            Continue;
            Return;
        }
    }
}
"""
        expect = str(Program([
ClassDecl(Id('Program'), [
    MethodDecl(Static(), Id('main'), [], Block([
        For(Id('i'), IntLiteral('1'), IntLiteral('100'), Block([
            Break(),
            Continue(),
            Return()
        ]))
    ]))
])
]))
        self.assertTrue(TestAST.test(input,expect,346))
    
    
    def test_for_statements3(self):
        input = """
Class Program {
    main() {
        Foreach (i In 1 .. 100 By 0*1-0) {
            Break;
            Continue;
            Return;
        }
    }
}
"""
        expect = str(Program([
ClassDecl(Id('Program'), [
    MethodDecl(Static(), Id('main'), [], Block([
        For(Id('i'), IntLiteral('1'), IntLiteral('100'), Block([
            Break(),
            Continue(),
            Return()
        ]), BinaryOp('-',BinaryOp('*',IntLiteral('0'),IntLiteral('1')),IntLiteral('0')))
    ]))
])
]))
        self.assertTrue(TestAST.test(input,expect,347))
    
    
    def test_for_statements4(self):
        input = """
Class Program {
    main() {
        Foreach (i In 1 .. 100) {
            Foreach(j In 1 .. 100) {}
        }
    }
}
"""
        expect = str(Program([
ClassDecl(Id('Program'), [
    MethodDecl(Static(), Id('main'), [], Block([
        For(Id('i'), IntLiteral('1'), IntLiteral('100'), Block([
            For(Id('j'), IntLiteral('1'), IntLiteral('100'), Block([]))
        ]))
    ]))
])
]))
        self.assertTrue(TestAST.test(input,expect,348))
    
    
    def test_for_statements5(self):
        input = """
Class Program {
    main() {
        Foreach (i In 1 .. 100) {
            If (True) {
                Var j: Int;
                Continue;
                Break;
            }
        }
    }
}
"""
        expect = str(Program([
ClassDecl(Id('Program'), [
    MethodDecl(Static(), Id('main'), [], Block([
        For(Id('i'), IntLiteral('1'), IntLiteral('100'), Block([
            If(BooleanLiteral('True'), Block([
                VarDecl(Id('j'), IntType()),
                Continue(),
                Break()
            ]))
        ]))
    ]))
])
]))
        self.assertTrue(TestAST.test(input,expect,349))