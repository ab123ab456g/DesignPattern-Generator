import unittest

from ..modules.variable import Variable, Datatype
from ..modules.variable import G_Int, G_Str, G_List, G_Dict, G_Set, G_Tuple, G_Other
from ..modules.variable import VariableFacotry

class Test_Variable(unittest.TestCase):
    def test_Datatype(self):
        d = Datatype()
        datatype = ['int', 'str', 'None', 'list', 'dict', 'set', 'tuple', 'other']
        self.assertEqual(d.datatype, datatype)

    def test_Variable_Generator(self):
        v =Variable()
        name = 'abc'
        TestDict = {'int':53, 'str':'53', 'None':None, 'list':[], 'dict':{}, 'set':set({1:1,2:2}), 'tuple':(1,2), 'other':'other'}
        v.name = name
        for datatype in Datatype.datatype:
            v.datatype = datatype
            v.value = TestDict[datatype]
            if  v.datatype == 'str':
                self.assertEqual(v.generate(), 'abc=' + '\'' + str(TestDict[datatype]) + '\'')
            elif v.datatype == 'set':
                self.assertEqual(v.generate(), 'abc=' + str(set(TestDict[datatype])))
            else:
                self.assertEqual(v.generate(), 'abc=' + str(TestDict[datatype]))

    def test_G_Int(self):
        g = G_Int()
        self.assertEqual(g.datatype, 'int')

    def test_G_Str(self):
        g = G_Str()
        self.assertEqual(g.datatype, 'str')

    def test_G_List(self):
        g = G_List()
        self.assertEqual(g.datatype, 'list')

    def test_G_Tuple(self):
        g = G_Tuple()
        self.assertEqual(g.datatype, 'tuple')

    def test_G_Dict(self):
        g = G_Dict()
        self.assertEqual(g.datatype, 'dict')

    def test_G_Set(self):
        g = G_Set()
        self.assertEqual(g.datatype, 'set')

    def test_G_Other(self):
        g = G_Other()
        self.assertEqual(g.datatype, 'other')

    def test_VariableFactory(self):
        f = VariableFacotry()
        self.assertEqual(type(f.setVariable()), type(Variable()))
        self.assertEqual(type(f.setInt()), type(G_Int()))
        self.assertEqual(type(f.setStr()), type(G_Str()))
        self.assertEqual(type(f.setList()), type(G_List()))
        self.assertEqual(type(f.setTuple()), type(G_Tuple()))
        self.assertEqual(type(f.setDict()), type(G_Dict()))
        self.assertEqual(type(f.setSet()), type(G_Set()))
        self.assertEqual(type(f.setOther()), type(G_Other()))

if __name__ == '__main__':
    unittest.main()

# assertTrue(expr, msg=None)
# assertFalse(expr, msg=None)
# assertEqual(first, second, msg=None)
# assertNotEqual(first, second, msg=None}})