from array import ArrayType
from ast import BinOp
from msilib.schema import Binary, Class
import unittest
from attr import Attribute

from pandas import BooleanDtype
from TestUtils import TestAST
from AST import *
from main.d96.astgen.AST import ArrayCell, ArrayLiteral, ClassType, FieldAccess, NewExpr, NullLiteral
from main.d96.utils.AST import AST, AttributeDecl, BinaryOp, BoolType, BooleanLiteral, ClassDecl, ConstDecl,  FloatLiteral, FloatType, Id, Instance, IntLiteral, IntType, Program, Static, StringLiteral, StringType, UnaryOp, VarDecl
 
class ASTGenSuite(unittest.TestCase):

    def test_complex_programsimple_program1(self):
        input = ""
        expect = str(Program([]))
        self.assertTrue(TestAST.test(input,expect,300))

    def test_complex_programsimple_program2(self):
        input = """
Class class1{}
Class class2{}
Class class3 : parent{}
"""
        expect = str(Program([ClassDecl(Id('class1'),[]),
                              ClassDecl(Id('class2'),[]),
                              ClassDecl(Id('class3'),[],Id('parent'))]))
        self.assertTrue(TestAST.test(input,expect,301))


    def test_complex_programprimitivetype_attributes1(self):
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


    def test_complex_programprimitivetype_attributes2(self):
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


    def test_complex_programprimitivetype_attributes3(self):
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
    AttributeDecl(Instance(), VarDecl( Id('b'), IntType(), IntLiteral('51966') )),
    AttributeDecl(Static(), ConstDecl( Id('$c'), FloatType(), FloatLiteral('3.141592653589') )),
    AttributeDecl(Static(), VarDecl( Id('$d'), BoolType(), BooleanLiteral('True') )),
    AttributeDecl(Instance(), ConstDecl( Id('e'), StringType(), StringLiteral('first') )),
    AttributeDecl(Static(), ConstDecl( Id('$f'), StringType(), StringLiteral('second') ))
])
]))
        self.assertTrue(TestAST.test(input,expect,304))

    
    def test_complex_programprimitivetype_attributes4(self):
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
    AttributeDecl(Instance(), ConstDecl( Id('c'), IntType(), BinaryOp('+',BinaryOp('+',IntLiteral('83'),BinaryOp('*',IntLiteral('51966'),IntLiteral('9'))),IntLiteral('1000')))),
    AttributeDecl(Static(), VarDecl( Id('$c'), IntType(), BinaryOp('/',Id('a'),Id('b'))))
])
]))
        self.assertTrue(TestAST.test(input,expect,305))

    
