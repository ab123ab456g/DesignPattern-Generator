import unittest
from ..modules.generator_variable import GeneratorVariable
from ..modules.variable import Variable
from ..modules.basic import Keyword
datatype = ['int', 'str', 'None', 'list', 'dict', 'set', 'tuple', 'other']



class Test_Generator_Variable(unittest.TestCase):
    def test_GeneratorVariable(self):
        G = GeneratorVariable()
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

if __name__ == '__main__':
    unittest.main()
