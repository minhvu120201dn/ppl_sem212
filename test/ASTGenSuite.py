from array import ArrayType
from msilib.schema import Binary
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
    MethodDecl(Instance(), Id('main'), [], []),
    MethodDecl(Static(), Id('$main'), [], []),
    MethodDecl(Instance(), Id('Constructor'), [VarDecl(Id('a'),IntType()), VarDecl(Id('b'),IntType()), VarDecl(Id('c'),FloatType())], []),
    MethodDecl(Instance(), Id('Destructor'), [], [])
])
]))
        self.assertTrue(TestAST.test(input,expect,320))