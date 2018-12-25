import unittest
from ..modules.basic import Keyword
from ..modules.base import Variable
from ..modules.base import Operator
from ..modules.base import Function
from ..modules.base import Class

from ..modules.structure import If,Elif,Else


from ..modules.generator import G_Variable
from ..modules.generator import G_Operator
from ..modules.generator import G_Structure
from ..modules.generator import G_Function
from ..modules.generator import G_Class



class Test_Generator(unittest.TestCase):
    def test_GeneratorVariable(self):
        G = G_Variable()
        V = Variable()
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
    def test_GeneratorOperator(self):
        G = G_Operator()
        O = Operator()
        O.str1 = 'abc'
        O.operator = '=='
        O.str2 = 'bcd'
        self.assertEqual(G.generate(O), 'abc == bcd')
    def test_GeneratorStructure(self):
        G = G_Structure()
        O = Operator()
        O.str1 = 'abc'
        O.operator = '=='
        O.str2 = 'bcd'
        I = If()
        I.addCondition(O)
        self.assertEqual(G.generate(I), 'if abc == bcd :\npass')
    def test_GeneratorFunction(self):
        G = G_Function()
        F = Function()
        F.name = 'test_fun'
        self.assertEqual(G.generate(F), 'def test_fun():\npass')
    def test_GeneratorClass(self):
        G = G_Class()
        C = Class()
        C.name = 'test_class'
        self.assertEqual(G.generate(C), 'class test_class:\npass')
        C.inherit_class = 'Base()'
        self.assertEqual(G.generate(C), 'class test_class(Base()):\npass')

if __name__ == '__main__':
    unittest.main()
