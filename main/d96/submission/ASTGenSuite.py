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
    AttributeDecl(Instance(), VarDecl( Id('b'), IntType(), IntLiteral('51966') )),
    AttributeDecl(Static(), ConstDecl( Id('$c'), FloatType(), FloatLiteral('3.141592653589') )),
    AttributeDecl(Static(), VarDecl( Id('$d'), BoolType(), BooleanLiteral('True') )),
    AttributeDecl(Instance(), ConstDecl( Id('e'), StringType(), StringLiteral('first') )),
    AttributeDecl(Static(), ConstDecl( Id('$f'), StringType(), StringLiteral('second') ))
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
    AttributeDecl(Instance(), ConstDecl( Id('c'), IntType(), BinaryOp('+',BinaryOp('+',IntLiteral('83'),BinaryOp('*',IntLiteral('51966'),IntLiteral('9'))),IntLiteral('1000')))),
    AttributeDecl(Static(), VarDecl( Id('$c'), IntType(), BinaryOp('/',Id('a'),Id('b'))))
])
]))
        self.assertTrue(TestAST.test(input,expect,305))

    
#     def test_primitivetype_attributes5(self):
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

    
    def test_primitivetype_attributes6(self):
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
    AttributeDecl(Static(), VarDecl( Id('$g'), BoolType(), BinaryOp('==.',BinaryOp('+.',StringLiteral('hello'),StringLiteral('world')),StringLiteral('helloworld')) )),
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
                        ArrayLiteral([StringLiteral('hello'), StringLiteral('world'), BinaryOp('+.', StringLiteral('hello'), StringLiteral('world'))])))
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
    AttributeDecl(Instance(), VarDecl(Id('x'), ClassType(Id('_class')), NullLiteral())),
    AttributeDecl(Static(), VarDecl(Id('$x'), ClassType(Id('_class')), NullLiteral())),
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
    AttributeDecl(Instance(), VarDecl(Id('obj'), ClassType(Id('_class')), NullLiteral())),
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
            StringLiteral('an object'))
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
        ConstDecl( Id('e'), IntType(), BinaryOp('+',BinaryOp('+',IntLiteral('83'),BinaryOp('*',IntLiteral('51966'),IntLiteral('9'))),IntLiteral('1000')) ),
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
        VarDecl( Id('i'), BoolType(), BinaryOp('==.',BinaryOp('+.',StringLiteral('hello'),StringLiteral('world')),StringLiteral('helloworld')) ),
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
    
    
    def test_if_statements6(self):
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
    

    def test_complex_program1(self):
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
    

    def test_complex_program2(self):
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


    def test_complex_program3(self):
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


    def test_complex_program4(self):
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



    def test_complex_program5(self):
        line = '''Class _:__{Destructor (){} }Class J{Destructor (){}Constructor (Nk,__7_:Array [Array [Array [Boolean ,0b1],047],0B1]){} }Class _{}Class _1{Destructor (){}Destructor (){} }'''
        expect = '''Program([ClassDecl(Id(_),Id(__),[MethodDecl(Id(Destructor),Instance,[],Block([]))]),ClassDecl(Id(J),[MethodDecl(Id(Destructor),Instance,[],Block([])),MethodDecl(Id(Constructor),Instance,[param(Id(Nk),ArrayType(1,ArrayType(39,ArrayType(1,BoolType)))),param(Id(__7_),ArrayType(1,ArrayType(39,ArrayType(1,BoolType))))],Block([]))]),ClassDecl(Id(_),[]),ClassDecl(Id(_1),[MethodDecl(Id(Destructor),Instance,[],Block([])),MethodDecl(Id(Destructor),Instance,[],Block([]))])])'''
        self.assertTrue(TestAST.test(line, expect, 355))

    def test_complex_program6(self):
        line = '''Class f{}Class _:_{$_12F5(){} }Class __cl{Var $_B_0b,_t,$h0,$_,_6H_:f;}Class __6:_64{}Class ti8{Var P2c:Array [Array [Array [Boolean ,04_3_2],0x48],36];}Class _5K5{Constructor (){} }Class _A:M___{}'''
        expect = '''Program([ClassDecl(Id(f),[]),ClassDecl(Id(_),Id(_),[MethodDecl(Id($_12F5),Static,[],Block([]))]),ClassDecl(Id(__cl),[AttributeDecl(Static,VarDecl(Id($_B_0b),ClassType(Id(f)),NullLiteral())),AttributeDecl(Instance,VarDecl(Id(_t),ClassType(Id(f)),NullLiteral())),AttributeDecl(Static,VarDecl(Id($h0),ClassType(Id(f)),NullLiteral())),AttributeDecl(Static,VarDecl(Id($_),ClassType(Id(f)),NullLiteral())),AttributeDecl(Instance,VarDecl(Id(_6H_),ClassType(Id(f)),NullLiteral()))]),ClassDecl(Id(__6),Id(_64),[]),ClassDecl(Id(ti8),[AttributeDecl(Instance,VarDecl(Id(P2c),ArrayType(36,ArrayType(72,ArrayType(282,BoolType)))))]),ClassDecl(Id(_5K5),[MethodDecl(Id(Constructor),Instance,[],Block([]))]),ClassDecl(Id(_A),Id(M___),[])])'''
        self.assertTrue(TestAST.test(line, expect, 356))

    def test_complex_program7(self):
        line = '''Class _:_{}Class J_:O{Destructor (){}__(_:String ;_x__,_:Float ;_:Array [Array [Array [Float ,0x1],0b1_1_1],0x47];U:Array [Array [Float ,06_6],0B111110];_:_){}$__(V:v;_N_:N){Continue ;} }'''
        expect = '''Program([ClassDecl(Id(_),Id(_),[]),ClassDecl(Id(J_),Id(O),[MethodDecl(Id(Destructor),Instance,[],Block([])),MethodDecl(Id(__),Instance,[param(Id(_),StringType),param(Id(_x__),FloatType),param(Id(_),FloatType),param(Id(_),ArrayType(71,ArrayType(7,ArrayType(1,FloatType)))),param(Id(U),ArrayType(62,ArrayType(54,FloatType))),param(Id(_),ClassType(Id(_)))],Block([])),MethodDecl(Id($__),Static,[param(Id(V),ClassType(Id(v))),param(Id(_N_),ClassType(Id(N)))],Block([Continue]))])])'''
        self.assertTrue(TestAST.test(line, expect, 357))

    def test_complex_program8(self):
        line = '''Class _51W_:a{$4(l:Int ;_5:String ;__,_:Array [String ,0X48];_,e,_9n,g_:Array [Boolean ,86];_,K:Array [String ,0b101111];B__D4_,Rr4,W:String ;m,n_,_,_:Boolean ;p,i:Array [Boolean ,0xD]){} }'''
        expect = '''Program([ClassDecl(Id(_51W_),Id(a),[MethodDecl(Id($4),Static,[param(Id(l),IntType),param(Id(_5),StringType),param(Id(__),ArrayType(72,StringType)),param(Id(_),ArrayType(72,StringType)),param(Id(_),ArrayType(86,BoolType)),param(Id(e),ArrayType(86,BoolType)),param(Id(_9n),ArrayType(86,BoolType)),param(Id(g_),ArrayType(86,BoolType)),param(Id(_),ArrayType(47,StringType)),param(Id(K),ArrayType(47,StringType)),param(Id(B__D4_),StringType),param(Id(Rr4),StringType),param(Id(W),StringType),param(Id(m),BoolType),param(Id(n_),BoolType),param(Id(_),BoolType),param(Id(_),BoolType),param(Id(p),ArrayType(13,BoolType)),param(Id(i),ArrayType(13,BoolType))],Block([]))])])'''
        self.assertTrue(TestAST.test(line, expect, 358))

    def test_complex_program9(self):
        line = '''Class k7:_1{}Class X{Val $__E3,NH,L,_,$o_5,e242:Array [Array [Array [Array [Boolean ,03],0xA],0X4B_49],1];}Class R517673__o__:_{}Class T:_TE_{}Class jra{}Class _:d{}'''
        expect = '''Program([ClassDecl(Id(k7),Id(_1),[]),ClassDecl(Id(X),[AttributeDecl(Static,ConstDecl(Id($__E3),ArrayType(1,ArrayType(19273,ArrayType(10,ArrayType(3,BoolType)))),None)),AttributeDecl(Instance,ConstDecl(Id(NH),ArrayType(1,ArrayType(19273,ArrayType(10,ArrayType(3,BoolType)))),None)),AttributeDecl(Instance,ConstDecl(Id(L),ArrayType(1,ArrayType(19273,ArrayType(10,ArrayType(3,BoolType)))),None)),AttributeDecl(Instance,ConstDecl(Id(_),ArrayType(1,ArrayType(19273,ArrayType(10,ArrayType(3,BoolType)))),None)),AttributeDecl(Static,ConstDecl(Id($o_5),ArrayType(1,ArrayType(19273,ArrayType(10,ArrayType(3,BoolType)))),None)),AttributeDecl(Instance,ConstDecl(Id(e242),ArrayType(1,ArrayType(19273,ArrayType(10,ArrayType(3,BoolType)))),None))]),ClassDecl(Id(R517673__o__),Id(_),[]),ClassDecl(Id(T),Id(_TE_),[]),ClassDecl(Id(jra),[]),ClassDecl(Id(_),Id(d),[])])'''
        self.assertTrue(TestAST.test(line, expect, 359))

    def test_complex_program10(self):
        line = '''Class _L{}Class _:__7{G(E77,_46,J:J;j,b,g,_:H7G){Break ;} }Class _:_8{o11A(fc,a_:Array [Array [Float ,92],92];_0_:W;_:Array [Boolean ,042];_4_:Array [Array [Boolean ,0B10101],0X26]){} }'''
        expect = '''Program([ClassDecl(Id(_L),[]),ClassDecl(Id(_),Id(__7),[MethodDecl(Id(G),Instance,[param(Id(E77),ClassType(Id(J))),param(Id(_46),ClassType(Id(J))),param(Id(J),ClassType(Id(J))),param(Id(j),ClassType(Id(H7G))),param(Id(b),ClassType(Id(H7G))),param(Id(g),ClassType(Id(H7G))),param(Id(_),ClassType(Id(H7G)))],Block([Break]))]),ClassDecl(Id(_),Id(_8),[MethodDecl(Id(o11A),Instance,[param(Id(fc),ArrayType(92,ArrayType(92,FloatType))),param(Id(a_),ArrayType(92,ArrayType(92,FloatType))),param(Id(_0_),ClassType(Id(W))),param(Id(_),ArrayType(34,BoolType)),param(Id(_4_),ArrayType(38,ArrayType(21,BoolType)))],Block([]))])])'''
        self.assertTrue(TestAST.test(line, expect, 360))

    def test_complex_program11(self):
        line = '''Class W{}Class J58:S3{Constructor (_:___;__,_1,V,G,QO,F__7__i:Array [Boolean ,0X34];_s,_5_c_:Array [Array [Array [Array [Array [Boolean ,0x18],0X34],0b1],0x18],3]){} }'''
        expect = '''Program([ClassDecl(Id(W),[]),ClassDecl(Id(J58),Id(S3),[MethodDecl(Id(Constructor),Instance,[param(Id(_),ClassType(Id(___))),param(Id(__),ArrayType(52,BoolType)),param(Id(_1),ArrayType(52,BoolType)),param(Id(V),ArrayType(52,BoolType)),param(Id(G),ArrayType(52,BoolType)),param(Id(QO),ArrayType(52,BoolType)),param(Id(F__7__i),ArrayType(52,BoolType)),param(Id(_s),ArrayType(3,ArrayType(24,ArrayType(1,ArrayType(52,ArrayType(24,BoolType)))))),param(Id(_5_c_),ArrayType(3,ArrayType(24,ArrayType(1,ArrayType(52,ArrayType(24,BoolType))))))],Block([]))])])'''
        self.assertTrue(TestAST.test(line, expect, 361))

    def test_complex_program12(self):
        line = '''Class T0{$72DF(_,_y:qP;_3_:Int ;F4:Float ;J:Float ;l:Array [String ,0x4];_,YZg,P:Array [String ,0103]){}Var $38,_,__A,_p,B:Array [Array [Boolean ,80],0b1000000];Destructor (){} }'''
        expect = '''Program([ClassDecl(Id(T0),[MethodDecl(Id($72DF),Static,[param(Id(_),ClassType(Id(qP))),param(Id(_y),ClassType(Id(qP))),param(Id(_3_),IntType),param(Id(F4),FloatType),param(Id(J),FloatType),param(Id(l),ArrayType(4,StringType)),param(Id(_),ArrayType(67,StringType)),param(Id(YZg),ArrayType(67,StringType)),param(Id(P),ArrayType(67,StringType))],Block([])),AttributeDecl(Static,VarDecl(Id($38),ArrayType(64,ArrayType(80,BoolType)))),AttributeDecl(Instance,VarDecl(Id(_),ArrayType(64,ArrayType(80,BoolType)))),AttributeDecl(Instance,VarDecl(Id(__A),ArrayType(64,ArrayType(80,BoolType)))),AttributeDecl(Instance,VarDecl(Id(_p),ArrayType(64,ArrayType(80,BoolType)))),AttributeDecl(Instance,VarDecl(Id(B),ArrayType(64,ArrayType(80,BoolType)))),MethodDecl(Id(Destructor),Instance,[],Block([]))])])'''
        self.assertTrue(TestAST.test(line, expect, 362))

    def test_complex_program13(self):
        line = '''Class A:B4_28{Constructor (o_:Array [Array [Float ,61],0B1];L__:_v;l:Array [String ,0x3A];C:Array [Array [Array [Array [Int ,06_10],0b10110],556],05_214_5]){} }Class B__:V{Constructor (){Break ;} }Class d:_3__{}Class y{Destructor (){} }'''
        expect = '''Program([ClassDecl(Id(A),Id(B4_28),[MethodDecl(Id(Constructor),Instance,[param(Id(o_),ArrayType(1,ArrayType(61,FloatType))),param(Id(L__),ClassType(Id(_v))),param(Id(l),ArrayType(58,StringType)),param(Id(C),ArrayType(21605,ArrayType(556,ArrayType(22,ArrayType(392,IntType)))))],Block([]))]),ClassDecl(Id(B__),Id(V),[MethodDecl(Id(Constructor),Instance,[],Block([Break]))]),ClassDecl(Id(d),Id(_3__),[]),ClassDecl(Id(y),[MethodDecl(Id(Destructor),Instance,[],Block([]))])])'''
        self.assertTrue(TestAST.test(line, expect, 363))

    def test_complex_program14(self):
        line = '''Class p_:_71{_(){} }Class _{Constructor (_:A2y_;f,s:__){Z__o::$z_._.Y_.C_()._._4().O_.Y();}Constructor (){} }Class __{$_(){}Constructor (__16:Array [Array [Array [String ,0130],04],0130]){} }Class u_x{}'''
        expect = '''Program([ClassDecl(Id(p_),Id(_71),[MethodDecl(Id(_),Instance,[],Block([]))]),ClassDecl(Id(_),[MethodDecl(Id(Constructor),Instance,[param(Id(_),ClassType(Id(A2y_))),param(Id(f),ClassType(Id(__))),param(Id(s),ClassType(Id(__)))],Block([Call(FieldAccess(CallExpr(FieldAccess(CallExpr(FieldAccess(FieldAccess(FieldAccess(Id(Z__o),Id($z_)),Id(_)),Id(Y_)),Id(C_),[]),Id(_)),Id(_4),[]),Id(O_)),Id(Y),[])])),MethodDecl(Id(Constructor),Instance,[],Block([]))]),ClassDecl(Id(__),[MethodDecl(Id($_),Static,[],Block([])),MethodDecl(Id(Constructor),Instance,[param(Id(__16),ArrayType(88,ArrayType(4,ArrayType(88,StringType))))],Block([]))]),ClassDecl(Id(u_x),[])])'''
        self.assertTrue(TestAST.test(line, expect, 364))

    def test_complex_program15(self):
        line = '''Class _Z4{}Class oR_{$fW(){}Destructor (){Var Z,c:Array [Array [Array [Array [Array [Array [Array [String ,074_64],02],49],0X46],0XE],0133],03];Continue ;}$3(X0_8:String ;_u2_,y6_,_,N46PH:String ){}Constructor (){} }'''
        expect = '''Program([ClassDecl(Id(_Z4),[]),ClassDecl(Id(oR_),[MethodDecl(Id($fW),Static,[],Block([])),MethodDecl(Id(Destructor),Instance,[],Block([VarDecl(Id(Z),ArrayType(3,ArrayType(91,ArrayType(14,ArrayType(70,ArrayType(49,ArrayType(2,ArrayType(3892,StringType)))))))),VarDecl(Id(c),ArrayType(3,ArrayType(91,ArrayType(14,ArrayType(70,ArrayType(49,ArrayType(2,ArrayType(3892,StringType)))))))),Continue])),MethodDecl(Id($3),Static,[param(Id(X0_8),StringType),param(Id(_u2_),StringType),param(Id(y6_),StringType),param(Id(_),StringType),param(Id(N46PH),StringType)],Block([])),MethodDecl(Id(Constructor),Instance,[],Block([]))])])'''
        self.assertTrue(TestAST.test(line, expect, 365))

    def test_complex_program16(self):
        line = '''Class _p_:_m{}Class Y{Constructor (o,K:Array [Array [Array [Array [Array [Boolean ,7_3],38_8_21],3_8_5_1_645_1],8],9];_:r;z,_71,_,_:Array [Array [Float ,19],0b101001];b_3f5,m,BS74:Array [Array [Array [Boolean ,046],0X30],046];_ZF8,_2:D1;o:Float ){} }Class Hv{}Class e__:Lz88{}'''
        expect = '''Program([ClassDecl(Id(_p_),Id(_m),[]),ClassDecl(Id(Y),[MethodDecl(Id(Constructor),Instance,[param(Id(o),ArrayType(9,ArrayType(8,ArrayType(38516451,ArrayType(38821,ArrayType(73,BoolType)))))),param(Id(K),ArrayType(9,ArrayType(8,ArrayType(38516451,ArrayType(38821,ArrayType(73,BoolType)))))),param(Id(_),ClassType(Id(r))),param(Id(z),ArrayType(41,ArrayType(19,FloatType))),param(Id(_71),ArrayType(41,ArrayType(19,FloatType))),param(Id(_),ArrayType(41,ArrayType(19,FloatType))),param(Id(_),ArrayType(41,ArrayType(19,FloatType))),param(Id(b_3f5),ArrayType(38,ArrayType(48,ArrayType(38,BoolType)))),param(Id(m),ArrayType(38,ArrayType(48,ArrayType(38,BoolType)))),param(Id(BS74),ArrayType(38,ArrayType(48,ArrayType(38,BoolType)))),param(Id(_ZF8),ClassType(Id(D1))),param(Id(_2),ClassType(Id(D1))),param(Id(o),FloatType)],Block([]))]),ClassDecl(Id(Hv),[]),ClassDecl(Id(e__),Id(Lz88),[])])'''
        self.assertTrue(TestAST.test(line, expect, 366))

    def test_complex_program17(self):
        line = '''Class rB_:_6{$2a(_6:Array [Array [Array [Array [Array [String ,06],0x5_1],057],0B1001011],69_12_9];F44_5,_,A,Ia:Array [Array [Array [Array [String ,32],0X30],0X1_2],0x7_7_6]){} }Class c_i:__{}'''
        expect = '''Program([ClassDecl(Id(rB_),Id(_6),[MethodDecl(Id($2a),Static,[param(Id(_6),ArrayType(69129,ArrayType(75,ArrayType(47,ArrayType(81,ArrayType(6,StringType)))))),param(Id(F44_5),ArrayType(1910,ArrayType(18,ArrayType(48,ArrayType(32,StringType))))),param(Id(_),ArrayType(1910,ArrayType(18,ArrayType(48,ArrayType(32,StringType))))),param(Id(A),ArrayType(1910,ArrayType(18,ArrayType(48,ArrayType(32,StringType))))),param(Id(Ia),ArrayType(1910,ArrayType(18,ArrayType(48,ArrayType(32,StringType)))))],Block([]))]),ClassDecl(Id(c_i),Id(__),[])])'''
        self.assertTrue(TestAST.test(line, expect, 367))

    def test_complex_program18(self):
        line = '''Class _{Val _,$30,_,y:Array [Array [Array [Float ,0753_7],0X42],109];$_d3__S(_0,_,N_,k:Array [Int ,0B1000101]){}Destructor (){}Val $R7_,_:Boolean ;Var W1:_;Val $_93,$_4,_,$_3,$6_:_;}'''
        expect = '''Program([ClassDecl(Id(_),[AttributeDecl(Instance,ConstDecl(Id(_),ArrayType(109,ArrayType(66,ArrayType(3935,FloatType))),None)),AttributeDecl(Static,ConstDecl(Id($30),ArrayType(109,ArrayType(66,ArrayType(3935,FloatType))),None)),AttributeDecl(Instance,ConstDecl(Id(_),ArrayType(109,ArrayType(66,ArrayType(3935,FloatType))),None)),AttributeDecl(Instance,ConstDecl(Id(y),ArrayType(109,ArrayType(66,ArrayType(3935,FloatType))),None)),MethodDecl(Id($_d3__S),Static,[param(Id(_0),ArrayType(69,IntType)),param(Id(_),ArrayType(69,IntType)),param(Id(N_),ArrayType(69,IntType)),param(Id(k),ArrayType(69,IntType))],Block([])),MethodDecl(Id(Destructor),Instance,[],Block([])),AttributeDecl(Static,ConstDecl(Id($R7_),BoolType,None)),AttributeDecl(Instance,ConstDecl(Id(_),BoolType,None)),AttributeDecl(Instance,VarDecl(Id(W1),ClassType(Id(_)),NullLiteral())),AttributeDecl(Static,ConstDecl(Id($_93),ClassType(Id(_)),NullLiteral())),AttributeDecl(Static,ConstDecl(Id($_4),ClassType(Id(_)),NullLiteral())),AttributeDecl(Instance,ConstDecl(Id(_),ClassType(Id(_)),NullLiteral())),AttributeDecl(Static,ConstDecl(Id($_3),ClassType(Id(_)),NullLiteral())),AttributeDecl(Static,ConstDecl(Id($6_),ClassType(Id(_)),NullLiteral()))])])'''
        self.assertTrue(TestAST.test(line, expect, 368))

    def test_complex_program19(self):
        line = '''Class __n{}Class _23{Constructor (s1J,_86,H__5:Array [Array [Array [Boolean ,9],05],50];r___,_I:_;_HQ_b,G7,oA8:Boolean ;d71_:String ;_:String ;Tr,x,X:Array [Array [Float ,2_200],052];X,_:Array [Array [Array [Array [Array [Array [Boolean ,0b110001],0101],0X56],50],0x61],04];Y:g){ {} }Destructor (){} }'''
        expect = '''Program([ClassDecl(Id(__n),[]),ClassDecl(Id(_23),[MethodDecl(Id(Constructor),Instance,[param(Id(s1J),ArrayType(50,ArrayType(5,ArrayType(9,BoolType)))),param(Id(_86),ArrayType(50,ArrayType(5,ArrayType(9,BoolType)))),param(Id(H__5),ArrayType(50,ArrayType(5,ArrayType(9,BoolType)))),param(Id(r___),ClassType(Id(_))),param(Id(_I),ClassType(Id(_))),param(Id(_HQ_b),BoolType),param(Id(G7),BoolType),param(Id(oA8),BoolType),param(Id(d71_),StringType),param(Id(_),StringType),param(Id(Tr),ArrayType(42,ArrayType(2200,FloatType))),param(Id(x),ArrayType(42,ArrayType(2200,FloatType))),param(Id(X),ArrayType(42,ArrayType(2200,FloatType))),param(Id(X),ArrayType(4,ArrayType(97,ArrayType(50,ArrayType(86,ArrayType(65,ArrayType(49,BoolType))))))),param(Id(_),ArrayType(4,ArrayType(97,ArrayType(50,ArrayType(86,ArrayType(65,ArrayType(49,BoolType))))))),param(Id(Y),ClassType(Id(g)))],Block([Block([])])),MethodDecl(Id(Destructor),Instance,[],Block([]))])])'''
        self.assertTrue(TestAST.test(line, expect, 369))

    def test_complex_program20(self):
        line = '''Class __{Var _:Array [Float ,0B101010];}Class _:_{Var $3_,__9O,$_8:mE_5D;}Class h:w51{}Class _6Fd{$s57(_4:_;_,_E,__2P_m2,_,uf_,W:Boolean ){}Val _,$2S,$L:Array [String ,0X21];}'''
        expect = '''Program([ClassDecl(Id(__),[AttributeDecl(Instance,VarDecl(Id(_),ArrayType(42,FloatType)))]),ClassDecl(Id(_),Id(_),[AttributeDecl(Static,VarDecl(Id($3_),ClassType(Id(mE_5D)),NullLiteral())),AttributeDecl(Instance,VarDecl(Id(__9O),ClassType(Id(mE_5D)),NullLiteral())),AttributeDecl(Static,VarDecl(Id($_8),ClassType(Id(mE_5D)),NullLiteral()))]),ClassDecl(Id(h),Id(w51),[]),ClassDecl(Id(_6Fd),[MethodDecl(Id($s57),Static,[param(Id(_4),ClassType(Id(_))),param(Id(_),BoolType),param(Id(_E),BoolType),param(Id(__2P_m2),BoolType),param(Id(_),BoolType),param(Id(uf_),BoolType),param(Id(W),BoolType)],Block([])),AttributeDecl(Instance,ConstDecl(Id(_),ArrayType(33,StringType),None)),AttributeDecl(Static,ConstDecl(Id($2S),ArrayType(33,StringType),None)),AttributeDecl(Static,ConstDecl(Id($L),ArrayType(33,StringType),None))])])'''
        self.assertTrue(TestAST.test(line, expect, 370))

    def test_complex_program21(self):
        line = '''Class _{Var $O,_G,$_,$0,$__:Array [Array [Array [Int ,5],0XE],01];Var W7:Array [Boolean ,0B1_0_1_1];Constructor (Ez9:Array [Array [Array [Boolean ,5],0b11110],0b11110];_:Int ;c,K,w____X:Array [Array [Array [Float ,2],021],021];_xvO:String ){}Constructor (){} }'''
        expect = '''Program([ClassDecl(Id(_),[AttributeDecl(Static,VarDecl(Id($O),ArrayType(1,ArrayType(14,ArrayType(5,IntType))))),AttributeDecl(Instance,VarDecl(Id(_G),ArrayType(1,ArrayType(14,ArrayType(5,IntType))))),AttributeDecl(Static,VarDecl(Id($_),ArrayType(1,ArrayType(14,ArrayType(5,IntType))))),AttributeDecl(Static,VarDecl(Id($0),ArrayType(1,ArrayType(14,ArrayType(5,IntType))))),AttributeDecl(Static,VarDecl(Id($__),ArrayType(1,ArrayType(14,ArrayType(5,IntType))))),AttributeDecl(Instance,VarDecl(Id(W7),ArrayType(11,BoolType))),MethodDecl(Id(Constructor),Instance,[param(Id(Ez9),ArrayType(30,ArrayType(30,ArrayType(5,BoolType)))),param(Id(_),IntType),param(Id(c),ArrayType(17,ArrayType(17,ArrayType(2,FloatType)))),param(Id(K),ArrayType(17,ArrayType(17,ArrayType(2,FloatType)))),param(Id(w____X),ArrayType(17,ArrayType(17,ArrayType(2,FloatType)))),param(Id(_xvO),StringType)],Block([])),MethodDecl(Id(Constructor),Instance,[],Block([]))])])'''
        self.assertTrue(TestAST.test(line, expect, 371))

    def test_complex_program22(self):
        line = '''Class N_{$_(W2,i_:Array [Float ,0x20];Y:_0;_04,Z50Ho7__61,_,_:Array [Array [Int ,073],0x20];_:_){}Var $_,$S:V0_;}Class ___2W_4_57:P{}Class Os{}Class _{Val $4,$_5:Float ;Var $5,$A5:_2_t;Var _40:Array [String ,06_37];Destructor (){Break ;} }'''
        expect = '''Program([ClassDecl(Id(N_),[MethodDecl(Id($_),Static,[param(Id(W2),ArrayType(32,FloatType)),param(Id(i_),ArrayType(32,FloatType)),param(Id(Y),ClassType(Id(_0))),param(Id(_04),ArrayType(32,ArrayType(59,IntType))),param(Id(Z50Ho7__61),ArrayType(32,ArrayType(59,IntType))),param(Id(_),ArrayType(32,ArrayType(59,IntType))),param(Id(_),ArrayType(32,ArrayType(59,IntType))),param(Id(_),ClassType(Id(_)))],Block([])),AttributeDecl(Static,VarDecl(Id($_),ClassType(Id(V0_)),NullLiteral())),AttributeDecl(Static,VarDecl(Id($S),ClassType(Id(V0_)),NullLiteral()))]),ClassDecl(Id(___2W_4_57),Id(P),[]),ClassDecl(Id(Os),[]),ClassDecl(Id(_),[AttributeDecl(Static,ConstDecl(Id($4),FloatType,None)),AttributeDecl(Static,ConstDecl(Id($_5),FloatType,None)),AttributeDecl(Static,VarDecl(Id($5),ClassType(Id(_2_t)),NullLiteral())),AttributeDecl(Static,VarDecl(Id($A5),ClassType(Id(_2_t)),NullLiteral())),AttributeDecl(Instance,VarDecl(Id(_40),ArrayType(415,StringType))),MethodDecl(Id(Destructor),Instance,[],Block([Break]))])])'''
        self.assertTrue(TestAST.test(line, expect, 372))

    def test_complex_program23(self):
        line = '''Class Zbp:B{_4_(){}Constructor (x,j,q0a1:Array [Array [Array [Float ,95],06654],95];z7N,Y,n:String ){}Var $6:Array [Array [Array [Boolean ,353_6_4],011_1],0B10];}Class h85:Iy_{Var _,$_b3,__8:Array [Float ,0b1011111];}'''
        expect = '''Program([ClassDecl(Id(Zbp),Id(B),[MethodDecl(Id(_4_),Instance,[],Block([])),MethodDecl(Id(Constructor),Instance,[param(Id(x),ArrayType(95,ArrayType(3500,ArrayType(95,FloatType)))),param(Id(j),ArrayType(95,ArrayType(3500,ArrayType(95,FloatType)))),param(Id(q0a1),ArrayType(95,ArrayType(3500,ArrayType(95,FloatType)))),param(Id(z7N),StringType),param(Id(Y),StringType),param(Id(n),StringType)],Block([])),AttributeDecl(Static,VarDecl(Id($6),ArrayType(2,ArrayType(73,ArrayType(35364,BoolType)))))]),ClassDecl(Id(h85),Id(Iy_),[AttributeDecl(Instance,VarDecl(Id(_),ArrayType(95,FloatType))),AttributeDecl(Static,VarDecl(Id($_b3),ArrayType(95,FloatType))),AttributeDecl(Instance,VarDecl(Id(__8),ArrayType(95,FloatType)))])])'''
        self.assertTrue(TestAST.test(line, expect, 373))

    def test_complex_program24(self):
        line = '''Class jF_:_NS{Constructor (_N,_:Array [Int ,063];_,V,Nt_1:Array [Array [Array [Array [String ,0x5F],063],063],0b1_1];z_:String ){}Constructor (__:_){Val _,_,ZS:String ;}Var $__,_,$A_V_:Int ;}Class _:_7{Constructor (v:a;_6q_l:Array [Boolean ,0x96]){} }Class _B:Hc_{}'''
        expect = '''Program([ClassDecl(Id(jF_),Id(_NS),[MethodDecl(Id(Constructor),Instance,[param(Id(_N),ArrayType(51,IntType)),param(Id(_),ArrayType(51,IntType)),param(Id(_),ArrayType(3,ArrayType(51,ArrayType(51,ArrayType(95,StringType))))),param(Id(V),ArrayType(3,ArrayType(51,ArrayType(51,ArrayType(95,StringType))))),param(Id(Nt_1),ArrayType(3,ArrayType(51,ArrayType(51,ArrayType(95,StringType))))),param(Id(z_),StringType)],Block([])),MethodDecl(Id(Constructor),Instance,[param(Id(__),ClassType(Id(_)))],Block([ConstDecl(Id(_),StringType,None),ConstDecl(Id(_),StringType,None),ConstDecl(Id(ZS),StringType,None)])),AttributeDecl(Static,VarDecl(Id($__),IntType)),AttributeDecl(Instance,VarDecl(Id(_),IntType)),AttributeDecl(Static,VarDecl(Id($A_V_),IntType))]),ClassDecl(Id(_),Id(_7),[MethodDecl(Id(Constructor),Instance,[param(Id(v),ClassType(Id(a))),param(Id(_6q_l),ArrayType(150,BoolType))],Block([]))]),ClassDecl(Id(_B),Id(Hc_),[])])'''
        self.assertTrue(TestAST.test(line, expect, 374))

    def test_complex_program25(self):
        line = '''Class XkGu{}Class _{}Class W{}Class e:N{f(_:Float ){} }Class pyq{Var P_:_09;Constructor (_:C;_,_56,A:Int ;___,_w:Float ;_r1w_,_,_:__;N,wl,_8,y7G:_;m4_:Boolean ){Return ;{} }}Class _:_{}'''
        expect = '''Program([ClassDecl(Id(XkGu),[]),ClassDecl(Id(_),[]),ClassDecl(Id(W),[]),ClassDecl(Id(e),Id(N),[MethodDecl(Id(f),Instance,[param(Id(_),FloatType)],Block([]))]),ClassDecl(Id(pyq),[AttributeDecl(Instance,VarDecl(Id(P_),ClassType(Id(_09)),NullLiteral())),MethodDecl(Id(Constructor),Instance,[param(Id(_),ClassType(Id(C))),param(Id(_),IntType),param(Id(_56),IntType),param(Id(A),IntType),param(Id(___),FloatType),param(Id(_w),FloatType),param(Id(_r1w_),ClassType(Id(__))),param(Id(_),ClassType(Id(__))),param(Id(_),ClassType(Id(__))),param(Id(N),ClassType(Id(_))),param(Id(wl),ClassType(Id(_))),param(Id(_8),ClassType(Id(_))),param(Id(y7G),ClassType(Id(_))),param(Id(m4_),BoolType)],Block([Return(),Block([])]))]),ClassDecl(Id(_),Id(_),[])])'''
        self.assertTrue(TestAST.test(line, expect, 375))

    def test_complex_program26(self):
        line = '''Class EKM:__7{Constructor (z1,x:Jg0_;_51_:Array [Array [Array [String ,0b1_0],0B10100_1_1],0X7C_0_77];T_:Array [Array [Array [Array [Boolean ,0b111100],0xE],0B1010011],12_9]){} }'''
        expect = '''Program([ClassDecl(Id(EKM),Id(__7),[MethodDecl(Id(Constructor),Instance,[param(Id(z1),ClassType(Id(Jg0_))),param(Id(x),ClassType(Id(Jg0_))),param(Id(_51_),ArrayType(508023,ArrayType(83,ArrayType(2,StringType)))),param(Id(T_),ArrayType(129,ArrayType(83,ArrayType(14,ArrayType(60,BoolType)))))],Block([]))])])'''
        self.assertTrue(TestAST.test(line, expect, 376))

    def test_complex_program27(self):
        line = '''Class d{}Class B{$2(c_:__;_:Array [Array [String ,0xD],053_4_5_4]){} }Class z2lC:B3L{Var _l,$7a:S_;Constructor (y,_1_40_2_,__P:K_78){}Var $4:J;Val _,$q3_:Array [Array [Array [Array [Boolean ,046],0x8],046],5_2];}Class _7:_{Var v:G_J;}'''
        expect = '''Program([ClassDecl(Id(d),[]),ClassDecl(Id(B),[MethodDecl(Id($2),Static,[param(Id(c_),ClassType(Id(__))),param(Id(_),ArrayType(22316,ArrayType(13,StringType)))],Block([]))]),ClassDecl(Id(z2lC),Id(B3L),[AttributeDecl(Instance,VarDecl(Id(_l),ClassType(Id(S_)),NullLiteral())),AttributeDecl(Static,VarDecl(Id($7a),ClassType(Id(S_)),NullLiteral())),MethodDecl(Id(Constructor),Instance,[param(Id(y),ClassType(Id(K_78))),param(Id(_1_40_2_),ClassType(Id(K_78))),param(Id(__P),ClassType(Id(K_78)))],Block([])),AttributeDecl(Static,VarDecl(Id($4),ClassType(Id(J)),NullLiteral())),AttributeDecl(Instance,ConstDecl(Id(_),ArrayType(52,ArrayType(38,ArrayType(8,ArrayType(38,BoolType)))),None)),AttributeDecl(Static,ConstDecl(Id($q3_),ArrayType(52,ArrayType(38,ArrayType(8,ArrayType(38,BoolType)))),None))]),ClassDecl(Id(_7),Id(_),[AttributeDecl(Instance,VarDecl(Id(v),ClassType(Id(G_J)),NullLiteral()))])])'''
        self.assertTrue(TestAST.test(line, expect, 377))

    def test_complex_program28(self):
        line = '''Class _e7{_3(){} }Class g:kIn {Constructor (_,_L9_ka,T,f0,y,_3:_){Var m1,v,H:Array [Array [Array [String ,073],073],0B1];} }Class d:J{Val $8_21,$__,p8u_:_;Var Th_9X339I,_e,_:String ;}Class _{}'''
        expect = '''Program([ClassDecl(Id(_e7),[MethodDecl(Id(_3),Instance,[],Block([]))]),ClassDecl(Id(g),Id(kIn),[MethodDecl(Id(Constructor),Instance,[param(Id(_),ClassType(Id(_))),param(Id(_L9_ka),ClassType(Id(_))),param(Id(T),ClassType(Id(_))),param(Id(f0),ClassType(Id(_))),param(Id(y),ClassType(Id(_))),param(Id(_3),ClassType(Id(_)))],Block([VarDecl(Id(m1),ArrayType(1,ArrayType(59,ArrayType(59,StringType)))),VarDecl(Id(v),ArrayType(1,ArrayType(59,ArrayType(59,StringType)))),VarDecl(Id(H),ArrayType(1,ArrayType(59,ArrayType(59,StringType))))]))]),ClassDecl(Id(d),Id(J),[AttributeDecl(Static,ConstDecl(Id($8_21),ClassType(Id(_)),NullLiteral())),AttributeDecl(Static,ConstDecl(Id($__),ClassType(Id(_)),NullLiteral())),AttributeDecl(Instance,ConstDecl(Id(p8u_),ClassType(Id(_)),NullLiteral())),AttributeDecl(Instance,VarDecl(Id(Th_9X339I),StringType)),AttributeDecl(Instance,VarDecl(Id(_e),StringType)),AttributeDecl(Instance,VarDecl(Id(_),StringType))]),ClassDecl(Id(_),[])])'''
        self.assertTrue(TestAST.test(line, expect, 378))

    def test_complex_program29(self):
        line = '''Class W{}Class _9:J2{Destructor (){}Constructor (L:Array [Int ,28];G,__:J;TD:_3;C52__:_my__;_9v,_764,z_7,_:Array [Array [Array [Array [Array [Array [String ,0b1001100],07_4_765],7],015],047],047];__h_j:Array [Array [Array [Float ,0X5E],0X37_2],9]){} }Class _{}Class i4:_{_5(){Break ;} }'''
        expect = '''Program([ClassDecl(Id(W),[]),ClassDecl(Id(_9),Id(J2),[MethodDecl(Id(Destructor),Instance,[],Block([])),MethodDecl(Id(Constructor),Instance,[param(Id(L),ArrayType(28,IntType)),param(Id(G),ClassType(Id(J))),param(Id(__),ClassType(Id(J))),param(Id(TD),ClassType(Id(_3))),param(Id(C52__),ClassType(Id(_my__))),param(Id(_9v),ArrayType(39,ArrayType(39,ArrayType(13,ArrayType(7,ArrayType(31221,ArrayType(76,StringType))))))),param(Id(_764),ArrayType(39,ArrayType(39,ArrayType(13,ArrayType(7,ArrayType(31221,ArrayType(76,StringType))))))),param(Id(z_7),ArrayType(39,ArrayType(39,ArrayType(13,ArrayType(7,ArrayType(31221,ArrayType(76,StringType))))))),param(Id(_),ArrayType(39,ArrayType(39,ArrayType(13,ArrayType(7,ArrayType(31221,ArrayType(76,StringType))))))),param(Id(__h_j),ArrayType(9,ArrayType(882,ArrayType(94,FloatType))))],Block([]))]),ClassDecl(Id(_),[]),ClassDecl(Id(i4),Id(_),[MethodDecl(Id(_5),Instance,[],Block([Break]))])])'''
        self.assertTrue(TestAST.test(line, expect, 379))

    def test_complex_program30(self):
        line = '''Class _:_{}Class _S_F39W9{}Class r{Constructor (){} }Class c0A:_{Val $5_,m6,$ld_:Boolean ;Destructor (){Break ;{} }$e(K__:Array [Array [String ,53],0123];_F36_:h){Val _1,_6,Iy:Array [Boolean ,0XB_A];} }Class _{}'''
        expect = '''Program([ClassDecl(Id(_),Id(_),[]),ClassDecl(Id(_S_F39W9),[]),ClassDecl(Id(r),[MethodDecl(Id(Constructor),Instance,[],Block([]))]),ClassDecl(Id(c0A),Id(_),[AttributeDecl(Static,ConstDecl(Id($5_),BoolType,None)),AttributeDecl(Instance,ConstDecl(Id(m6),BoolType,None)),AttributeDecl(Static,ConstDecl(Id($ld_),BoolType,None)),MethodDecl(Id(Destructor),Instance,[],Block([Break,Block([])])),MethodDecl(Id($e),Static,[param(Id(K__),ArrayType(83,ArrayType(53,StringType))),param(Id(_F36_),ClassType(Id(h)))],Block([ConstDecl(Id(_1),ArrayType(186,BoolType),None),ConstDecl(Id(_6),ArrayType(186,BoolType),None),ConstDecl(Id(Iy),ArrayType(186,BoolType),None)]))]),ClassDecl(Id(_),[])])'''
        self.assertTrue(TestAST.test(line, expect, 380))

    def test_complex_program31(self):
        line = '''Class g_0:_{Var SQYe0f44,$69v3:Array [Array [Array [Array [Array [Int ,15],15],6],3],0b1_10];Var $_,$__1,__7_,_:Array [Array [Array [Array [Array [Int ,56_9_0],07],0xA8],0b1],01];$_8(){} }'''
        expect = '''Program([ClassDecl(Id(g_0),Id(_),[AttributeDecl(Instance,VarDecl(Id(SQYe0f44),ArrayType(6,ArrayType(3,ArrayType(6,ArrayType(15,ArrayType(15,IntType))))))),AttributeDecl(Static,VarDecl(Id($69v3),ArrayType(6,ArrayType(3,ArrayType(6,ArrayType(15,ArrayType(15,IntType))))))),AttributeDecl(Static,VarDecl(Id($_),ArrayType(1,ArrayType(1,ArrayType(168,ArrayType(7,ArrayType(5690,IntType))))))),AttributeDecl(Static,VarDecl(Id($__1),ArrayType(1,ArrayType(1,ArrayType(168,ArrayType(7,ArrayType(5690,IntType))))))),AttributeDecl(Instance,VarDecl(Id(__7_),ArrayType(1,ArrayType(1,ArrayType(168,ArrayType(7,ArrayType(5690,IntType))))))),AttributeDecl(Instance,VarDecl(Id(_),ArrayType(1,ArrayType(1,ArrayType(168,ArrayType(7,ArrayType(5690,IntType))))))),MethodDecl(Id($_8),Static,[],Block([]))])])'''
        self.assertTrue(TestAST.test(line, expect, 381))

    def test_complex_program32(self):
        line = '''Class _:Ef{Constructor (__9_,I:Array [Int ,0b1];w,_:Array [Array [Float ,0B1],0X34]){} }Class d8{Constructor (_,d_,S,tbS5s_:_1_){} }Class jR{}Class P8{}Class t:_{Constructor (_,_S:P;_,_,i1:String ;e_,Z_,w:V;_:Array [Float ,17];z:Array [Boolean ,0X9]){} }'''
        expect = '''Program([ClassDecl(Id(_),Id(Ef),[MethodDecl(Id(Constructor),Instance,[param(Id(__9_),ArrayType(1,IntType)),param(Id(I),ArrayType(1,IntType)),param(Id(w),ArrayType(52,ArrayType(1,FloatType))),param(Id(_),ArrayType(52,ArrayType(1,FloatType)))],Block([]))]),ClassDecl(Id(d8),[MethodDecl(Id(Constructor),Instance,[param(Id(_),ClassType(Id(_1_))),param(Id(d_),ClassType(Id(_1_))),param(Id(S),ClassType(Id(_1_))),param(Id(tbS5s_),ClassType(Id(_1_)))],Block([]))]),ClassDecl(Id(jR),[]),ClassDecl(Id(P8),[]),ClassDecl(Id(t),Id(_),[MethodDecl(Id(Constructor),Instance,[param(Id(_),ClassType(Id(P))),param(Id(_S),ClassType(Id(P))),param(Id(_),StringType),param(Id(_),StringType),param(Id(i1),StringType),param(Id(e_),ClassType(Id(V))),param(Id(Z_),ClassType(Id(V))),param(Id(w),ClassType(Id(V))),param(Id(_),ArrayType(17,FloatType)),param(Id(z),ArrayType(9,BoolType))],Block([]))])])'''
        self.assertTrue(TestAST.test(line, expect, 382))

    def test_complex_program33(self):
        line = '''Class y:_{Constructor (gN4,_,_:Array [String ,010];f:Array [Array [String ,0XD],33];J_0,TF,_:Float ;v:String ;_L_0:Array [Float ,063];W,_:Array [Array [Array [String ,0b1000000],0x5],0b1_1];V:_;Ad,_:s__;_1O7:Boolean ){Var A,_,_0__,_,g,_:Int ;} }'''
        expect = '''Program([ClassDecl(Id(y),Id(_),[MethodDecl(Id(Constructor),Instance,[param(Id(gN4),ArrayType(8,StringType)),param(Id(_),ArrayType(8,StringType)),param(Id(_),ArrayType(8,StringType)),param(Id(f),ArrayType(33,ArrayType(13,StringType))),param(Id(J_0),FloatType),param(Id(TF),FloatType),param(Id(_),FloatType),param(Id(v),StringType),param(Id(_L_0),ArrayType(51,FloatType)),param(Id(W),ArrayType(3,ArrayType(5,ArrayType(64,StringType)))),param(Id(_),ArrayType(3,ArrayType(5,ArrayType(64,StringType)))),param(Id(V),ClassType(Id(_))),param(Id(Ad),ClassType(Id(s__))),param(Id(_),ClassType(Id(s__))),param(Id(_1O7),BoolType)],Block([VarDecl(Id(A),IntType),VarDecl(Id(_),IntType),VarDecl(Id(_0__),IntType),VarDecl(Id(_),IntType),VarDecl(Id(g),IntType),VarDecl(Id(_),IntType)]))])])'''
        self.assertTrue(TestAST.test(line, expect, 383))

    def test_complex_program34(self):
        line = '''Class X{}Class _02_{}Class fT_8:_Kx{Val ___9M,$__:Array [Array [Array [Array [Array [Array [String ,075],5_4_7],0b1_0],0B1],0b1],0b1110];}Class _{Var $0,$_,_U7:Array [String ,54];}'''
        expect = '''Program([ClassDecl(Id(X),[]),ClassDecl(Id(_02_),[]),ClassDecl(Id(fT_8),Id(_Kx),[AttributeDecl(Instance,ConstDecl(Id(___9M),ArrayType(14,ArrayType(1,ArrayType(1,ArrayType(2,ArrayType(547,ArrayType(61,StringType)))))),None)),AttributeDecl(Static,ConstDecl(Id($__),ArrayType(14,ArrayType(1,ArrayType(1,ArrayType(2,ArrayType(547,ArrayType(61,StringType)))))),None))]),ClassDecl(Id(_),[AttributeDecl(Static,VarDecl(Id($0),ArrayType(54,StringType))),AttributeDecl(Static,VarDecl(Id($_),ArrayType(54,StringType))),AttributeDecl(Instance,VarDecl(Id(_U7),ArrayType(54,StringType)))])])'''
        self.assertTrue(TestAST.test(line, expect, 384))

    def test_complex_program35(self):
        line = '''Class E_{Constructor (_2l,_N:Array [Array [Array [Array [Boolean ,87],05],87],0b11100];__2,L:Float ;B:_){Return ;}Val $4VW_:Array [Boolean ,036];_(){} }Class _:___{$48(){}Val _,J:_;}Class _:_{}Class _t{}Class _:N{Destructor (){} }'''
        expect = '''Program([ClassDecl(Id(E_),[MethodDecl(Id(Constructor),Instance,[param(Id(_2l),ArrayType(28,ArrayType(87,ArrayType(5,ArrayType(87,BoolType))))),param(Id(_N),ArrayType(28,ArrayType(87,ArrayType(5,ArrayType(87,BoolType))))),param(Id(__2),FloatType),param(Id(L),FloatType),param(Id(B),ClassType(Id(_)))],Block([Return()])),AttributeDecl(Static,ConstDecl(Id($4VW_),ArrayType(30,BoolType),None)),MethodDecl(Id(_),Instance,[],Block([]))]),ClassDecl(Id(_),Id(___),[MethodDecl(Id($48),Static,[],Block([])),AttributeDecl(Instance,ConstDecl(Id(_),ClassType(Id(_)),NullLiteral())),AttributeDecl(Instance,ConstDecl(Id(J),ClassType(Id(_)),NullLiteral()))]),ClassDecl(Id(_),Id(_),[]),ClassDecl(Id(_t),[]),ClassDecl(Id(_),Id(N),[MethodDecl(Id(Destructor),Instance,[],Block([]))])])'''
        self.assertTrue(TestAST.test(line, expect, 385))

    def test_complex_program36(self):
        line = '''Class _7_{Val $_,$w9M:Int ;$O(L_:Array [String ,0B1]){ {}Return ;Break ;Continue ;{} }Destructor (){}$__(V_j3,r,_K,___u,_f:J;_U,F:Int ;_5_:Array [Float ,0X5_61A]){} }'''
        expect = '''Program([ClassDecl(Id(_7_),[AttributeDecl(Static,ConstDecl(Id($_),IntType,None)),AttributeDecl(Static,ConstDecl(Id($w9M),IntType,None)),MethodDecl(Id($O),Static,[param(Id(L_),ArrayType(1,StringType))],Block([Block([]),Return(),Break,Continue,Block([])])),MethodDecl(Id(Destructor),Instance,[],Block([])),MethodDecl(Id($__),Static,[param(Id(V_j3),ClassType(Id(J))),param(Id(r),ClassType(Id(J))),param(Id(_K),ClassType(Id(J))),param(Id(___u),ClassType(Id(J))),param(Id(_f),ClassType(Id(J))),param(Id(_U),IntType),param(Id(F),IntType),param(Id(_5_),ArrayType(22042,FloatType))],Block([]))])])'''
        self.assertTrue(TestAST.test(line, expect, 386))

    def test_complex_program37(self):
        line = '''Class o{$_X(_,d,_:Array [Array [Int ,014],0b1010000];s,KA:Int ;O,x0y_,I___,_43,M:H0;C:Float ){}Constructor (_0:Array [String ,0b1010000];TQ,z:_){} }Class _7{}Class __{}Class BdEiC:_4j{}'''
        expect = '''Program([ClassDecl(Id(o),[MethodDecl(Id($_X),Static,[param(Id(_),ArrayType(80,ArrayType(12,IntType))),param(Id(d),ArrayType(80,ArrayType(12,IntType))),param(Id(_),ArrayType(80,ArrayType(12,IntType))),param(Id(s),IntType),param(Id(KA),IntType),param(Id(O),ClassType(Id(H0))),param(Id(x0y_),ClassType(Id(H0))),param(Id(I___),ClassType(Id(H0))),param(Id(_43),ClassType(Id(H0))),param(Id(M),ClassType(Id(H0))),param(Id(C),FloatType)],Block([])),MethodDecl(Id(Constructor),Instance,[param(Id(_0),ArrayType(80,StringType)),param(Id(TQ),ClassType(Id(_))),param(Id(z),ClassType(Id(_)))],Block([]))]),ClassDecl(Id(_7),[]),ClassDecl(Id(__),[]),ClassDecl(Id(BdEiC),Id(_4j),[])])'''
        self.assertTrue(TestAST.test(line, expect, 387))

    def test_complex_program38(self):
        line = '''Class __:Q{Val $_DE8:Int ;Var $_,I,$7v:Array [String ,0B1_1];Constructor (){ {Return ;} }$8(){} }Class __T{Constructor (){} }Class o:A_{__0L(_Fb5,d:h;_,_:Boolean ){Val ___:Array [Array [Array [Array [Boolean ,064334],8],0XF_D_9],0XD];Break ;}Var z_,$6:Array [String ,19];}Class __9:cy{}'''
        expect = '''Program([ClassDecl(Id(__),Id(Q),[AttributeDecl(Static,ConstDecl(Id($_DE8),IntType,None)),AttributeDecl(Static,VarDecl(Id($_),ArrayType(3,StringType))),AttributeDecl(Instance,VarDecl(Id(I),ArrayType(3,StringType))),AttributeDecl(Static,VarDecl(Id($7v),ArrayType(3,StringType))),MethodDecl(Id(Constructor),Instance,[],Block([Block([Return()])])),MethodDecl(Id($8),Static,[],Block([]))]),ClassDecl(Id(__T),[MethodDecl(Id(Constructor),Instance,[],Block([]))]),ClassDecl(Id(o),Id(A_),[MethodDecl(Id(__0L),Instance,[param(Id(_Fb5),ClassType(Id(h))),param(Id(d),ClassType(Id(h))),param(Id(_),BoolType),param(Id(_),BoolType)],Block([ConstDecl(Id(___),ArrayType(13,ArrayType(4057,ArrayType(8,ArrayType(26844,BoolType)))),None),Break])),AttributeDecl(Instance,VarDecl(Id(z_),ArrayType(19,StringType))),AttributeDecl(Static,VarDecl(Id($6),ArrayType(19,StringType)))]),ClassDecl(Id(__9),Id(cy),[])])'''
        self.assertTrue(TestAST.test(line, expect, 388))

    def test_complex_program39(self):
        line = '''Class M{Constructor (__:Boolean ){Break ;} }Class P:_g52{Val _:_;Constructor (p:Float ){ {}Return ;}Val $_5:Float ;$_(){}Constructor (){} }Class U:W{Var a2,_:Array [Array [Array [Array [Array [Array [Int ,075],0116],0B1],6],0x53],0116];Var h:Array [Array [Boolean ,26],0B1100001];}Class B:_{}Class RRG2{}'''
        expect = '''Program([ClassDecl(Id(M),[MethodDecl(Id(Constructor),Instance,[param(Id(__),BoolType)],Block([Break]))]),ClassDecl(Id(P),Id(_g52),[AttributeDecl(Instance,ConstDecl(Id(_),ClassType(Id(_)),NullLiteral())),MethodDecl(Id(Constructor),Instance,[param(Id(p),FloatType)],Block([Block([]),Return()])),AttributeDecl(Static,ConstDecl(Id($_5),FloatType,None)),MethodDecl(Id($_),Static,[],Block([])),MethodDecl(Id(Constructor),Instance,[],Block([]))]),ClassDecl(Id(U),Id(W),[AttributeDecl(Instance,VarDecl(Id(a2),ArrayType(78,ArrayType(83,ArrayType(6,ArrayType(1,ArrayType(78,ArrayType(61,IntType)))))))),AttributeDecl(Instance,VarDecl(Id(_),ArrayType(78,ArrayType(83,ArrayType(6,ArrayType(1,ArrayType(78,ArrayType(61,IntType)))))))),AttributeDecl(Instance,VarDecl(Id(h),ArrayType(97,ArrayType(26,BoolType))))]),ClassDecl(Id(B),Id(_),[]),ClassDecl(Id(RRG2),[])])'''
        self.assertTrue(TestAST.test(line, expect, 389))

    def test_complex_program40(self):
        line = '''Class P8O5w__:_{Val $__b0__Y,_,_,$5_,$h_,$3O_K:String ;}Class k{n(){Continue ;}Destructor (){}Val X,$e_,$R,_,_:_4;}Class Q:r{$2(){}Val $___:String ;}Class d7:F4{}'''
        expect = '''Program([ClassDecl(Id(P8O5w__),Id(_),[AttributeDecl(Static,ConstDecl(Id($__b0__Y),StringType,None)),AttributeDecl(Instance,ConstDecl(Id(_),StringType,None)),AttributeDecl(Instance,ConstDecl(Id(_),StringType,None)),AttributeDecl(Static,ConstDecl(Id($5_),StringType,None)),AttributeDecl(Static,ConstDecl(Id($h_),StringType,None)),AttributeDecl(Static,ConstDecl(Id($3O_K),StringType,None))]),ClassDecl(Id(k),[MethodDecl(Id(n),Instance,[],Block([Continue])),MethodDecl(Id(Destructor),Instance,[],Block([])),AttributeDecl(Instance,ConstDecl(Id(X),ClassType(Id(_4)),NullLiteral())),AttributeDecl(Static,ConstDecl(Id($e_),ClassType(Id(_4)),NullLiteral())),AttributeDecl(Static,ConstDecl(Id($R),ClassType(Id(_4)),NullLiteral())),AttributeDecl(Instance,ConstDecl(Id(_),ClassType(Id(_4)),NullLiteral())),AttributeDecl(Instance,ConstDecl(Id(_),ClassType(Id(_4)),NullLiteral()))]),ClassDecl(Id(Q),Id(r),[MethodDecl(Id($2),Static,[],Block([])),AttributeDecl(Static,ConstDecl(Id($___),StringType,None))]),ClassDecl(Id(d7),Id(F4),[])])'''
        self.assertTrue(TestAST.test(line, expect, 390))

    def test_complex_program41(self):
        line = '''Class H{Constructor (__h9:Array [Array [Array [Array [Float ,0x2_8C_4_8],43],0B1],43];b2L:e0l4;Bq_uP5n322:Boolean ;_,G,_:Boolean ){} }Class LB6:g{}Class _{Destructor (){}$_(){}Val _,__:__l_4;}'''
        expect = '''Program([ClassDecl(Id(H),[MethodDecl(Id(Constructor),Instance,[param(Id(__h9),ArrayType(43,ArrayType(1,ArrayType(43,ArrayType(166984,FloatType))))),param(Id(b2L),ClassType(Id(e0l4))),param(Id(Bq_uP5n322),BoolType),param(Id(_),BoolType),param(Id(G),BoolType),param(Id(_),BoolType)],Block([]))]),ClassDecl(Id(LB6),Id(g),[]),ClassDecl(Id(_),[MethodDecl(Id(Destructor),Instance,[],Block([])),MethodDecl(Id($_),Static,[],Block([])),AttributeDecl(Instance,ConstDecl(Id(_),ClassType(Id(__l_4)),NullLiteral())),AttributeDecl(Instance,ConstDecl(Id(__),ClassType(Id(__l_4)),NullLiteral()))])])'''
        self.assertTrue(TestAST.test(line, expect, 391))

    def test_complex_program42(self):
        line = '''Class _:G_{}Class _{Destructor (){ {Continue ;}Val V_126:Array [Array [Int ,4_5],0104];}$_(z,F_:Boolean ;gU3:Boolean ;_,_lU0:Array [Float ,0B1100010];P,B,k,_,_,_,L:Array [Array [Float ,0XD],77]){} }'''
        expect = '''Program([ClassDecl(Id(_),Id(G_),[]),ClassDecl(Id(_),[MethodDecl(Id(Destructor),Instance,[],Block([Block([Continue]),ConstDecl(Id(V_126),ArrayType(68,ArrayType(45,IntType)),None)])),MethodDecl(Id($_),Static,[param(Id(z),BoolType),param(Id(F_),BoolType),param(Id(gU3),BoolType),param(Id(_),ArrayType(98,FloatType)),param(Id(_lU0),ArrayType(98,FloatType)),param(Id(P),ArrayType(77,ArrayType(13,FloatType))),param(Id(B),ArrayType(77,ArrayType(13,FloatType))),param(Id(k),ArrayType(77,ArrayType(13,FloatType))),param(Id(_),ArrayType(77,ArrayType(13,FloatType))),param(Id(_),ArrayType(77,ArrayType(13,FloatType))),param(Id(_),ArrayType(77,ArrayType(13,FloatType))),param(Id(L),ArrayType(77,ArrayType(13,FloatType)))],Block([]))])])'''
        self.assertTrue(TestAST.test(line, expect, 392))

    def test_complex_program43(self):
        line = '''Class _66NNM:k{Constructor (_,z,v:Boolean ;_8,_:Boolean ;G9c:String ){} }Class YK3{}Class _{}Class c:_C{Var j,_BT,$_c,A:_9;Destructor (){Continue ;}Destructor (){} }Class ____:_{}'''
        expect = '''Program([ClassDecl(Id(_66NNM),Id(k),[MethodDecl(Id(Constructor),Instance,[param(Id(_),BoolType),param(Id(z),BoolType),param(Id(v),BoolType),param(Id(_8),BoolType),param(Id(_),BoolType),param(Id(G9c),StringType)],Block([]))]),ClassDecl(Id(YK3),[]),ClassDecl(Id(_),[]),ClassDecl(Id(c),Id(_C),[AttributeDecl(Instance,VarDecl(Id(j),ClassType(Id(_9)),NullLiteral())),AttributeDecl(Instance,VarDecl(Id(_BT),ClassType(Id(_9)),NullLiteral())),AttributeDecl(Static,VarDecl(Id($_c),ClassType(Id(_9)),NullLiteral())),AttributeDecl(Instance,VarDecl(Id(A),ClassType(Id(_9)),NullLiteral())),MethodDecl(Id(Destructor),Instance,[],Block([Continue])),MethodDecl(Id(Destructor),Instance,[],Block([]))]),ClassDecl(Id(____),Id(_),[])])'''
        self.assertTrue(TestAST.test(line, expect, 393))

    def test_complex_program44(self):
        line = '''Class _:_{Constructor (_r2,c__:Array [Array [Array [Array [Float ,0B1100000],0X7],06_2_1],0116]){Return ;}Var _:Array [Array [String ,0b101010],0X3];Destructor (){}Var _P,$_6,$7:Array [String ,0116];}Class i:_5{}'''
        expect = '''Program([ClassDecl(Id(_),Id(_),[MethodDecl(Id(Constructor),Instance,[param(Id(_r2),ArrayType(78,ArrayType(401,ArrayType(7,ArrayType(96,FloatType))))),param(Id(c__),ArrayType(78,ArrayType(401,ArrayType(7,ArrayType(96,FloatType)))))],Block([Return()])),AttributeDecl(Instance,VarDecl(Id(_),ArrayType(3,ArrayType(42,StringType)))),MethodDecl(Id(Destructor),Instance,[],Block([])),AttributeDecl(Instance,VarDecl(Id(_P),ArrayType(78,StringType))),AttributeDecl(Static,VarDecl(Id($_6),ArrayType(78,StringType))),AttributeDecl(Static,VarDecl(Id($7),ArrayType(78,StringType)))]),ClassDecl(Id(i),Id(_5),[])])'''
        self.assertTrue(TestAST.test(line, expect, 394))

    def test_complex_program45(self):
        line = '''Class __:b{}Class _:N_{}Class _:_42{}Class C:y7{Constructor (__j,_8_D_V__4:F_X57;_:Float ){}Destructor (){} }Class _i__{}Class _:__{Constructor (_9:__B_0){} }Class _{$W(){} }'''
        expect = '''Program([ClassDecl(Id(__),Id(b),[]),ClassDecl(Id(_),Id(N_),[]),ClassDecl(Id(_),Id(_42),[]),ClassDecl(Id(C),Id(y7),[MethodDecl(Id(Constructor),Instance,[param(Id(__j),ClassType(Id(F_X57))),param(Id(_8_D_V__4),ClassType(Id(F_X57))),param(Id(_),FloatType)],Block([])),MethodDecl(Id(Destructor),Instance,[],Block([]))]),ClassDecl(Id(_i__),[]),ClassDecl(Id(_),Id(__),[MethodDecl(Id(Constructor),Instance,[param(Id(_9),ClassType(Id(__B_0)))],Block([]))]),ClassDecl(Id(_),[MethodDecl(Id($W),Static,[],Block([]))])])'''
        self.assertTrue(TestAST.test(line, expect, 395))

    def test_complex_program46(self):
        line = '''Class _{Destructor (){Return ;} }Class _3q:_{Val _:Array [Array [Array [Array [Array [Array [Array [Int ,11_8],65],65],65],8_8_0],0x8D_1_2],0xD];}Class S{}Class J4:_p{}Class ___:_{}'''
        expect = '''Program([ClassDecl(Id(_),[MethodDecl(Id(Destructor),Instance,[],Block([Return()]))]),ClassDecl(Id(_3q),Id(_),[AttributeDecl(Instance,ConstDecl(Id(_),ArrayType(13,ArrayType(36114,ArrayType(880,ArrayType(65,ArrayType(65,ArrayType(65,ArrayType(118,IntType))))))),None))]),ClassDecl(Id(S),[]),ClassDecl(Id(J4),Id(_p),[]),ClassDecl(Id(___),Id(_),[])])'''
        self.assertTrue(TestAST.test(line, expect, 396))

    def test_complex_program47(self):
        line = '''Class N:__{Constructor (r_:I8M;_:Array [Array [Boolean ,0x95],90_0]){}Constructor (){} }Class HY:l5{}Class U39{}Class _B_m{}Class z7_6:u{}Class S6:_{}Class _{Destructor (){} }'''
        expect = '''Program([ClassDecl(Id(N),Id(__),[MethodDecl(Id(Constructor),Instance,[param(Id(r_),ClassType(Id(I8M))),param(Id(_),ArrayType(900,ArrayType(149,BoolType)))],Block([])),MethodDecl(Id(Constructor),Instance,[],Block([]))]),ClassDecl(Id(HY),Id(l5),[]),ClassDecl(Id(U39),[]),ClassDecl(Id(_B_m),[]),ClassDecl(Id(z7_6),Id(u),[]),ClassDecl(Id(S6),Id(_),[]),ClassDecl(Id(_),[MethodDecl(Id(Destructor),Instance,[],Block([]))])])'''
        self.assertTrue(TestAST.test(line, expect, 397))

    def test_complex_program48(self):
        line = '''Class Z1:_k{Var $8,$_JBA:Boolean ;Constructor (E_a8:Array [Int ,0x55];h:P_;_,_1_4_:Array [Array [Array [Boolean ,0X5C],0X5C],0166];Js68:o;__,k:Boolean ){}Constructor (j:Boolean ){} }'''
        expect = '''Program([ClassDecl(Id(Z1),Id(_k),[AttributeDecl(Static,VarDecl(Id($8),BoolType)),AttributeDecl(Static,VarDecl(Id($_JBA),BoolType)),MethodDecl(Id(Constructor),Instance,[param(Id(E_a8),ArrayType(85,IntType)),param(Id(h),ClassType(Id(P_))),param(Id(_),ArrayType(118,ArrayType(92,ArrayType(92,BoolType)))),param(Id(_1_4_),ArrayType(118,ArrayType(92,ArrayType(92,BoolType)))),param(Id(Js68),ClassType(Id(o))),param(Id(__),BoolType),param(Id(k),BoolType)],Block([])),MethodDecl(Id(Constructor),Instance,[param(Id(j),BoolType)],Block([]))])])'''
        self.assertTrue(TestAST.test(line, expect, 398))

    def test_complex_program49(self):
        line = '''Class h{Var _6,J,_:Boolean ;Destructor (){Break ;}$t(E_X,N:CWL;__:Gv8;_5_z,_S6:Int ;x:Array [String ,056];s:Array [Int ,3_2_1];g,Rb:Array [Array [Array [String ,0X54],0xD_3],0x46];_f:Float ;_,v_,kJ6,_0:String ){} }'''
        expect = '''Program([ClassDecl(Id(h),[AttributeDecl(Instance,VarDecl(Id(_6),BoolType)),AttributeDecl(Instance,VarDecl(Id(J),BoolType)),AttributeDecl(Instance,VarDecl(Id(_),BoolType)),MethodDecl(Id(Destructor),Instance,[],Block([Break])),MethodDecl(Id($t),Static,[param(Id(E_X),ClassType(Id(CWL))),param(Id(N),ClassType(Id(CWL))),param(Id(__),ClassType(Id(Gv8))),param(Id(_5_z),IntType),param(Id(_S6),IntType),param(Id(x),ArrayType(46,StringType)),param(Id(s),ArrayType(321,IntType)),param(Id(g),ArrayType(70,ArrayType(211,ArrayType(84,StringType)))),param(Id(Rb),ArrayType(70,ArrayType(211,ArrayType(84,StringType)))),param(Id(_f),FloatType),param(Id(_),StringType),param(Id(v_),StringType),param(Id(kJ6),StringType),param(Id(_0),StringType)],Block([]))])])'''
        self.assertTrue(TestAST.test(line, expect, 399))

    def test_complex_program50(self):
        line = '''Class _X:_{Var $6,$11:Array [Array [Array [Array [String ,61],0133],0xA],0133];}Class C{}Class _:_{Constructor (_,r:_5;_:Array [Array [String ,1],0x57];b_9c9,Y:Array [Float ,5];xh,Ae40:_){} }Class K{Val x8_6:Boolean ;}'''
        expect = '''Program([ClassDecl(Id(_X),Id(_),[AttributeDecl(Static,VarDecl(Id($6),ArrayType(91,ArrayType(10,ArrayType(91,ArrayType(61,StringType)))))),AttributeDecl(Static,VarDecl(Id($11),ArrayType(91,ArrayType(10,ArrayType(91,ArrayType(61,StringType))))))]),ClassDecl(Id(C),[]),ClassDecl(Id(_),Id(_),[MethodDecl(Id(Constructor),Instance,[param(Id(_),ClassType(Id(_5))),param(Id(r),ClassType(Id(_5))),param(Id(_),ArrayType(87,ArrayType(1,StringType))),param(Id(b_9c9),ArrayType(5,FloatType)),param(Id(Y),ArrayType(5,FloatType)),param(Id(xh),ClassType(Id(_))),param(Id(Ae40),ClassType(Id(_)))],Block([]))]),ClassDecl(Id(K),[AttributeDecl(Instance,ConstDecl(Id(x8_6),BoolType,None))])])'''
        self.assertTrue(TestAST.test(line, expect, 353))