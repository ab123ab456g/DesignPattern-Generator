import unittest

from ..modules.datatypes.basic import Keyword
from ..modules.datatypes.variable import G_Int, G_Str, G_List, G_Dict, G_Set, G_Tuple, G_Other
from ..modules.datatypes.variable import VariableFactory_equal
from ..modules.datatypes.variable import VariableFactory_add_equal
from ..modules.datatypes.variable import VariableFactory_sub_equal
from ..modules.datatypes.variable import VariableFactory_multi_equal
from ..modules.datatypes.variable import VariableFactory_divi_equal

class Test_variable(unittest.TestCase):
    def test_G_Int(self):
        g = G_Int()
        self.assertEqual(g.datatype, 'int')
        self.assertEqual(g.name, '')
        self.assertEqual(g.value, '')
    def test_G_Str(self):
        g = G_Str()
        self.assertEqual(g.datatype, 'str')
        self.assertEqual(g.name, '')
        self.assertEqual(g.value, '')
    def test_G_List(self):
        g = G_List()
        self.assertEqual(g.datatype, 'list')
        self.assertEqual(g.name, '')
        self.assertEqual(g.value, '')
    def test_G_Tuple(self):
        g = G_Tuple()
        self.assertEqual(g.datatype, 'tuple')
        self.assertEqual(g.name, '')
        self.assertEqual(g.value, '')
    def test_G_Dict(self):
        g = G_Dict()
        self.assertEqual(g.datatype, 'dict')
        self.assertEqual(g.name, '')
        self.assertEqual(g.value, '')
    def test_G_Set(self):
        g = G_Set()
        self.assertEqual(g.datatype, 'set')
        self.assertEqual(g.name, '')
        self.assertEqual(g.value, '')
        g = G_Other(list())
        self.assertEqual(g.datatype, 'other')
        self.assertEqual(g.name, '')
        self.assertEqual(g.value, [])
    def test_VariableFactory_equal(self):
        f = VariableFactory_equal()
        self.assertEqual(f.operator, '=')
        self.assertEqual(type(f.setInt()), type(G_Int()))
        self.assertEqual(type(f.setStr()), type(G_Str()))
        self.assertEqual(type(f.setList()), type(G_List()))
        self.assertEqual(type(f.setTuple()), type(G_Tuple()))
        self.assertEqual(type(f.setDict()), type(G_Dict()))
        self.assertEqual(type(f.setSet()), type(G_Set()))
        self.assertEqual(type(f.setOther('datetime()')), type(G_Other('datetime()')))
    def test_G_VariableFactory_add_equal(self):
        f = VariableFactory_add_equal()
        self.assertEqual(f.operator, '+=')
        self.assertEqual(type(f.setInt()), type(G_Int()))
        self.assertEqual(type(f.setStr()), type(G_Str()))
        self.assertEqual(type(f.setList()), type(G_List()))
        self.assertEqual(type(f.setTuple()), type(G_Tuple()))
        self.assertEqual(type(f.setDict()), type(G_Dict()))
        self.assertEqual(type(f.setSet()), type(G_Set()))
        self.assertEqual(type(f.setOther('datetime()')), type(G_Other('datetime()')))
    def test_VariableFactory_sub_equal(self):
        f = VariableFactory_sub_equal()
        self.assertEqual(f.operator, '-=')
        self.assertEqual(type(f.setInt()), type(G_Int()))
        self.assertEqual(type(f.setStr()), type(G_Str()))
        self.assertEqual(type(f.setList()), type(G_List()))
        self.assertEqual(type(f.setTuple()), type(G_Tuple()))
        self.assertEqual(type(f.setDict()), type(G_Dict()))
        self.assertEqual(type(f.setSet()), type(G_Set()))
        self.assertEqual(type(f.setOther('datetime()')), type(G_Other('datetime()')))
    def test_VariableFactory_multi_equal(self):
        f = VariableFactory_multi_equal()
        self.assertEqual(f.operator, '*=')
        self.assertEqual(type(f.setInt()), type(G_Int()))
        self.assertEqual(type(f.setStr()), type(G_Str()))
        self.assertEqual(type(f.setList()), type(G_List()))
        self.assertEqual(type(f.setTuple()), type(G_Tuple()))
        self.assertEqual(type(f.setDict()), type(G_Dict()))
        self.assertEqual(type(f.setSet()), type(G_Set()))
        self.assertEqual(type(f.setOther('datetime()')), type(G_Other('datetime()')))
    def test_VariableFactory_divi_equal(self):
        f = VariableFactory_divi_equal()
        self.assertEqual(f.operator, '/=')
        self.assertEqual(type(f.setInt()), type(G_Int()))
        self.assertEqual(type(f.setStr()), type(G_Str()))
        self.assertEqual(type(f.setList()), type(G_List()))
        self.assertEqual(type(f.setTuple()), type(G_Tuple()))
        self.assertEqual(type(f.setDict()), type(G_Dict()))
        self.assertEqual(type(f.setSet()), type(G_Set()))
        self.assertEqual(type(f.setOther('datetime()')), type(G_Other('datetime()')))




if __name__ == '__main__':
    unittest.main()

# assertTrue(expr, msg=None)
# assertFalse(expr, msg=None)
# assertEqual(first, second, msg=None)
# assertNotEqual(first, second, msg=None}})