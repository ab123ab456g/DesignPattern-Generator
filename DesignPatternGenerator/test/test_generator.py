import unittest
from ..modules.datatypes import basic
from ..modules.datatypes import base
from ..modules.datatypes import structure
from ..modules.generators import gbase

class Test_Generator(unittest.TestCase):
    def test_GeneratorVariable(self):
        G = gbase.G_Variable()
        V = base.Variable()
        V.name = 'abc'
        V.operator = '='
        V.value = '123'
        V.datatype = ''
        self.assertEqual(G.generate(V), 'abc = \'123\'')
        V.value = '123'
        V.datatype = 'int'
        self.assertEqual(G.generate(V), 'abc = 123')
        V.value = '123'
        V.datatype = 'str'
        self.assertEqual(G.generate(V), 'abc = \'123\'')
        V.value = '123'
        V.datatype = None
        self.assertEqual(G.generate(V), 'abc = \'123\'')
        V.value = None
        V.datatype = 'None'
        self.assertEqual(G.generate(V), 'abc = None')
        V.value = []
        V.datatype = 'list'
        self.assertEqual(G.generate(V), 'abc = []')
        V.value = '{}'
        V.datatype = 'dict'
        self.assertEqual(G.generate(V), 'abc = {}')
        V.value = set()
        V.datatype = 'set'
        self.assertEqual(G.generate(V), 'abc = set()')
        V.value = 'tuple()'
        V.datatype = 'tuple'
        self.assertEqual(G.generate(V), 'abc = tuple()')
        V.value = 'datetime()'
        V.datatype = 'other'
        self.assertEqual(G.generate(V), 'abc = datetime()')
    def test_GeneratorIf(self):
        G = gbase.G_Structure()
        O = base.Operator()
        O.str1 = 'abc'
        O.operator = '=='
        O.str2 = 'bcd'
        I = structure.If()
        I.addCondition(O)
        self.assertEqual(G.generate(I), 'if abc == bcd:\n    pass\n')
    def test_GeneratorElif(self):
        pass
    def test_GeneratorElse(self):
        pass
    def test_GeneratorOperator(self):
        G = gbase.G_Operator()
        O = base.Operator()
        O.str1 = 'abc'
        O.operator = '=='
        O.str2 = 'bcd'
        self.assertEqual(G.generate(O), 'abc == bcd')
    def test_GeneratorContent(self):
        G = gbase.G_Content()
        C = base.Content()
        self.assertEqual(G.space, '    ')
        self.assertEqual(G.generate(C), '    pass\n')
        V = base.Variable()
        V.value = '123'
        V.name = 'abc'
        V.operator = '='
        C.addContent(base.Variable, V)
        C.addContent(base.Variable, V)
        self.assertEqual(G.generate(C), '    abc = \'123\'\n    abc = \'123\'\n')
        C = base.Content()
        C2= base.Call()
        C2.name = 'test'
        C2.addParameter('abc')
        C2.addParameter('cde')
        C.addContent(base.Call, C2)
        self.assertEqual(G.generate(C), '    test(abc, cde)\n')
        C = base.Content()
        O = base.Operator()
        O.str1 = 'abc'
        O.operator = '=='
        O.str2 = 'bcd'
        I = structure.If()
        I.addCondition(O)
        C.addContent(base.Structure, I)
        self.assertEqual(G.generate(C), '    if abc == bcd:\n        pass\n')
    def test_GeneratorCall(self):
        G = gbase.G_Call()
        C = base.Call()
        C.name = 'test'
        self.assertEqual(G.generate(C), 'test()')
        C.addParameter('abc')
        self.assertEqual(G.generate(C), 'test(abc)')
        C.addParameter('cde')
        self.assertEqual(G.generate(C), 'test(abc, cde)')

    def test_GeneratorLoop(self):
        pass

    def test_GeneratorFunction(self):
        G = gbase.G_Function()
        F = base.Function()
        F.name = 'test_fun'

        self.assertEqual(G.generate(F), 'def test_fun():\n    pass\n')
        F.addParameter('abc')
        self.assertEqual(G.generate(F), 'def test_fun(abc):\n    pass\n')
    def test_GeneratorClass(self):
        G = gbase.G_Class()
        C = base.Class()
        C.name = 'test_class'
        C.inherit_class = 'Base()'
        self.assertEqual(G.generate(C), 'class test_class(Base()):\n    pass\n')
        C = base.Class()
        V = base.Variable()
        V2 = base.Variable()
        V.name = 'abc'
        V.operator = '='
        V.datatype = 'int'
        V.value = 0
        C.name = 'test_class'
        C.addVariable(V)
        self.assertEqual(G.generate(C), 'class test_class:\n    def __init__(self):\n        self.abc = 0\n')
        C = base.Class()
        V.name = 'abc'
        V2.name = 'cde'
        V2.operator = '='
        V2.datatype = 'int'
        V2.value = 0
        C.name = 'test_class'
        C.addVariable(V)
        C.addVariable(V2)
        self.assertEqual(G.generate(C), 'class test_class:\n    def __init__(self):\n        self.abc = 0\n        self.cde = 0\n')
        C = base.Class()
        F =base.Function()
        F.name = 'test_fun'
        F.addParameter('self')
        F2 =base.Function()
        F2.name = 'test_fun2'
        F2.addParameter('self')
        C.name = 'test_class'
        C.addMethod(F)
        self.assertEqual(G.generate(C), 'class test_class:\n    def test_fun(self):\n        pass\n')
        C = base.Class()
        C.name = 'test_class'
        C.addMethod(F)
        C.addMethod(F2)
        self.assertEqual(G.generate(C), 'class test_class:\n    def test_fun(self):\n        pass\n    def test_fun2(self):\n        pass\n')

    def test_Designpattern(self):
        pass

if __name__ == '__main__':
    unittest.main()