#     def test_complex_programprimitivetype_attributes5(self):
#         input = """
# Class Program {
#     Val a, b: Float = -1.5, 2.0+3e5;
#     Var $a, $b: Float = 1_0.0+2.9e1*3, (1+2)*3;
#     Val c: Float = 1_2_3 + 12.34e-1 * 123  + 1_000.0e0;
#     Var $c: Float = a / b;
# }
# """
#         expect = str(Program([
# ClassDecl(Id('Program'),[
#     AttributeDecl(Instance(), ConstDecl( Id('a'), FloatType(), UnaryOp('-',FloatLiteral('1.5')) )),
#     AttributeDecl(Instance(), ConstDecl( Id('b'), FloatType(), BinaryOp('+',FloatLiteral('2.0'),FloatLiteral('3e5')) )),    
#     AttributeDecl(Static(), VarDecl( Id('$a'), FloatType(), BinaryOp('+',FloatLiteral('10.0'),BinaryOp('*',FloatLiteral('2.9e1'),IntLiteral('3'))) )),
#     AttributeDecl(Static(), VarDecl( Id('$b'), FloatType(), BinaryOp('*',BinaryOp('+',IntLiteral('1'),IntLiteral('2')),IntLiteral('3')) )),
#     AttributeDecl(Instance(), ConstDecl( Id('c'), FloatType(), BinaryOp('+',BinaryOp('+',IntLiteral('123'),BinaryOp('*',FloatLiteral('12.34e-1'),IntLiteral('123'))),FloatLiteral('1000.0e0')))),
#     AttributeDecl(Static(), VarDecl( Id('$c'), FloatType(), BinaryOp('/',Id('a'),Id('b')))),
# ])
# ]))
#         self.assertTrue(TestAST.test(input,expect,306))

    
    def test_complex_programprimitivetype_attributes6(self):
        input = """
Class Program {
    Val a, b: String = "hello" +. "world", "hello" +. "hcmut";
    Var $a: String = a +. b +. "abcde\\n";
}
"""
        expect = str(Program([
ClassDecl(Id('Program'),[
    AttributeDecl(Instance(), ConstDecl( Id('a'), StringType(), BinaryOp('+.',StringLiteral('hello'),StringLiteral('world')) )),
    AttributeDecl(Instance(), ConstDecl( Id('b'), StringType(), BinaryOp('+.',StringLiteral('hello'),StringLiteral('hcmut')) )),
    AttributeDecl(Static(), VarDecl( Id('$a'), StringType(), BinaryOp('+.',BinaryOp('+.',Id('a'),Id('b')),StringLiteral('abcde\\n')) ))
])
]))
        self.assertTrue(TestAST.test(input,expect,307))

    
    def test_complex_programprimitivetype_attributes7(self):
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
    AttributeDecl(Static(), VarDecl( Id('$g'), BoolType(), BinaryOp('==.',BinaryOp('+.',StringLiteral('hello'),StringLiteral('world')),StringLiteral('helloworld')) )),
    AttributeDecl(Instance(), ConstDecl( Id('c'), BoolType(), BinaryOp('||',Id('$a'),Id('$b')) )),
    AttributeDecl(Instance(), ConstDecl( Id('d'), BoolType(), BinaryOp('&&',Id('$c'),Id('$d')) )),
    AttributeDecl(Instance(), ConstDecl( Id('xor'), BoolType(), BinaryOp('||',BinaryOp('&&',UnaryOp('!',Id('c')),Id('d')),BinaryOp('&&',Id('c'),UnaryOp('!',Id('d')))) )),
])
]))
        self.assertTrue(TestAST.test(input,expect,308))


    def test_complex_programarraytype_attributes1(self):
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


    def test_complex_programarraytype_attributes2(self):
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


    def test_complex_programarraytype_attributes3(self):
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


    def test_complex_programarraytype_attributes4(self):
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


    def test_complex_programarraytype_attributes5(self):
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


    def test_complex_programarraytype_attributes6(self):
        input = """
Class Program {
    Val arr: Array[String,3] = Array("hello", "world", "hello" +. "world");
}
"""
        expect = str(Program([
ClassDecl(Id('Program'),[
    AttributeDecl(Instance(), ConstDecl(Id('arr'), ArrayType(3,StringType()),
                        ArrayLiteral([StringLiteral('hello'), StringLiteral('world'), BinaryOp('+.', StringLiteral('hello'), StringLiteral('world'))])))
])
]))
        self.assertTrue(TestAST.test(input,expect,314))
    

    def test_complex_programcomplex_attributes1(self):
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
    AttributeDecl(Instance(), VarDecl(Id('x'), ClassType(Id('_class')), NullLiteral())),
    AttributeDecl(Static(), VarDecl(Id('$x'), ClassType(Id('_class')), NullLiteral())),
    AttributeDecl(Instance(), ConstDecl(Id('y'), ClassType(Id('_class')), NewExpr(Id('_class'),[]))),
    AttributeDecl(Static(), ConstDecl(Id('$y'), ClassType(Id('_class')), NewExpr(Id('_class'),[])))
])
]))
        self.assertTrue(TestAST.test(input,expect,315))
    

    def test_complex_programcomplex_attributes2(self):
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
    

    def test_complex_programcomplex_attributes3(self):
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
    AttributeDecl(Instance(), VarDecl(Id('x'), IntType(), IntLiteral('1'))),
    AttributeDecl(Static(), VarDecl(Id('$x'), IntType(), IntLiteral('1')))
]),
ClassDecl(Id('Program'), [
    AttributeDecl(Instance(), ConstDecl(Id('obj'), ClassType(Id('_class')), NullLiteral())),
    AttributeDecl(Instance(), VarDecl(Id('x'), IntType(), FieldAccess(NewExpr(Id('_class'),[]),Id('x')))),
    AttributeDecl(Static(), VarDecl(Id('$x'), IntType(), FieldAccess(Id('_class'),Id('$x'))))
])
]))
        self.assertTrue(TestAST.test(input,expect,-1))
    

    def test_complex_programcomplex_attributes4(self):
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
    

    def test_complex_programcomplex_attributes5(self):
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
    
    def test_complex_programempty_methods(self):
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
    
    def test_complex_programassign_statements1(self):
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
    
    def test_complex_programassign_statements2(self):
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
    
    def test_complex_programassign_statements3(self):
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

    
    def test_complex_programassign_statements4(self):
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
    AttributeDecl(Instance(), VarDecl(Id('obj'), ClassType(Id('_class')), NullLiteral())),
    MethodDecl(Static(), Id('main'), [], Block([
        Assign(Id('obj'), NewExpr(Id('_class'),[])),
        Assign(FieldAccess(Id('obj'),Id('x')), IntLiteral('0')),
        Assign(FieldAccess(Id('_class'),Id('$x')), IntLiteral('0'))
    ]))
])
]))
        self.assertTrue(TestAST.test(input,expect,324))


    def test_complex_programassign_statements5(self):
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
            StringLiteral('an object'))
    ]))
])
]))
        self.assertTrue(TestAST.test(input,expect,325))


    def test_complex_programcall_statements1(self):
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


    def test_complex_programcall_statements2(self):
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


    def test_complex_programcall_statements3(self):
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
    

    def test_complex_programreturn_statements1(self):
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
    

    def test_complex_programreturn_statements2(self):
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
    
    def test_complex_programblocks(self):
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
    
    
    def test_complex_programdeclare_statements1(self):
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
    
    
    def test_complex_programdeclare_statements2(self):
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

    
    def test_complex_programdeclare_statements3(self):
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
        ConstDecl( Id('e'), IntType(), BinaryOp('+',BinaryOp('+',IntLiteral('83'),BinaryOp('*',IntLiteral('51966'),IntLiteral('9'))),IntLiteral('1000')) ),
        VarDecl( Id('f'), IntType(), BinaryOp('/',Id('a'),Id('b')) )
    ]))
])
]))
        self.assertTrue(TestAST.test(input,expect,334))

    
    def test_complex_programdeclare_statements4(self):
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
        VarDecl( Id('i'), BoolType(), BinaryOp('==.',BinaryOp('+.',StringLiteral('hello'),StringLiteral('world')),StringLiteral('helloworld')) ),
        ConstDecl( Id('j'), BoolType(), BinaryOp('||',Id('c'),Id('d')) ),
        ConstDecl( Id('k'), BoolType(), BinaryOp('&&',Id('e'),Id('f')) ),
        ConstDecl( Id('l'), BoolType(), BinaryOp('||',BinaryOp('&&',UnaryOp('!',Id('c')),Id('d')),BinaryOp('&&',Id('c'),UnaryOp('!',Id('d')))) ),
    ]))
])
]))
        self.assertTrue(TestAST.test(input,expect,335))


    def test_complex_programdeclare_statements5(self):
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
    

    def test_complex_programdeclare_statements6(self):
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
    

    def test_complex_programdeclare_statements7(self):
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
    
    
    def test_complex_programif_statements1(self):
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
    
    
    def test_complex_programif_statements2(self):
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
    
    
    def test_complex_programif_statements3(self):
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
    
    
    def test_complex_programif_statements4(self):
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
    
    
    def test_complex_programif_statements5(self):
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
    
    
    def test_complex_programif_statements6(self):
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
        VarDecl(Id('result'), BoolType(), CallExpr(Id('Program'),Id('$isOdd'),[IntLiteral('51966')]))
    ]))
])
]))
        self.assertTrue(TestAST.test(input,expect,354))
    
    
    def test_complex_programmain_function(self):
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
    
    
    def test_complex_programfor_statements1(self):
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
    
    
    def test_complex_programfor_statements2(self):
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
    
    
    def test_complex_programfor_statements3(self):
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
    
    
    def test_complex_programfor_statements4(self):
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
    
    
    def test_complex_programfor_statements5(self):
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
    

    def test_complex_programcomplex_program1(self):
        input = """
Class Shape {
    Var area: Float;
}

Class Rectangle : Shape {
    Var height, width: Float;
}

Class Circle : Shape {
    Var radius: Float;
    Val $pi: Float = 3.141592653589;
}
"""
        expect = str(Program([
ClassDecl(Id('Shape'), [
    AttributeDecl(Instance(), VarDecl(Id('area'), FloatType()))
]),
ClassDecl(Id('Rectangle'), [
    AttributeDecl(Instance(), VarDecl(Id('height'), FloatType())),
    AttributeDecl(Instance(), VarDecl(Id('width'), FloatType()))
], Id('Shape')),
ClassDecl(Id('Circle'), [
    AttributeDecl(Instance(), VarDecl(Id('radius'), FloatType())),
    AttributeDecl(Static(), ConstDecl(Id('$pi'), FloatType(), FloatLiteral('3.141592653589')))
], Id('Shape'))
]))
        self.assertTrue(TestAST.test(input,expect,350))
    

    def test_complex_programcomplex_program2(self):
        input = """
Class Shape {
    Var area: Float;
}

Class Rectangle : Shape {
    Var height, width: Float;
    Constructor(h,w:Float) {
        Self.height = h;
        Self.width = w;
        Self.area = h*w;
    }
}

Class Circle : Shape {
    Var radius: Float;
    Val $pi: Float = 3.141592653589;
    Constructor(r:Float) {
        Self.radius = r;
        Self.area = $pi*r*r;
    }
}
"""
        expect = str(Program([
ClassDecl(Id('Shape'), [
    AttributeDecl(Instance(), VarDecl(Id('area'), FloatType()))
]),
ClassDecl(Id('Rectangle'), [
    AttributeDecl(Instance(), VarDecl(Id('height'), FloatType())),
    AttributeDecl(Instance(), VarDecl(Id('width'), FloatType())),
    MethodDecl(Instance(), Id('Constructor'), [VarDecl(Id('h'),FloatType()),VarDecl(Id('w'),FloatType())], Block([
        Assign(FieldAccess(SelfLiteral(),Id('height')), Id('h')),
        Assign(FieldAccess(SelfLiteral(),Id('width')), Id('w')),
        Assign(FieldAccess(SelfLiteral(),Id('area')), BinaryOp('*',Id('h'),Id('w')))
    ]))
], Id('Shape')),
ClassDecl(Id('Circle'), [
    AttributeDecl(Instance(), VarDecl(Id('radius'), FloatType())),
    AttributeDecl(Static(), ConstDecl(Id('$pi'), FloatType(), FloatLiteral('3.141592653589'))),
    MethodDecl(Instance(), Id('Constructor'), [VarDecl(Id('r'),FloatType())], Block([
        Assign(FieldAccess(SelfLiteral(),Id('radius')), Id('r')),
        Assign(FieldAccess(SelfLiteral(),Id('area')), BinaryOp('*',BinaryOp('*',Id('$pi'),Id('r')),Id('r')))
    ]))
], Id('Shape'))
]))
        self.assertTrue(TestAST.test(input,expect,351))


    def test_complex_programcomplex_program3(self):
        input = """
Class Math {
    $fact(n:Int) {
        If (n < 0) {
            Return;
        }
        Elseif (n == 0) {
            Return 1;
        }
        Else {
            Return Math::$fact(n-1) * n;
        }
    }
}
"""
        expect = str(Program([
ClassDecl(Id('Math'), [
    MethodDecl(Static(), Id('$fact'), [VarDecl(Id('n'),IntType())], Block([
        If(BinaryOp('<',Id('n'),IntLiteral('0')), Block([
            Return()
        ]),
        If(BinaryOp('==',Id('n'),IntLiteral('0')), Block([
            Return(IntLiteral('1'))
        ]),
        Block([
            Return(BinaryOp('*',CallExpr(Id('Math'),Id('$fact'),[BinaryOp('-',Id('n'),IntLiteral('1'))]),Id('n')))
        ])
        ))
    ]))
])
]))
        self.assertTrue(TestAST.test(input,expect,352))


    def test_complex_programcomplex_program4(self):
        input = """
Class Math {
    $fact(n:Int) {
        If (n < 0) {
            Return;
        }
        Elseif (n == 0) {
            Return 1;
        }
        Else {
            Var fact: Int = 1;
            Foreach (i In 1 .. n) {
                fact = fact * i;
            }
            Return fact;
        }
    }
}
"""
        expect = str(Program([
ClassDecl(Id('Math'), [
    MethodDecl(Static(), Id('$fact'), [VarDecl(Id('n'),IntType())], Block([
        If(BinaryOp('<',Id('n'),IntLiteral('0')), Block([
            Return()
        ]),
        If(BinaryOp('==',Id('n'),IntLiteral('0')), Block([
            Return(IntLiteral('1'))
        ]),
        Block([
            VarDecl(Id('fact'), IntType(), IntLiteral('1')),
            For(Id('i'), IntLiteral('1'), Id('n'), Block([
                Assign(Id('fact'), BinaryOp('*',Id('fact'),Id('i')))
            ])),
            Return(Id('fact'))
        ])
        ))
    ]))
])
]))
        self.assertTrue(TestAST.test(input,expect,306))


    def test_complex_programcomplex_program5(self):
        input = """
Class Math {
    $fact(n:Int) {
        If (n < 0) {
            Return;
        }
        Elseif (n == 0) {
            Return 1;
        }
        Else {
            Var fact: Int = 1;
            Foreach (i In 1 .. n) {
                fact = fact * i;
            }
            Return fact;
        }
    }
    $P(n,k:Int) {
        Return Math::$fact(n) / Math::$fact(k);
    }
    $C(n,k:Int) {
        Return Math::$fact(n) / (Math::$fact(k) * Math::$fact(n-k));
    }
}
"""
        expect = str(Program([
ClassDecl(Id('Math'), [
    MethodDecl(Static(), Id('$fact'), [VarDecl(Id('n'),IntType())], Block([
        If(BinaryOp('<',Id('n'),IntLiteral('0')), Block([
            Return()
        ]),
        If(BinaryOp('==',Id('n'),IntLiteral('0')), Block([
            Return(IntLiteral('1'))
        ]),
        Block([
            VarDecl(Id('fact'), IntType(), IntLiteral('1')),
            For(Id('i'), IntLiteral('1'), Id('n'), Block([
                Assign(Id('fact'), BinaryOp('*',Id('fact'),Id('i')))
            ])),
            Return(Id('fact'))
        ])
        ))
    ])),
    MethodDecl(Static(), Id('$P'), [VarDecl(Id('n'),IntType()),VarDecl(Id('k'),IntType())], Block([
        Return(BinaryOp('/',CallExpr(Id('Math'),Id('$fact'),[Id('n')]),CallExpr(Id('Math'),Id('$fact'),[Id('k')])))
    ])),
    MethodDecl(Static(), Id('$C'), [VarDecl(Id('n'),IntType()),VarDecl(Id('k'),IntType())], Block([
        Return(BinaryOp('/',CallExpr(Id('Math'),Id('$fact'),[Id('n')]),
                            BinaryOp('*',CallExpr(Id('Math'),Id('$fact'),[Id('k')]),CallExpr(Id('Math'),Id('$fact'),[BinaryOp('-',Id('n'),Id('k'))]))
                       ))
    ]))
])
]))
        self.assertTrue(TestAST.test(input,expect,355))
    

    def test_complex_programcomplex_program6(self):
        input = """
Class Math {
    $max(arr:Array[Int,1000000]; n:Int) {
        Var m: Int = arr[0];
        Foreach (i In 1 .. n) {
            If (arr[i] > m) {
                m = arr[i];
            }
        }
        Return m;
    }
}
"""
        expect = str(Program([
ClassDecl(Id('Math'), [
    MethodDecl(Static(), Id('$max'), [VarDecl(Id('arr'),ArrayType(1000000,IntType())), VarDecl(Id('n'),IntType())], Block([
        VarDecl(Id('m'), IntType(), ArrayCell(Id('arr'),[IntLiteral('0')])),
        For(Id('i'), IntLiteral('1'), Id('n'), Block([
            If(BinaryOp('>',ArrayCell(Id('arr'),[Id('i')]),Id('m')), Block([
                Assign(Id('m'), ArrayCell(Id('arr'),[Id('i')]))
            ]))
        ])),
        Return(Id('m'))
    ]))
])
]))
        self.assertTrue(TestAST.test(input,expect,355))



    def test_complex_program6(self):
        input = '''Class _6h:_{Val RLt_:_Y;}Class L:__D{Val $__4:Int ;}Class W{Destructor (){Break ;Break ;Continue ;} }Class C{Var $5:String ;Constructor (_4_9,_:Boolean ;q:String ;J:String ;m,_,_,d3,T0X_:_){} }Class w:_{}'''
        expect = '''Program([ClassDecl(Id(_6h),Id(_),[AttributeDecl(Instance,ConstDecl(Id(RLt_),ClassType(Id(_Y)),None))]),ClassDecl(Id(L),Id(__D),[AttributeDecl(Static,ConstDecl(Id($__4),IntType,None))]),ClassDecl(Id(W),[MethodDecl(Id(Destructor),Instance,[],Block([Break,Break,Continue]))]),ClassDecl(Id(C),[AttributeDecl(Static,VarDecl(Id($5),StringType)),MethodDecl(Id(Constructor),Instance,[param(Id(_4_9),BoolType),param(Id(_),BoolType),param(Id(q),StringType),param(Id(J),StringType),param(Id(m),ClassType(Id(_))),param(Id(_),ClassType(Id(_))),param(Id(_),ClassType(Id(_))),param(Id(d3),ClassType(Id(_))),param(Id(T0X_),ClassType(Id(_)))],Block([]))]),ClassDecl(Id(w),Id(_),[])])'''
        self.assertTrue(TestAST.test(input, expect, 356))

    def test_complex_program7(self):
        input = '''Class I{}Class a:_{Constructor (F,f,_,u_0:Array [Int ,050];s:_A;N:_Y;e_24X,__,__,__,z,w:Array [Array [Boolean ,0b1100100],0b1];_,s__2:Array [Array [String ,0B1],0x2D];__,_:Array [Array [Float ,21_1_59],44];_:Array [Int ,0B10101]){} }Class _:f_b_2I{Var $5:Array [Array [String ,0X27],0X27];Val F3:_;}'''
        expect = '''Program([ClassDecl(Id(I),[]),ClassDecl(Id(a),Id(_),[MethodDecl(Id(Constructor),Instance,[param(Id(F),ArrayType(40,IntType)),param(Id(f),ArrayType(40,IntType)),param(Id(_),ArrayType(40,IntType)),param(Id(u_0),ArrayType(40,IntType)),param(Id(s),ClassType(Id(_A))),param(Id(N),ClassType(Id(_Y))),param(Id(e_24X),ArrayType(1,ArrayType(100,BoolType))),param(Id(__),ArrayType(1,ArrayType(100,BoolType))),param(Id(__),ArrayType(1,ArrayType(100,BoolType))),param(Id(__),ArrayType(1,ArrayType(100,BoolType))),param(Id(z),ArrayType(1,ArrayType(100,BoolType))),param(Id(w),ArrayType(1,ArrayType(100,BoolType))),param(Id(_),ArrayType(45,ArrayType(1,StringType))),param(Id(s__2),ArrayType(45,ArrayType(1,StringType))),param(Id(__),ArrayType(44,ArrayType(21159,FloatType))),param(Id(_),ArrayType(44,ArrayType(21159,FloatType))),param(Id(_),ArrayType(21,IntType))],Block([]))]),ClassDecl(Id(_),Id(f_b_2I),[AttributeDecl(Static,VarDecl(Id($5),ArrayType(39,ArrayType(39,StringType)))),AttributeDecl(Instance,ConstDecl(Id(F3),ClassType(Id(_)),None))])])'''
        self.assertTrue(TestAST.test(input, expect, 357))

    def test_complex_program8(self):
        input = '''Class __:h_{}Class _4{Constructor (){}$7_(){} }Class t:K_{}Class i{Constructor (d,yY4:_){}Val $o,g_4,_8:_;}Class M4{V(){Break ;}Val $3jqD1,$6:_;}Class _{}Class _{z(){Break ;Return ;} }'''
        expect = '''Program([ClassDecl(Id(__),Id(h_),[]),ClassDecl(Id(_4),[MethodDecl(Id(Constructor),Instance,[],Block([])),MethodDecl(Id($7_),Static,[],Block([]))]),ClassDecl(Id(t),Id(K_),[]),ClassDecl(Id(i),[MethodDecl(Id(Constructor),Instance,[param(Id(d),ClassType(Id(_))),param(Id(yY4),ClassType(Id(_)))],Block([])),AttributeDecl(Static,ConstDecl(Id($o),ClassType(Id(_)),None)),AttributeDecl(Instance,ConstDecl(Id(g_4),ClassType(Id(_)),None)),AttributeDecl(Instance,ConstDecl(Id(_8),ClassType(Id(_)),None))]),ClassDecl(Id(M4),[MethodDecl(Id(V),Instance,[],Block([Break])),AttributeDecl(Static,ConstDecl(Id($3jqD1),ClassType(Id(_)),None)),AttributeDecl(Static,ConstDecl(Id($6),ClassType(Id(_)),None))]),ClassDecl(Id(_),[]),ClassDecl(Id(_),[MethodDecl(Id(z),Instance,[],Block([Break,Return()]))])])'''
        self.assertTrue(TestAST.test(input, expect, 358))

    def test_complex_program9(self):
        input = '''Class _3:__6{Var $_:_s;}Class _:_{Constructor (_,Y,D:Float ;_,_:Array [Array [Array [Array [String ,0b1],0B1_1],0X6],0B11];N6l_,A:_;J:_K2){}Val F:Boolean ;Var $SS:Boolean ;}'''
        expect = '''Program([ClassDecl(Id(_3),Id(__6),[AttributeDecl(Static,VarDecl(Id($_),ClassType(Id(_s)),NullLiteral()))]),ClassDecl(Id(_),Id(_),[MethodDecl(Id(Constructor),Instance,[param(Id(_),FloatType),param(Id(Y),FloatType),param(Id(D),FloatType),param(Id(_),ArrayType(3,ArrayType(6,ArrayType(3,ArrayType(1,StringType))))),param(Id(_),ArrayType(3,ArrayType(6,ArrayType(3,ArrayType(1,StringType))))),param(Id(N6l_),ClassType(Id(_))),param(Id(A),ClassType(Id(_))),param(Id(J),ClassType(Id(_K2)))],Block([])),AttributeDecl(Instance,ConstDecl(Id(F),BoolType,None)),AttributeDecl(Static,VarDecl(Id($SS),BoolType))])])'''
        self.assertTrue(TestAST.test(input, expect, 359))

    def test_complex_program10(self):
        input = '''Class M{}Class _0:_M5{}Class _:B5{Var $___:_;Constructor (_:Int ){}$P___(q,_,bL5__RD,pO36_:_8;M_5,c,AsF:Array [Array [Array [Array [Array [Array [Boolean ,0b1],0113],0b11],0B1_101_1_0],0X5B],55];_:X;_:Float ){} }Class oZ{Destructor (){} }'''
        expect = '''Program([ClassDecl(Id(M),[]),ClassDecl(Id(_0),Id(_M5),[]),ClassDecl(Id(_),Id(B5),[AttributeDecl(Static,VarDecl(Id($___),ClassType(Id(_)),NullLiteral())),MethodDecl(Id(Constructor),Instance,[param(Id(_),IntType)],Block([])),MethodDecl(Id($P___),Static,[param(Id(q),ClassType(Id(_8))),param(Id(_),ClassType(Id(_8))),param(Id(bL5__RD),ClassType(Id(_8))),param(Id(pO36_),ClassType(Id(_8))),param(Id(M_5),ArrayType(55,ArrayType(91,ArrayType(54,ArrayType(3,ArrayType(75,ArrayType(1,BoolType))))))),param(Id(c),ArrayType(55,ArrayType(91,ArrayType(54,ArrayType(3,ArrayType(75,ArrayType(1,BoolType))))))),param(Id(AsF),ArrayType(55,ArrayType(91,ArrayType(54,ArrayType(3,ArrayType(75,ArrayType(1,BoolType))))))),param(Id(_),ClassType(Id(X))),param(Id(_),FloatType)],Block([]))]),ClassDecl(Id(oZ),[MethodDecl(Id(Destructor),Instance,[],Block([]))])])'''
        self.assertTrue(TestAST.test(input, expect, 360))

    def test_complex_program11(self):
        input = '''Class __{z(){}Constructor (_,g5WWs76_:Boolean ;_,_,m7566_n:Boolean ;_:Float ;_:Array [Array [Float ,0b1000111],0B1011011];_,X:Array [Array [Array [Boolean ,0404_64_0_5_6_5],0X51],0b1]){} }'''
        expect = '''Program([ClassDecl(Id(__),[MethodDecl(Id(z),Instance,[],Block([])),MethodDecl(Id(Constructor),Instance,[param(Id(_),BoolType),param(Id(g5WWs76_),BoolType),param(Id(_),BoolType),param(Id(_),BoolType),param(Id(m7566_n),BoolType),param(Id(_),FloatType),param(Id(_),ArrayType(91,ArrayType(71,FloatType))),param(Id(_),ArrayType(1,ArrayType(81,ArrayType(68370805,BoolType)))),param(Id(X),ArrayType(1,ArrayType(81,ArrayType(68370805,BoolType))))],Block([]))])])'''
        self.assertTrue(TestAST.test(input, expect, 361))

    def test_complex_program12(self):
        input = '''Class uE:V{Constructor (_7:Int ;F97:Array [Array [Int ,0B110],0X53];M:Array [Array [Array [Array [Array [Float ,0B1010000],0103],10],7_0],94]){} }Class _{}Class _9:_{}Class qX:b{Val J:Int ;}'''
        expect = '''Program([ClassDecl(Id(uE),Id(V),[MethodDecl(Id(Constructor),Instance,[param(Id(_7),IntType),param(Id(F97),ArrayType(83,ArrayType(6,IntType))),param(Id(M),ArrayType(94,ArrayType(70,ArrayType(10,ArrayType(67,ArrayType(80,FloatType))))))],Block([]))]),ClassDecl(Id(_),[]),ClassDecl(Id(_9),Id(_),[]),ClassDecl(Id(qX),Id(b),[AttributeDecl(Instance,ConstDecl(Id(J),IntType,None))])])'''
        self.assertTrue(TestAST.test(input, expect, 362))

    def test_complex_program13(self):
        input = '''Class __79:Q_{Constructor (_,__:Int ;x,l1,_:Float ;a,V:Array [Array [Array [Array [Array [Array [Array [Array [Array [Array [Float ,044],0B1],0b100],0X3_2],0b11],0XBD3],38],044],38],0B1011101]){} }'''
        expect = '''Program([ClassDecl(Id(__79),Id(Q_),[MethodDecl(Id(Constructor),Instance,[param(Id(_),IntType),param(Id(__),IntType),param(Id(x),FloatType),param(Id(l1),FloatType),param(Id(_),FloatType),param(Id(a),ArrayType(93,ArrayType(38,ArrayType(36,ArrayType(38,ArrayType(3027,ArrayType(3,ArrayType(50,ArrayType(4,ArrayType(1,ArrayType(36,FloatType))))))))))),param(Id(V),ArrayType(93,ArrayType(38,ArrayType(36,ArrayType(38,ArrayType(3027,ArrayType(3,ArrayType(50,ArrayType(4,ArrayType(1,ArrayType(36,FloatType)))))))))))],Block([]))])])'''
        self.assertTrue(TestAST.test(input, expect, 363))

    def test_complex_program14(self):
        input = '''Class _eZ8U_{Var _:d;Constructor (){}Destructor (){ {}Continue ;Return ;}Var t,MCQ:_;Var $4_S:String ;Var $H,$H:String ;}Class z{Val $__,_,$2_,$_x__JU:i_;}Class e2{Val Lu:y;}'''
        expect = '''Program([ClassDecl(Id(_eZ8U_),[AttributeDecl(Instance,VarDecl(Id(_),ClassType(Id(d)),NullLiteral())),MethodDecl(Id(Constructor),Instance,[],Block([])),MethodDecl(Id(Destructor),Instance,[],Block([Block([]),Continue,Return()])),AttributeDecl(Instance,VarDecl(Id(t),ClassType(Id(_)),NullLiteral())),AttributeDecl(Instance,VarDecl(Id(MCQ),ClassType(Id(_)),NullLiteral())),AttributeDecl(Static,VarDecl(Id($4_S),StringType)),AttributeDecl(Static,VarDecl(Id($H),StringType)),AttributeDecl(Static,VarDecl(Id($H),StringType))]),ClassDecl(Id(z),[AttributeDecl(Static,ConstDecl(Id($__),ClassType(Id(i_)),None)),AttributeDecl(Instance,ConstDecl(Id(_),ClassType(Id(i_)),None)),AttributeDecl(Static,ConstDecl(Id($2_),ClassType(Id(i_)),None)),AttributeDecl(Static,ConstDecl(Id($_x__JU),ClassType(Id(i_)),None))]),ClassDecl(Id(e2),[AttributeDecl(Instance,ConstDecl(Id(Lu),ClassType(Id(y)),None))])])'''
        self.assertTrue(TestAST.test(input, expect, 364))

    def test_complex_program15(self):
        input = '''Class L:u{Var e,$H:Array [Array [Array [Array [Array [Float ,0B1],0B1001110],77],0B1001110],9_1];}Class _{}Class i4c{}Class E_{Var $_6:Array [Array [Array [Int ,026_00],0X42],0110];}Class e{}'''
        expect = '''Program([ClassDecl(Id(L),Id(u),[AttributeDecl(Instance,VarDecl(Id(e),ArrayType(91,ArrayType(78,ArrayType(77,ArrayType(78,ArrayType(1,FloatType))))))),AttributeDecl(Static,VarDecl(Id($H),ArrayType(91,ArrayType(78,ArrayType(77,ArrayType(78,ArrayType(1,FloatType)))))))]),ClassDecl(Id(_),[]),ClassDecl(Id(i4c),[]),ClassDecl(Id(E_),[AttributeDecl(Static,VarDecl(Id($_6),ArrayType(72,ArrayType(66,ArrayType(1408,IntType)))))]),ClassDecl(Id(e),[])])'''
        self.assertTrue(TestAST.test(input, expect, 365))

    def test_complex_program16(self):
        input = '''Class _Z3_:_g_j{}Class f__:LT{Destructor (){ {} }Var __:Array [Int ,0117];}Class b4:p{$_(_:Array [Array [Array [Float ,0b11_0],0x3C],0x3C];dTp__,_H9:_39;h,p_J:_;XH_,_73__,_:Array [String ,0b101]){}Constructor (i6_,_5_a,_8:z9;_,C:Float ){} }Class U_R_{}'''
        expect = '''Program([ClassDecl(Id(_Z3_),Id(_g_j),[]),ClassDecl(Id(f__),Id(LT),[MethodDecl(Id(Destructor),Instance,[],Block([Block([])])),AttributeDecl(Instance,VarDecl(Id(__),ArrayType(79,IntType)))]),ClassDecl(Id(b4),Id(p),[MethodDecl(Id($_),Static,[param(Id(_),ArrayType(60,ArrayType(60,ArrayType(6,FloatType)))),param(Id(dTp__),ClassType(Id(_39))),param(Id(_H9),ClassType(Id(_39))),param(Id(h),ClassType(Id(_))),param(Id(p_J),ClassType(Id(_))),param(Id(XH_),ArrayType(5,StringType)),param(Id(_73__),ArrayType(5,StringType)),param(Id(_),ArrayType(5,StringType))],Block([])),MethodDecl(Id(Constructor),Instance,[param(Id(i6_),ClassType(Id(z9))),param(Id(_5_a),ClassType(Id(z9))),param(Id(_8),ClassType(Id(z9))),param(Id(_),FloatType),param(Id(C),FloatType)],Block([]))]),ClassDecl(Id(U_R_),[])])'''
        self.assertTrue(TestAST.test(input, expect, 366))

    def test_complex_program17(self):
        input = '''Class _{Destructor (){} }Class __{Var $fcU8,$_,$_,_,$T,_:String ;Var _:Array [Array [Array [String ,0B100010],34_429],014];}Class _H{Ky(_3:Array [Array [Array [Array [Float ,0b1011111],36],36],36];ue6,XV5,saG0:Array [Array [Array [Int ,9],04],0x5];p_t:Boolean ){}Destructor (){}Val D9_F_:Array [Array [String ,0X5],050];Destructor (){Continue ;{} }}'''
        expect = '''Program([ClassDecl(Id(_),[MethodDecl(Id(Destructor),Instance,[],Block([]))]),ClassDecl(Id(__),[AttributeDecl(Static,VarDecl(Id($fcU8),StringType)),AttributeDecl(Static,VarDecl(Id($_),StringType)),AttributeDecl(Static,VarDecl(Id($_),StringType)),AttributeDecl(Instance,VarDecl(Id(_),StringType)),AttributeDecl(Static,VarDecl(Id($T),StringType)),AttributeDecl(Instance,VarDecl(Id(_),StringType)),AttributeDecl(Instance,VarDecl(Id(_),ArrayType(12,ArrayType(34429,ArrayType(34,StringType)))))]),ClassDecl(Id(_H),[MethodDecl(Id(Ky),Instance,[param(Id(_3),ArrayType(36,ArrayType(36,ArrayType(36,ArrayType(95,FloatType))))),param(Id(ue6),ArrayType(5,ArrayType(4,ArrayType(9,IntType)))),param(Id(XV5),ArrayType(5,ArrayType(4,ArrayType(9,IntType)))),param(Id(saG0),ArrayType(5,ArrayType(4,ArrayType(9,IntType)))),param(Id(p_t),BoolType)],Block([])),MethodDecl(Id(Destructor),Instance,[],Block([])),AttributeDecl(Instance,ConstDecl(Id(D9_F_),ArrayType(40,ArrayType(5,StringType)),None)),MethodDecl(Id(Destructor),Instance,[],Block([Continue,Block([])]))])])'''
        self.assertTrue(TestAST.test(input, expect, 367))

    def test_complex_program18(self):
        input = '''Class I1:Z_1UbF{Var __:Boolean ;}Class _{}Class c2:Z{}Class _:__{Val $2_p:Array [Array [Array [Boolean ,07_27],0b1_00],07_5_02_2];}Class _9:_{}Class _e:hH{Destructor (){}Val $_:Array [Float ,0X1A];}'''
        expect = '''Program([ClassDecl(Id(I1),Id(Z_1UbF),[AttributeDecl(Instance,VarDecl(Id(__),BoolType))]),ClassDecl(Id(_),[]),ClassDecl(Id(c2),Id(Z),[]),ClassDecl(Id(_),Id(__),[AttributeDecl(Static,ConstDecl(Id($2_p),ArrayType(31250,ArrayType(4,ArrayType(471,BoolType))),None))]),ClassDecl(Id(_9),Id(_),[]),ClassDecl(Id(_e),Id(hH),[MethodDecl(Id(Destructor),Instance,[],Block([])),AttributeDecl(Static,ConstDecl(Id($_),ArrayType(26,FloatType),None))])])'''
        self.assertTrue(TestAST.test(input, expect, 368))

    def test_complex_program19(self):
        input = '''Class __C7q0_j{Constructor (){}H(_0:Array [Int ,66];qL:Array [Float ,07];_n:Array [Int ,66];X_,S:Float ;C:String ;MY:Array [Boolean ,02];_,_y7__,_,_:y;w:Boolean ;_:_;u8,m_5:Array [Array [Int ,66],0b110010]){} }'''
        expect = '''Program([ClassDecl(Id(__C7q0_j),[MethodDecl(Id(Constructor),Instance,[],Block([])),MethodDecl(Id(H),Instance,[param(Id(_0),ArrayType(66,IntType)),param(Id(qL),ArrayType(7,FloatType)),param(Id(_n),ArrayType(66,IntType)),param(Id(X_),FloatType),param(Id(S),FloatType),param(Id(C),StringType),param(Id(MY),ArrayType(2,BoolType)),param(Id(_),ClassType(Id(y))),param(Id(_y7__),ClassType(Id(y))),param(Id(_),ClassType(Id(y))),param(Id(_),ClassType(Id(y))),param(Id(w),BoolType),param(Id(_),ClassType(Id(_))),param(Id(u8),ArrayType(50,ArrayType(66,IntType))),param(Id(m_5),ArrayType(50,ArrayType(66,IntType)))],Block([]))])])'''
        self.assertTrue(TestAST.test(input, expect, 369))

    def test_complex_program20(self):
        input = '''Class _:E_G__{}Class SO:k{Val $P:Boolean ;}Class _{Val j1,_oOU__,F_:S;}Class _q{Val X,$h__5YeVB:Array [Array [Float ,0xE_3_0],41];_(l:Int ;_,W,D,w,Heo__1_:__;ZLL1R:Float ;v:Array [Int ,41];_L,z_:String ;n__c,_,i98,_,w:Array [Array [Array [String ,0b10100],0b1],0xCC]){} }Class _4X{Destructor (){} }'''
        expect = '''Program([ClassDecl(Id(_),Id(E_G__),[]),ClassDecl(Id(SO),Id(k),[AttributeDecl(Static,ConstDecl(Id($P),BoolType,None))]),ClassDecl(Id(_),[AttributeDecl(Instance,ConstDecl(Id(j1),ClassType(Id(S)),None)),AttributeDecl(Instance,ConstDecl(Id(_oOU__),ClassType(Id(S)),None)),AttributeDecl(Instance,ConstDecl(Id(F_),ClassType(Id(S)),None))]),ClassDecl(Id(_q),[AttributeDecl(Instance,ConstDecl(Id(X),ArrayType(41,ArrayType(3632,FloatType)),None)),AttributeDecl(Static,ConstDecl(Id($h__5YeVB),ArrayType(41,ArrayType(3632,FloatType)),None)),MethodDecl(Id(_),Instance,[param(Id(l),IntType),param(Id(_),ClassType(Id(__))),param(Id(W),ClassType(Id(__))),param(Id(D),ClassType(Id(__))),param(Id(w),ClassType(Id(__))),param(Id(Heo__1_),ClassType(Id(__))),param(Id(ZLL1R),FloatType),param(Id(v),ArrayType(41,IntType)),param(Id(_L),StringType),param(Id(z_),StringType),param(Id(n__c),ArrayType(204,ArrayType(1,ArrayType(20,StringType)))),param(Id(_),ArrayType(204,ArrayType(1,ArrayType(20,StringType)))),param(Id(i98),ArrayType(204,ArrayType(1,ArrayType(20,StringType)))),param(Id(_),ArrayType(204,ArrayType(1,ArrayType(20,StringType)))),param(Id(w),ArrayType(204,ArrayType(1,ArrayType(20,StringType))))],Block([]))]),ClassDecl(Id(_4X),[MethodDecl(Id(Destructor),Instance,[],Block([]))])])'''
        self.assertTrue(TestAST.test(input, expect, 370))

    def test_complex_program21(self):
        input = '''Class _R94_c_9:_{}Class XF_{Var $1,$3k_,D,_:Int ;$0(){Return ;}Constructor (s,B_27_id:_;d3z_Y__C67_i,P:String ){}w(_:Array [Float ,0X41];r,_,_b:Array [Array [Array [Array [Array [String ,399],0123],0B110011],6],0X41];_,_z9:Array [Array [Array [Int ,84],84],9_4];O,F,U:String ;__,h,_:Array [Boolean ,5]){} }'''
        expect = '''Program([ClassDecl(Id(_R94_c_9),Id(_),[]),ClassDecl(Id(XF_),[AttributeDecl(Static,VarDecl(Id($1),IntType)),AttributeDecl(Static,VarDecl(Id($3k_),IntType)),AttributeDecl(Instance,VarDecl(Id(D),IntType)),AttributeDecl(Instance,VarDecl(Id(_),IntType)),MethodDecl(Id($0),Static,[],Block([Return()])),MethodDecl(Id(Constructor),Instance,[param(Id(s),ClassType(Id(_))),param(Id(B_27_id),ClassType(Id(_))),param(Id(d3z_Y__C67_i),StringType),param(Id(P),StringType)],Block([])),MethodDecl(Id(w),Instance,[param(Id(_),ArrayType(65,FloatType)),param(Id(r),ArrayType(65,ArrayType(6,ArrayType(51,ArrayType(83,ArrayType(399,StringType)))))),param(Id(_),ArrayType(65,ArrayType(6,ArrayType(51,ArrayType(83,ArrayType(399,StringType)))))),param(Id(_b),ArrayType(65,ArrayType(6,ArrayType(51,ArrayType(83,ArrayType(399,StringType)))))),param(Id(_),ArrayType(94,ArrayType(84,ArrayType(84,IntType)))),param(Id(_z9),ArrayType(94,ArrayType(84,ArrayType(84,IntType)))),param(Id(O),StringType),param(Id(F),StringType),param(Id(U),StringType),param(Id(__),ArrayType(5,BoolType)),param(Id(h),ArrayType(5,BoolType)),param(Id(_),ArrayType(5,BoolType))],Block([]))])])'''
        self.assertTrue(TestAST.test(input, expect, 371))

    def test_complex_program22(self):
        input = '''Class n:s_{}Class __:S_{}Class K1:KQ{}Class _1:__{Val $_,$Gf_7,$31,_:Array [Boolean ,39];Var $u,_:S___;Val $__:Array [Array [Array [Boolean ,0x43],66_3],0b1011101];Var $04llb_4,$o,dR:Int ;Destructor (){Break ;} }Class H_:i54{C(){} }Class W{}'''
        expect = '''Program([ClassDecl(Id(n),Id(s_),[]),ClassDecl(Id(__),Id(S_),[]),ClassDecl(Id(K1),Id(KQ),[]),ClassDecl(Id(_1),Id(__),[AttributeDecl(Static,ConstDecl(Id($_),ArrayType(39,BoolType),None)),AttributeDecl(Static,ConstDecl(Id($Gf_7),ArrayType(39,BoolType),None)),AttributeDecl(Static,ConstDecl(Id($31),ArrayType(39,BoolType),None)),AttributeDecl(Instance,ConstDecl(Id(_),ArrayType(39,BoolType),None)),AttributeDecl(Static,VarDecl(Id($u),ClassType(Id(S___)),NullLiteral())),AttributeDecl(Instance,VarDecl(Id(_),ClassType(Id(S___)),NullLiteral())),AttributeDecl(Static,ConstDecl(Id($__),ArrayType(93,ArrayType(663,ArrayType(67,BoolType))),None)),AttributeDecl(Static,VarDecl(Id($04llb_4),IntType)),AttributeDecl(Static,VarDecl(Id($o),IntType)),AttributeDecl(Instance,VarDecl(Id(dR),IntType)),MethodDecl(Id(Destructor),Instance,[],Block([Break]))]),ClassDecl(Id(H_),Id(i54),[MethodDecl(Id(C),Instance,[],Block([]))]),ClassDecl(Id(W),[])])'''
        self.assertTrue(TestAST.test(input, expect, 372))

    def test_complex_program23(self):
        input = '''Class K{}Class Q:_V{}Class _63{}Class _:_t2q{_7z(_,D,a_:Boolean ;_,_7q9,I_:Array [Array [Array [Array [Int ,0b101101],0B1_0],60],0b1]){}Destructor (){_::$D()._.T.n().kd().y()._();Continue ;}Var $__m___,$_,_:B6;}Class _{}'''
        expect = '''Program([ClassDecl(Id(K),[]),ClassDecl(Id(Q),Id(_V),[]),ClassDecl(Id(_63),[]),ClassDecl(Id(_),Id(_t2q),[MethodDecl(Id(_7z),Instance,[param(Id(_),BoolType),param(Id(D),BoolType),param(Id(a_),BoolType),param(Id(_),ArrayType(1,ArrayType(60,ArrayType(2,ArrayType(45,IntType))))),param(Id(_7q9),ArrayType(1,ArrayType(60,ArrayType(2,ArrayType(45,IntType))))),param(Id(I_),ArrayType(1,ArrayType(60,ArrayType(2,ArrayType(45,IntType)))))],Block([])),MethodDecl(Id(Destructor),Instance,[],Block([Call(CallExpr(CallExpr(CallExpr(FieldAccess(FieldAccess(CallExpr(Id(_),Id($D),[]),Id(_)),Id(T)),Id(n),[]),Id(kd),[]),Id(y),[]),Id(_),[]),Continue])),AttributeDecl(Static,VarDecl(Id($__m___),ClassType(Id(B6)),NullLiteral())),AttributeDecl(Static,VarDecl(Id($_),ClassType(Id(B6)),NullLiteral())),AttributeDecl(Instance,VarDecl(Id(_),ClassType(Id(B6)),NullLiteral()))]),ClassDecl(Id(_),[])])'''
        self.assertTrue(TestAST.test(input, expect, 373))

    def test_complex_program24(self):
        input = '''Class o_:_{}Class __:_{Var $G:_;Var $_:__;Constructor (Y3H,_,_B,U,H,_m:_;W_,k6:Array [String ,0B110101];_:Float ;_8E,V,b,s,_,_,_:Boolean ){}Destructor (){} }Class _{Constructor (c5:String ;_:Array [Array [Boolean ,0430_0_1],0X1B];_,_kpR:Array [Array [Array [Array [Float ,0X9_8],01],0b111011],0X1B]){} }Class _{Constructor (_,Nb:Boolean ;_,_,_,d:Array [Int ,0b111011];_:Float ;rj,o:k){ {} }Destructor (){} }'''
        expect = '''Program([ClassDecl(Id(o_),Id(_),[]),ClassDecl(Id(__),Id(_),[AttributeDecl(Static,VarDecl(Id($G),ClassType(Id(_)),NullLiteral())),AttributeDecl(Static,VarDecl(Id($_),ClassType(Id(__)),NullLiteral())),MethodDecl(Id(Constructor),Instance,[param(Id(Y3H),ClassType(Id(_))),param(Id(_),ClassType(Id(_))),param(Id(_B),ClassType(Id(_))),param(Id(U),ClassType(Id(_))),param(Id(H),ClassType(Id(_))),param(Id(_m),ClassType(Id(_))),param(Id(W_),ArrayType(53,StringType)),param(Id(k6),ArrayType(53,StringType)),param(Id(_),FloatType),param(Id(_8E),BoolType),param(Id(V),BoolType),param(Id(b),BoolType),param(Id(s),BoolType),param(Id(_),BoolType),param(Id(_),BoolType),param(Id(_),BoolType)],Block([])),MethodDecl(Id(Destructor),Instance,[],Block([]))]),ClassDecl(Id(_),[MethodDecl(Id(Constructor),Instance,[param(Id(c5),StringType),param(Id(_),ArrayType(27,ArrayType(17921,BoolType))),param(Id(_),ArrayType(27,ArrayType(59,ArrayType(1,ArrayType(152,FloatType))))),param(Id(_kpR),ArrayType(27,ArrayType(59,ArrayType(1,ArrayType(152,FloatType)))))],Block([]))]),ClassDecl(Id(_),[MethodDecl(Id(Constructor),Instance,[param(Id(_),BoolType),param(Id(Nb),BoolType),param(Id(_),ArrayType(59,IntType)),param(Id(_),ArrayType(59,IntType)),param(Id(_),ArrayType(59,IntType)),param(Id(d),ArrayType(59,IntType)),param(Id(_),FloatType),param(Id(rj),ClassType(Id(k))),param(Id(o),ClassType(Id(k)))],Block([Block([])])),MethodDecl(Id(Destructor),Instance,[],Block([]))])])'''
        self.assertTrue(TestAST.test(input, expect, 374))

    def test_complex_program25(self):
        input = '''Class i{Destructor (){Break ;}Var $q,$v,_8:__0;Constructor (k,_8_o0U,H_,______:u;e6,_:Array [String ,02];n1:___;M5,_O_:Array [Int ,0x1]){} }Class j:q_5{}Class _{Var d_,V4:Float ;Val F,$c6,_:Array [Int ,13];Destructor (){} }'''
        expect = '''Program([ClassDecl(Id(i),[MethodDecl(Id(Destructor),Instance,[],Block([Break])),AttributeDecl(Static,VarDecl(Id($q),ClassType(Id(__0)),NullLiteral())),AttributeDecl(Static,VarDecl(Id($v),ClassType(Id(__0)),NullLiteral())),AttributeDecl(Instance,VarDecl(Id(_8),ClassType(Id(__0)),NullLiteral())),MethodDecl(Id(Constructor),Instance,[param(Id(k),ClassType(Id(u))),param(Id(_8_o0U),ClassType(Id(u))),param(Id(H_),ClassType(Id(u))),param(Id(______),ClassType(Id(u))),param(Id(e6),ArrayType(2,StringType)),param(Id(_),ArrayType(2,StringType)),param(Id(n1),ClassType(Id(___))),param(Id(M5),ArrayType(1,IntType)),param(Id(_O_),ArrayType(1,IntType))],Block([]))]),ClassDecl(Id(j),Id(q_5),[]),ClassDecl(Id(_),[AttributeDecl(Instance,VarDecl(Id(d_),FloatType)),AttributeDecl(Instance,VarDecl(Id(V4),FloatType)),AttributeDecl(Instance,ConstDecl(Id(F),ArrayType(13,IntType),None)),AttributeDecl(Static,ConstDecl(Id($c6),ArrayType(13,IntType),None)),AttributeDecl(Instance,ConstDecl(Id(_),ArrayType(13,IntType),None)),MethodDecl(Id(Destructor),Instance,[],Block([]))])])'''
        self.assertTrue(TestAST.test(input, expect, 375))

    def test_complex_program26(self):
        input = '''Class _{}Class C_{}Class I_{_q(_6t_j_v,_8,T:Array [Float ,5];V:Boolean ;dP:Boolean ;C_2,_O:Array [Array [Array [Int ,0X5],0B1],0x3E];E:Float ){} }Class r___:c{Constructor (hI:eW;F__,s:Boolean ;_,c_,_3,_0,Q0B,j723_:_WwL;PG6_D:Array [Int ,0107];L:__;l,e_:Float ;x:Float ;_,M:_;n:_){} }'''
        expect = '''Program([ClassDecl(Id(_),[]),ClassDecl(Id(C_),[]),ClassDecl(Id(I_),[MethodDecl(Id(_q),Instance,[param(Id(_6t_j_v),ArrayType(5,FloatType)),param(Id(_8),ArrayType(5,FloatType)),param(Id(T),ArrayType(5,FloatType)),param(Id(V),BoolType),param(Id(dP),BoolType),param(Id(C_2),ArrayType(62,ArrayType(1,ArrayType(5,IntType)))),param(Id(_O),ArrayType(62,ArrayType(1,ArrayType(5,IntType)))),param(Id(E),FloatType)],Block([]))]),ClassDecl(Id(r___),Id(c),[MethodDecl(Id(Constructor),Instance,[param(Id(hI),ClassType(Id(eW))),param(Id(F__),BoolType),param(Id(s),BoolType),param(Id(_),ClassType(Id(_WwL))),param(Id(c_),ClassType(Id(_WwL))),param(Id(_3),ClassType(Id(_WwL))),param(Id(_0),ClassType(Id(_WwL))),param(Id(Q0B),ClassType(Id(_WwL))),param(Id(j723_),ClassType(Id(_WwL))),param(Id(PG6_D),ArrayType(71,IntType)),param(Id(L),ClassType(Id(__))),param(Id(l),FloatType),param(Id(e_),FloatType),param(Id(x),FloatType),param(Id(_),ClassType(Id(_))),param(Id(M),ClassType(Id(_))),param(Id(n),ClassType(Id(_)))],Block([]))])])'''
        self.assertTrue(TestAST.test(input, expect, 376))

    def test_complex_program27(self):
        input = '''Class b:A{Var $B5_,$5,$A:Array [Array [Array [Array [Boolean ,0X14],025],025],51];$5r9(e,_c,_66:Array [Array [Array [Array [Array [Array [Array [Boolean ,0B1_011],0xC_6],0b110101],0B1_0],0X14],0b110101],0X14]){} }Class V_{Var _:Int ;}'''
        expect = '''Program([ClassDecl(Id(b),Id(A),[AttributeDecl(Static,VarDecl(Id($B5_),ArrayType(51,ArrayType(21,ArrayType(21,ArrayType(20,BoolType)))))),AttributeDecl(Static,VarDecl(Id($5),ArrayType(51,ArrayType(21,ArrayType(21,ArrayType(20,BoolType)))))),AttributeDecl(Static,VarDecl(Id($A),ArrayType(51,ArrayType(21,ArrayType(21,ArrayType(20,BoolType)))))),MethodDecl(Id($5r9),Static,[param(Id(e),ArrayType(20,ArrayType(53,ArrayType(20,ArrayType(2,ArrayType(53,ArrayType(198,ArrayType(11,BoolType)))))))),param(Id(_c),ArrayType(20,ArrayType(53,ArrayType(20,ArrayType(2,ArrayType(53,ArrayType(198,ArrayType(11,BoolType)))))))),param(Id(_66),ArrayType(20,ArrayType(53,ArrayType(20,ArrayType(2,ArrayType(53,ArrayType(198,ArrayType(11,BoolType))))))))],Block([]))]),ClassDecl(Id(V_),[AttributeDecl(Instance,VarDecl(Id(_),IntType))])])'''
        self.assertTrue(TestAST.test(input, expect, 377))

    def test_complex_program28(self):
        input = '''Class h_:_1j7{Constructor (g,_p47o:Array [Array [Array [Array [Array [Array [Boolean ,0101],0X25],0B1100011],0b1010101],100],89];__Q2,_:_){Continue ;}Val $_:Array [Array [Array [Array [Array [Int ,100],06_1],0101],100],0b1010101];}'''
        expect = '''Program([ClassDecl(Id(h_),Id(_1j7),[MethodDecl(Id(Constructor),Instance,[param(Id(g),ArrayType(89,ArrayType(100,ArrayType(85,ArrayType(99,ArrayType(37,ArrayType(65,BoolType))))))),param(Id(_p47o),ArrayType(89,ArrayType(100,ArrayType(85,ArrayType(99,ArrayType(37,ArrayType(65,BoolType))))))),param(Id(__Q2),ClassType(Id(_))),param(Id(_),ClassType(Id(_)))],Block([Continue])),AttributeDecl(Static,ConstDecl(Id($_),ArrayType(85,ArrayType(100,ArrayType(65,ArrayType(49,ArrayType(100,IntType))))),None))])])'''
        self.assertTrue(TestAST.test(input, expect, 378))

    def test_complex_program29(self):
        input = '''Class m{}Class R:_j{Destructor (){} }Class _m:Ta_{Var $27:Float ;Val _k5,_:Array [Array [Array [Float ,025],0b1011110],0x44];$81(){}Val _9X:Boolean ;}Class s:_jV{e2230(_w:Float ;_,__,h,U__:_){}Val _91594,$_353_Fv:Int ;}'''
        expect = '''Program([ClassDecl(Id(m),[]),ClassDecl(Id(R),Id(_j),[MethodDecl(Id(Destructor),Instance,[],Block([]))]),ClassDecl(Id(_m),Id(Ta_),[AttributeDecl(Static,VarDecl(Id($27),FloatType)),AttributeDecl(Instance,ConstDecl(Id(_k5),ArrayType(68,ArrayType(94,ArrayType(21,FloatType))),None)),AttributeDecl(Instance,ConstDecl(Id(_),ArrayType(68,ArrayType(94,ArrayType(21,FloatType))),None)),MethodDecl(Id($81),Static,[],Block([])),AttributeDecl(Instance,ConstDecl(Id(_9X),BoolType,None))]),ClassDecl(Id(s),Id(_jV),[MethodDecl(Id(e2230),Instance,[param(Id(_w),FloatType),param(Id(_),ClassType(Id(_))),param(Id(__),ClassType(Id(_))),param(Id(h),ClassType(Id(_))),param(Id(U__),ClassType(Id(_)))],Block([])),AttributeDecl(Instance,ConstDecl(Id(_91594),IntType,None)),AttributeDecl(Static,ConstDecl(Id($_353_Fv),IntType,None))])])'''
        self.assertTrue(TestAST.test(input, expect, 379))

    def test_complex_program30(self):
        input = '''Class G5Vk{Destructor (){Continue ;} }Class _8{}Class __{Val _:Array [Int ,0B1011001];}Class o___n{Var _42,$_5,e8w69,_P,_:Array [Array [Array [Float ,0b1],0X8],7];}Class l_{}'''
        expect = '''Program([ClassDecl(Id(G5Vk),[MethodDecl(Id(Destructor),Instance,[],Block([Continue]))]),ClassDecl(Id(_8),[]),ClassDecl(Id(__),[AttributeDecl(Instance,ConstDecl(Id(_),ArrayType(89,IntType),None))]),ClassDecl(Id(o___n),[AttributeDecl(Instance,VarDecl(Id(_42),ArrayType(7,ArrayType(8,ArrayType(1,FloatType))))),AttributeDecl(Static,VarDecl(Id($_5),ArrayType(7,ArrayType(8,ArrayType(1,FloatType))))),AttributeDecl(Instance,VarDecl(Id(e8w69),ArrayType(7,ArrayType(8,ArrayType(1,FloatType))))),AttributeDecl(Instance,VarDecl(Id(_P),ArrayType(7,ArrayType(8,ArrayType(1,FloatType))))),AttributeDecl(Instance,VarDecl(Id(_),ArrayType(7,ArrayType(8,ArrayType(1,FloatType)))))]),ClassDecl(Id(l_),[])])'''
        self.assertTrue(TestAST.test(input, expect, 380))

    def test_complex_program31(self):
        input = '''Class _3_6TW7m2__{Constructor (_X_,_:Array [Array [Int ,037],0x3];e987,b,__W,_:_9_){Break ;}Destructor (){ {} }Constructor (o:Array [Int ,73]){Break ;Var _Zk43,_00,_:Array [Float ,4_9];} }'''
        expect = '''Program([ClassDecl(Id(_3_6TW7m2__),[MethodDecl(Id(Constructor),Instance,[param(Id(_X_),ArrayType(3,ArrayType(31,IntType))),param(Id(_),ArrayType(3,ArrayType(31,IntType))),param(Id(e987),ClassType(Id(_9_))),param(Id(b),ClassType(Id(_9_))),param(Id(__W),ClassType(Id(_9_))),param(Id(_),ClassType(Id(_9_)))],Block([Break])),MethodDecl(Id(Destructor),Instance,[],Block([Block([])])),MethodDecl(Id(Constructor),Instance,[param(Id(o),ArrayType(73,IntType))],Block([Break,VarDecl(Id(_Zk43),ArrayType(49,FloatType)),VarDecl(Id(_00),ArrayType(49,FloatType)),VarDecl(Id(_),ArrayType(49,FloatType))]))])])'''
        self.assertTrue(TestAST.test(input, expect, 381))

    def test_complex_program32(self):
        input = '''Class c:_4{Val _,$_,$8_5_2t:Array [Int ,043_7];Val $_,_:Float ;Constructor (_:String ;_:Float ){} }Class I{Var _:Array [Array [Array [String ,2_6],8_4],0b1011001];__(){Var y__:String ;} }Class QZ_{$T(){} }'''
        expect = '''Program([ClassDecl(Id(c),Id(_4),[AttributeDecl(Instance,ConstDecl(Id(_),ArrayType(287,IntType),None)),AttributeDecl(Static,ConstDecl(Id($_),ArrayType(287,IntType),None)),AttributeDecl(Static,ConstDecl(Id($8_5_2t),ArrayType(287,IntType),None)),AttributeDecl(Static,ConstDecl(Id($_),FloatType,None)),AttributeDecl(Instance,ConstDecl(Id(_),FloatType,None)),MethodDecl(Id(Constructor),Instance,[param(Id(_),StringType),param(Id(_),FloatType)],Block([]))]),ClassDecl(Id(I),[AttributeDecl(Instance,VarDecl(Id(_),ArrayType(89,ArrayType(84,ArrayType(26,StringType))))),MethodDecl(Id(__),Instance,[],Block([VarDecl(Id(y__),StringType)]))]),ClassDecl(Id(QZ_),[MethodDecl(Id($T),Static,[],Block([]))])])'''
        self.assertTrue(TestAST.test(input, expect, 382))

    def test_complex_program33(self):
        input = '''Class R_0Z_:J{Constructor (_8oSz9_,Iv,x,__,O:Array [Boolean ,020]){} }Class G:G_l3{Var $_6_v:Array [String ,05_7_6];w48_(p,f_1,_,_,_:Float ;_,S,_,_:Boolean ){Return ;} }'''
        expect = '''Program([ClassDecl(Id(R_0Z_),Id(J),[MethodDecl(Id(Constructor),Instance,[param(Id(_8oSz9_),ArrayType(16,BoolType)),param(Id(Iv),ArrayType(16,BoolType)),param(Id(x),ArrayType(16,BoolType)),param(Id(__),ArrayType(16,BoolType)),param(Id(O),ArrayType(16,BoolType))],Block([]))]),ClassDecl(Id(G),Id(G_l3),[AttributeDecl(Static,VarDecl(Id($_6_v),ArrayType(382,StringType))),MethodDecl(Id(w48_),Instance,[param(Id(p),FloatType),param(Id(f_1),FloatType),param(Id(_),FloatType),param(Id(_),FloatType),param(Id(_),FloatType),param(Id(_),BoolType),param(Id(S),BoolType),param(Id(_),BoolType),param(Id(_),BoolType)],Block([Return()]))])])'''
        self.assertTrue(TestAST.test(input, expect, 383))

    def test_complex_program34(self):
        input = '''Class _:f_Bia{_Z11(_:__;_,_,_D,_3T7__wo:Array [Float ,0124];f:Array [Array [Array [Float ,07],04],0124]){}Val _:Boolean ;}Class K{Constructor (cC:String ){}$_(){} }Class v{}'''
        expect = '''Program([ClassDecl(Id(_),Id(f_Bia),[MethodDecl(Id(_Z11),Instance,[param(Id(_),ClassType(Id(__))),param(Id(_),ArrayType(84,FloatType)),param(Id(_),ArrayType(84,FloatType)),param(Id(_D),ArrayType(84,FloatType)),param(Id(_3T7__wo),ArrayType(84,FloatType)),param(Id(f),ArrayType(84,ArrayType(4,ArrayType(7,FloatType))))],Block([])),AttributeDecl(Instance,ConstDecl(Id(_),BoolType,None))]),ClassDecl(Id(K),[MethodDecl(Id(Constructor),Instance,[param(Id(cC),StringType)],Block([])),MethodDecl(Id($_),Static,[],Block([]))]),ClassDecl(Id(v),[])])'''
        self.assertTrue(TestAST.test(input, expect, 384))

    def test_complex_program35(self):
        input = '''Class Q:_{}Class _K38{Constructor (_jdP,J:_;b,__m,G_:Array [Array [Array [Boolean ,91],0716],0X7];_,_Bg,_2:Boolean ;gNf:_;U:Array [Int ,026];_Ubm:j_P;__,i,j_7o42,f_:Boolean ;z,_:Array [Boolean ,0X7]){} }'''
        expect = '''Program([ClassDecl(Id(Q),Id(_),[]),ClassDecl(Id(_K38),[MethodDecl(Id(Constructor),Instance,[param(Id(_jdP),ClassType(Id(_))),param(Id(J),ClassType(Id(_))),param(Id(b),ArrayType(7,ArrayType(462,ArrayType(91,BoolType)))),param(Id(__m),ArrayType(7,ArrayType(462,ArrayType(91,BoolType)))),param(Id(G_),ArrayType(7,ArrayType(462,ArrayType(91,BoolType)))),param(Id(_),BoolType),param(Id(_Bg),BoolType),param(Id(_2),BoolType),param(Id(gNf),ClassType(Id(_))),param(Id(U),ArrayType(22,IntType)),param(Id(_Ubm),ClassType(Id(j_P))),param(Id(__),BoolType),param(Id(i),BoolType),param(Id(j_7o42),BoolType),param(Id(f_),BoolType),param(Id(z),ArrayType(7,BoolType)),param(Id(_),ArrayType(7,BoolType))],Block([]))])])'''
        self.assertTrue(TestAST.test(input, expect, 385))

    def test_complex_program36(self):
        input = '''Class _{Var $_L,$7,$3V,$9__,$2,$_1_8,_k,$5_:Array [Array [Array [Array [Array [String ,0204_6_1],0x4],03],18],2_1];Constructor (U8lj:Array [Array [Array [Int ,9_24],0XC],0XC];L:f;G_C,l_,_,_:Q){} }'''
        expect = '''Program([ClassDecl(Id(_),[AttributeDecl(Static,VarDecl(Id($_L),ArrayType(21,ArrayType(18,ArrayType(3,ArrayType(4,ArrayType(8497,StringType))))))),AttributeDecl(Static,VarDecl(Id($7),ArrayType(21,ArrayType(18,ArrayType(3,ArrayType(4,ArrayType(8497,StringType))))))),AttributeDecl(Static,VarDecl(Id($3V),ArrayType(21,ArrayType(18,ArrayType(3,ArrayType(4,ArrayType(8497,StringType))))))),AttributeDecl(Static,VarDecl(Id($9__),ArrayType(21,ArrayType(18,ArrayType(3,ArrayType(4,ArrayType(8497,StringType))))))),AttributeDecl(Static,VarDecl(Id($2),ArrayType(21,ArrayType(18,ArrayType(3,ArrayType(4,ArrayType(8497,StringType))))))),AttributeDecl(Static,VarDecl(Id($_1_8),ArrayType(21,ArrayType(18,ArrayType(3,ArrayType(4,ArrayType(8497,StringType))))))),AttributeDecl(Instance,VarDecl(Id(_k),ArrayType(21,ArrayType(18,ArrayType(3,ArrayType(4,ArrayType(8497,StringType))))))),AttributeDecl(Static,VarDecl(Id($5_),ArrayType(21,ArrayType(18,ArrayType(3,ArrayType(4,ArrayType(8497,StringType))))))),MethodDecl(Id(Constructor),Instance,[param(Id(U8lj),ArrayType(12,ArrayType(12,ArrayType(924,IntType)))),param(Id(L),ClassType(Id(f))),param(Id(G_C),ClassType(Id(Q))),param(Id(l_),ClassType(Id(Q))),param(Id(_),ClassType(Id(Q))),param(Id(_),ClassType(Id(Q)))],Block([]))])])'''
        self.assertTrue(TestAST.test(input, expect, 386))

    def test_complex_program37(self):
        input = '''Class h:S{_p(us:Array [Array [Boolean ,0b101],0X5E];RO,_,_:Array [Array [Array [Boolean ,9],84],03];__3__,Q,_0,_:Array [Boolean ,0X8_5];_1Djg:String ;Q61_,_,b,em,_i_:Array [Float ,0X5E];__,_w3,__x_o:_k;q:String ){} }'''
        expect = '''Program([ClassDecl(Id(h),Id(S),[MethodDecl(Id(_p),Instance,[param(Id(us),ArrayType(94,ArrayType(5,BoolType))),param(Id(RO),ArrayType(3,ArrayType(84,ArrayType(9,BoolType)))),param(Id(_),ArrayType(3,ArrayType(84,ArrayType(9,BoolType)))),param(Id(_),ArrayType(3,ArrayType(84,ArrayType(9,BoolType)))),param(Id(__3__),ArrayType(133,BoolType)),param(Id(Q),ArrayType(133,BoolType)),param(Id(_0),ArrayType(133,BoolType)),param(Id(_),ArrayType(133,BoolType)),param(Id(_1Djg),StringType),param(Id(Q61_),ArrayType(94,FloatType)),param(Id(_),ArrayType(94,FloatType)),param(Id(b),ArrayType(94,FloatType)),param(Id(em),ArrayType(94,FloatType)),param(Id(_i_),ArrayType(94,FloatType)),param(Id(__),ClassType(Id(_k))),param(Id(_w3),ClassType(Id(_k))),param(Id(__x_o),ClassType(Id(_k))),param(Id(q),StringType)],Block([]))])])'''
        self.assertTrue(TestAST.test(input, expect, 387))

    def test_complex_program38(self):
        input = '''Class X{Destructor (){} }Class S1_{Val _z,$4hA,$f:Array [Array [String ,0b1_1],0X59];Val V,_R,_I:Array [Array [Array [Array [Boolean ,15],0X59],0b1_0],3_3];}Class b{Destructor (){Break ;Continue ;Val x7_:_U___O;}____(){Continue ;}_(){} }'''
        expect = '''Program([ClassDecl(Id(X),[MethodDecl(Id(Destructor),Instance,[],Block([]))]),ClassDecl(Id(S1_),[AttributeDecl(Instance,ConstDecl(Id(_z),ArrayType(89,ArrayType(3,StringType)),None)),AttributeDecl(Static,ConstDecl(Id($4hA),ArrayType(89,ArrayType(3,StringType)),None)),AttributeDecl(Static,ConstDecl(Id($f),ArrayType(89,ArrayType(3,StringType)),None)),AttributeDecl(Instance,ConstDecl(Id(V),ArrayType(33,ArrayType(2,ArrayType(89,ArrayType(15,BoolType)))),None)),AttributeDecl(Instance,ConstDecl(Id(_R),ArrayType(33,ArrayType(2,ArrayType(89,ArrayType(15,BoolType)))),None)),AttributeDecl(Instance,ConstDecl(Id(_I),ArrayType(33,ArrayType(2,ArrayType(89,ArrayType(15,BoolType)))),None))]),ClassDecl(Id(b),[MethodDecl(Id(Destructor),Instance,[],Block([Break,Continue,ConstDecl(Id(x7_),ClassType(Id(_U___O)),None)])),MethodDecl(Id(____),Instance,[],Block([Continue])),MethodDecl(Id(_),Instance,[],Block([]))])])'''
        self.assertTrue(TestAST.test(input, expect, 388))

    def test_complex_program39(self):
        input = '''Class P7:__2c{$_896h(z7_,ac:String ;c__,XG_6,_:Array [Array [Float ,12],01_40];o,_,d_:Int ;Z,_:_8;Hm34:Array [String ,0B1_1_11_11]){}Constructor (){} }Class _F:_{Var _W:y;}'''
        expect = '''Program([ClassDecl(Id(P7),Id(__2c),[MethodDecl(Id($_896h),Static,[param(Id(z7_),StringType),param(Id(ac),StringType),param(Id(c__),ArrayType(96,ArrayType(12,FloatType))),param(Id(XG_6),ArrayType(96,ArrayType(12,FloatType))),param(Id(_),ArrayType(96,ArrayType(12,FloatType))),param(Id(o),IntType),param(Id(_),IntType),param(Id(d_),IntType),param(Id(Z),ClassType(Id(_8))),param(Id(_),ClassType(Id(_8))),param(Id(Hm34),ArrayType(63,StringType))],Block([])),MethodDecl(Id(Constructor),Instance,[],Block([]))]),ClassDecl(Id(_F),Id(_),[AttributeDecl(Instance,VarDecl(Id(_W),ClassType(Id(y)),NullLiteral()))])])'''
        self.assertTrue(TestAST.test(input, expect, 389))

    def test_complex_program40(self):
        input = '''Class __73:v_{}Class _04da:_70_0_63uq{Destructor (){Val M:_6__;{Break ;} }}Class c{}Class _:q{}Class _4{Constructor (Z:_M__7o){}$6_0(){Var _:Boolean ;} }Class _{Destructor (){} }Class t_8_:_6z_886{}Class _{}'''
        expect = '''Program([ClassDecl(Id(__73),Id(v_),[]),ClassDecl(Id(_04da),Id(_70_0_63uq),[MethodDecl(Id(Destructor),Instance,[],Block([ConstDecl(Id(M),ClassType(Id(_6__)),None),Block([Break])]))]),ClassDecl(Id(c),[]),ClassDecl(Id(_),Id(q),[]),ClassDecl(Id(_4),[MethodDecl(Id(Constructor),Instance,[param(Id(Z),ClassType(Id(_M__7o)))],Block([])),MethodDecl(Id($6_0),Static,[],Block([VarDecl(Id(_),BoolType)]))]),ClassDecl(Id(_),[MethodDecl(Id(Destructor),Instance,[],Block([]))]),ClassDecl(Id(t_8_),Id(_6z_886),[]),ClassDecl(Id(_),[])])'''
        self.assertTrue(TestAST.test(input, expect, 490))

    def test_complex_program41(self):
        input = '''Class J_:_{Constructor (){}Var $u_:Array [Float ,03];Constructor (P:_;_,a,T:String ;X_Y_wp:Float ;_,t,_:_;_2J:Array [Float ,61]){}Constructor (hg,d,_,_,V:S;_,d__,SV:_Q){}I(){} }Class o1:_{$_(_,_06,_1_,_,_j4,__:Float ;t,_:String ){} }'''
        expect = '''Program([ClassDecl(Id(J_),Id(_),[MethodDecl(Id(Constructor),Instance,[],Block([])),AttributeDecl(Static,VarDecl(Id($u_),ArrayType(3,FloatType))),MethodDecl(Id(Constructor),Instance,[param(Id(P),ClassType(Id(_))),param(Id(_),StringType),param(Id(a),StringType),param(Id(T),StringType),param(Id(X_Y_wp),FloatType),param(Id(_),ClassType(Id(_))),param(Id(t),ClassType(Id(_))),param(Id(_),ClassType(Id(_))),param(Id(_2J),ArrayType(61,FloatType))],Block([])),MethodDecl(Id(Constructor),Instance,[param(Id(hg),ClassType(Id(S))),param(Id(d),ClassType(Id(S))),param(Id(_),ClassType(Id(S))),param(Id(_),ClassType(Id(S))),param(Id(V),ClassType(Id(S))),param(Id(_),ClassType(Id(_Q))),param(Id(d__),ClassType(Id(_Q))),param(Id(SV),ClassType(Id(_Q)))],Block([])),MethodDecl(Id(I),Instance,[],Block([]))]),ClassDecl(Id(o1),Id(_),[MethodDecl(Id($_),Static,[param(Id(_),FloatType),param(Id(_06),FloatType),param(Id(_1_),FloatType),param(Id(_),FloatType),param(Id(_j4),FloatType),param(Id(__),FloatType),param(Id(t),StringType),param(Id(_),StringType)],Block([]))])])'''
        self.assertTrue(TestAST.test(input, expect, 491))

    def test_complex_program42(self):
        input = '''Class i:m{}Class t:Yo_{}Class w4:__42{Var C5X,$_,$2,$_,$_5,$7F:Array [Array [Array [Array [Array [Array [Array [Array [String ,0X38],0X58],0x7],0x3D],0X4],5],0b1_00],0x3D];Destructor (){Var s_:J_;}_u(___5,__:String ;ES:C48){Val _,Or__,n2_8:_;Break ;}Var D_:Boolean ;}'''
        expect = '''Program([ClassDecl(Id(i),Id(m),[]),ClassDecl(Id(t),Id(Yo_),[]),ClassDecl(Id(w4),Id(__42),[AttributeDecl(Instance,VarDecl(Id(C5X),ArrayType(61,ArrayType(4,ArrayType(5,ArrayType(4,ArrayType(61,ArrayType(7,ArrayType(88,ArrayType(56,StringType)))))))))),AttributeDecl(Static,VarDecl(Id($_),ArrayType(61,ArrayType(4,ArrayType(5,ArrayType(4,ArrayType(61,ArrayType(7,ArrayType(88,ArrayType(56,StringType)))))))))),AttributeDecl(Static,VarDecl(Id($2),ArrayType(61,ArrayType(4,ArrayType(5,ArrayType(4,ArrayType(61,ArrayType(7,ArrayType(88,ArrayType(56,StringType)))))))))),AttributeDecl(Static,VarDecl(Id($_),ArrayType(61,ArrayType(4,ArrayType(5,ArrayType(4,ArrayType(61,ArrayType(7,ArrayType(88,ArrayType(56,StringType)))))))))),AttributeDecl(Static,VarDecl(Id($_5),ArrayType(61,ArrayType(4,ArrayType(5,ArrayType(4,ArrayType(61,ArrayType(7,ArrayType(88,ArrayType(56,StringType)))))))))),AttributeDecl(Static,VarDecl(Id($7F),ArrayType(61,ArrayType(4,ArrayType(5,ArrayType(4,ArrayType(61,ArrayType(7,ArrayType(88,ArrayType(56,StringType)))))))))),MethodDecl(Id(Destructor),Instance,[],Block([VarDecl(Id(s_),ClassType(Id(J_)),NullLiteral())])),MethodDecl(Id(_u),Instance,[param(Id(___5),StringType),param(Id(__),StringType),param(Id(ES),ClassType(Id(C48)))],Block([ConstDecl(Id(_),ClassType(Id(_)),None),ConstDecl(Id(Or__),ClassType(Id(_)),None),ConstDecl(Id(n2_8),ClassType(Id(_)),None),Break])),AttributeDecl(Instance,VarDecl(Id(D_),BoolType))])])'''
        self.assertTrue(TestAST.test(input, expect, 492))

    def test_complex_program43(self):
        input = '''Class _:j_D{$q(__,D:Int ;A:_;__,v8,_:Float ){}_2__(Fw_,_,_6,_,_nh,_,g,_:_o;_P,v,A6,U_:Array [Array [Array [Boolean ,0x45],0b1100000],0b1100000];_,_:Boolean ;_:Array [Int ,4]){}Destructor (){} }Class H7{}Class R2__9:j{_(){} }'''
        expect = '''Program([ClassDecl(Id(_),Id(j_D),[MethodDecl(Id($q),Static,[param(Id(__),IntType),param(Id(D),IntType),param(Id(A),ClassType(Id(_))),param(Id(__),FloatType),param(Id(v8),FloatType),param(Id(_),FloatType)],Block([])),MethodDecl(Id(_2__),Instance,[param(Id(Fw_),ClassType(Id(_o))),param(Id(_),ClassType(Id(_o))),param(Id(_6),ClassType(Id(_o))),param(Id(_),ClassType(Id(_o))),param(Id(_nh),ClassType(Id(_o))),param(Id(_),ClassType(Id(_o))),param(Id(g),ClassType(Id(_o))),param(Id(_),ClassType(Id(_o))),param(Id(_P),ArrayType(96,ArrayType(96,ArrayType(69,BoolType)))),param(Id(v),ArrayType(96,ArrayType(96,ArrayType(69,BoolType)))),param(Id(A6),ArrayType(96,ArrayType(96,ArrayType(69,BoolType)))),param(Id(U_),ArrayType(96,ArrayType(96,ArrayType(69,BoolType)))),param(Id(_),BoolType),param(Id(_),BoolType),param(Id(_),ArrayType(4,IntType))],Block([])),MethodDecl(Id(Destructor),Instance,[],Block([]))]),ClassDecl(Id(H7),[]),ClassDecl(Id(R2__9),Id(j),[MethodDecl(Id(_),Instance,[],Block([]))])])'''
        self.assertTrue(TestAST.test(input, expect, 493))

    def test_complex_program44(self):
        input = '''Class _:_{Destructor (){} }Class _38_:__{}Class y{}Class _:z8{_(_,l_:Array [Array [Int ,68],1];_:_75;__,_P:String ;_:Boolean ){} }Class UZ6{Constructor (P3:k_0_){Break ;}Destructor (){} }'''
        expect = '''Program([ClassDecl(Id(_),Id(_),[MethodDecl(Id(Destructor),Instance,[],Block([]))]),ClassDecl(Id(_38_),Id(__),[]),ClassDecl(Id(y),[]),ClassDecl(Id(_),Id(z8),[MethodDecl(Id(_),Instance,[param(Id(_),ArrayType(1,ArrayType(68,IntType))),param(Id(l_),ArrayType(1,ArrayType(68,IntType))),param(Id(_),ClassType(Id(_75))),param(Id(__),StringType),param(Id(_P),StringType),param(Id(_),BoolType)],Block([]))]),ClassDecl(Id(UZ6),[MethodDecl(Id(Constructor),Instance,[param(Id(P3),ClassType(Id(k_0_)))],Block([Break])),MethodDecl(Id(Destructor),Instance,[],Block([]))])])'''
        self.assertTrue(TestAST.test(input, expect, 494))

    def test_complex_program45(self):
        input = '''Class _:_{}Class _2W98{Destructor (){Continue ;}Val _6_:o_;}Class _:_882{Val _C_,$1_c,$4Pj,B4,$P,__:GE;}Class _{Var _q,l,_,u,$_T__8x,_p:Array [Array [Array [Int ,0B111000],69],0b1000101];}Class ___{}'''
        expect = '''Program([ClassDecl(Id(_),Id(_),[]),ClassDecl(Id(_2W98),[MethodDecl(Id(Destructor),Instance,[],Block([Continue])),AttributeDecl(Instance,ConstDecl(Id(_6_),ClassType(Id(o_)),None))]),ClassDecl(Id(_),Id(_882),[AttributeDecl(Instance,ConstDecl(Id(_C_),ClassType(Id(GE)),None)),AttributeDecl(Static,ConstDecl(Id($1_c),ClassType(Id(GE)),None)),AttributeDecl(Static,ConstDecl(Id($4Pj),ClassType(Id(GE)),None)),AttributeDecl(Instance,ConstDecl(Id(B4),ClassType(Id(GE)),None)),AttributeDecl(Static,ConstDecl(Id($P),ClassType(Id(GE)),None)),AttributeDecl(Instance,ConstDecl(Id(__),ClassType(Id(GE)),None))]),ClassDecl(Id(_),[AttributeDecl(Instance,VarDecl(Id(_q),ArrayType(69,ArrayType(69,ArrayType(56,IntType))))),AttributeDecl(Instance,VarDecl(Id(l),ArrayType(69,ArrayType(69,ArrayType(56,IntType))))),AttributeDecl(Instance,VarDecl(Id(_),ArrayType(69,ArrayType(69,ArrayType(56,IntType))))),AttributeDecl(Instance,VarDecl(Id(u),ArrayType(69,ArrayType(69,ArrayType(56,IntType))))),AttributeDecl(Static,VarDecl(Id($_T__8x),ArrayType(69,ArrayType(69,ArrayType(56,IntType))))),AttributeDecl(Instance,VarDecl(Id(_p),ArrayType(69,ArrayType(69,ArrayType(56,IntType)))))]),ClassDecl(Id(___),[])])'''
        self.assertTrue(TestAST.test(input, expect, 495))

    def test_complex_program46(self):
        input = '''Class v{Destructor (){} }Class R_:v7{}Class _c:_{$3(_00_:String ;I1Z_2:r;MS_,F6,_1,V:Array [Float ,0xA];k:Y21;M5b,Pg:O_;I:Int ;q,_7,_,l,_:Array [Int ,23];_9_gy_:Float ;l1,_:Array [Boolean ,0xD_F_3_8];_,__,_:Float ){ {} }}'''
        expect = '''Program([ClassDecl(Id(v),[MethodDecl(Id(Destructor),Instance,[],Block([]))]),ClassDecl(Id(R_),Id(v7),[]),ClassDecl(Id(_c),Id(_),[MethodDecl(Id($3),Static,[param(Id(_00_),StringType),param(Id(I1Z_2),ClassType(Id(r))),param(Id(MS_),ArrayType(10,FloatType)),param(Id(F6),ArrayType(10,FloatType)),param(Id(_1),ArrayType(10,FloatType)),param(Id(V),ArrayType(10,FloatType)),param(Id(k),ClassType(Id(Y21))),param(Id(M5b),ClassType(Id(O_))),param(Id(Pg),ClassType(Id(O_))),param(Id(I),IntType),param(Id(q),ArrayType(23,IntType)),param(Id(_7),ArrayType(23,IntType)),param(Id(_),ArrayType(23,IntType)),param(Id(l),ArrayType(23,IntType)),param(Id(_),ArrayType(23,IntType)),param(Id(_9_gy_),FloatType),param(Id(l1),ArrayType(57144,BoolType)),param(Id(_),ArrayType(57144,BoolType)),param(Id(_),FloatType),param(Id(__),FloatType),param(Id(_),FloatType)],Block([Block([])]))])])'''
        self.assertTrue(TestAST.test(input, expect, 496))

    def test_complex_program47(self):
        input = '''Class _:_{___(_365:Array [Float ,0B1_0_0_1];L:_A9){} }Class _:nre49_{}Class __:_k5{Constructor (_d3_:__){} }Class X{}Class I_6{Constructor (qdT,O:Float ){}Var d,$X:Array [Boolean ,01_023];}'''
        expect = '''Program([ClassDecl(Id(_),Id(_),[MethodDecl(Id(___),Instance,[param(Id(_365),ArrayType(9,FloatType)),param(Id(L),ClassType(Id(_A9)))],Block([]))]),ClassDecl(Id(_),Id(nre49_),[]),ClassDecl(Id(__),Id(_k5),[MethodDecl(Id(Constructor),Instance,[param(Id(_d3_),ClassType(Id(__)))],Block([]))]),ClassDecl(Id(X),[]),ClassDecl(Id(I_6),[MethodDecl(Id(Constructor),Instance,[param(Id(qdT),FloatType),param(Id(O),FloatType)],Block([])),AttributeDecl(Instance,VarDecl(Id(d),ArrayType(531,BoolType))),AttributeDecl(Static,VarDecl(Id($X),ArrayType(531,BoolType)))])])'''
        self.assertTrue(TestAST.test(input, expect, 497))

    def test_complex_program48(self):
        input = '''Class h{$9(_:L){}x(WON7e_:_){ {}Continue ;}Val _,H,__8,_,$_,w:Boolean ;}Class _:_o89{Var __A7,f,$zB,$0_:String ;Constructor (mf,l_sJ_,_:_){}Destructor (){} }Class E_:_{}'''
        expect = '''Program([ClassDecl(Id(h),[MethodDecl(Id($9),Static,[param(Id(_),ClassType(Id(L)))],Block([])),MethodDecl(Id(x),Instance,[param(Id(WON7e_),ClassType(Id(_)))],Block([Block([]),Continue])),AttributeDecl(Instance,ConstDecl(Id(_),BoolType,None)),AttributeDecl(Instance,ConstDecl(Id(H),BoolType,None)),AttributeDecl(Instance,ConstDecl(Id(__8),BoolType,None)),AttributeDecl(Instance,ConstDecl(Id(_),BoolType,None)),AttributeDecl(Static,ConstDecl(Id($_),BoolType,None)),AttributeDecl(Instance,ConstDecl(Id(w),BoolType,None))]),ClassDecl(Id(_),Id(_o89),[AttributeDecl(Instance,VarDecl(Id(__A7),StringType)),AttributeDecl(Instance,VarDecl(Id(f),StringType)),AttributeDecl(Static,VarDecl(Id($zB),StringType)),AttributeDecl(Static,VarDecl(Id($0_),StringType)),MethodDecl(Id(Constructor),Instance,[param(Id(mf),ClassType(Id(_))),param(Id(l_sJ_),ClassType(Id(_))),param(Id(_),ClassType(Id(_)))],Block([])),MethodDecl(Id(Destructor),Instance,[],Block([]))]),ClassDecl(Id(E_),Id(_),[])])'''
        self.assertTrue(TestAST.test(input, expect, 498))

    def test_complex_program49(self):
        input = '''Class g_{Var $_:Array [Float ,25];Val _RA50j:Float ;}Class k{}Class o:__{}Class i8{}Class _:Y{Constructor (m,r,__,B:_;p_,_,_u1o_,_,v,B_0:String ){Continue ;}Var _h__,Qd_:Array [Array [Array [Boolean ,0x1_E],0b1110],06];Constructor (jf_:_6_;_58:_06){} }'''
        expect = '''Program([ClassDecl(Id(g_),[AttributeDecl(Static,VarDecl(Id($_),ArrayType(25,FloatType))),AttributeDecl(Instance,ConstDecl(Id(_RA50j),FloatType,None))]),ClassDecl(Id(k),[]),ClassDecl(Id(o),Id(__),[]),ClassDecl(Id(i8),[]),ClassDecl(Id(_),Id(Y),[MethodDecl(Id(Constructor),Instance,[param(Id(m),ClassType(Id(_))),param(Id(r),ClassType(Id(_))),param(Id(__),ClassType(Id(_))),param(Id(B),ClassType(Id(_))),param(Id(p_),StringType),param(Id(_),StringType),param(Id(_u1o_),StringType),param(Id(_),StringType),param(Id(v),StringType),param(Id(B_0),StringType)],Block([Continue])),AttributeDecl(Instance,VarDecl(Id(_h__),ArrayType(6,ArrayType(14,ArrayType(30,BoolType))))),AttributeDecl(Instance,VarDecl(Id(Qd_),ArrayType(6,ArrayType(14,ArrayType(30,BoolType))))),MethodDecl(Id(Constructor),Instance,[param(Id(jf_),ClassType(Id(_6_))),param(Id(_58),ClassType(Id(_06)))],Block([]))])])'''
        self.assertTrue(TestAST.test(input, expect, 499))