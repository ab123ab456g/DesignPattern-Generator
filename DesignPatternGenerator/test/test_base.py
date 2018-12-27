import unittest
from ..modules.datatypes import base

class Test_base(unittest.TestCase):

    def test_Base(self):
        TestObj = base.Base()
        self.assertEqual(TestObj.name, '')
        TestObj.name = 'test'
        self.assertEqual(TestObj.name, 'test')
        self.assertTrue(base.Base().isSetValue(TestObj))
        self.assertFalse(base.Base().isSetValue(base.Base()))
        self.assertTrue(base.Base().isSameType(TestObj))
        self.assertFalse(base.Base().isSameType(int()))
        

    def test_Variable(self):
        TestObj = base.Variable()
        self.assertEqual(TestObj.datatype, '')
        self.assertEqual(TestObj.name, '')
        self.assertEqual(TestObj.value, '')
        TestObj.datatype = 'int'
        TestObj.name = 'test'
        TestObj.value = '123'
        TestObj.operator = '='
        self.assertTrue(base.Variable().isSetValue(TestObj))
        self.assertFalse(base.Variable().isSetValue(base.Variable()))
        self.assertTrue(base.Variable().isSameType(TestObj))
        self.assertFalse(base.Variable().isSameType(int()))

    def test_Structure(self):
        TestObj = base.Structure()
        self.assertEqual(TestObj.name,'')
        self.assertEqual(type(TestObj.content),type(base.Content()))
        V = base.Variable()
        V.datatype = 'int'
        V.name = 'test'
        V.value = '123'
        TestObj.name = 'abc'
        V.operator = '='
        self.assertTrue(TestObj.addContent(base.Variable, V))
        self.assertTrue(base.Structure().isSetValue(TestObj))
        self.assertFalse(base.Structure().isSetValue(base.Structure()))
        self.assertTrue(base.Structure().isSameType(TestObj))
        self.assertFalse(base.Structure().isSameType(int()))

    def test_Operaotr(self):
        TestObj = base.Operator()
        self.assertEqual(TestObj.str1,'')
        self.assertEqual(TestObj.operator,'')
        self.assertEqual(TestObj.str2,'')
        TestObj.str1 = 'abc'
        TestObj.operator = '=='
        TestObj.str2 = 'bcd'
        self.assertTrue(base.Operator().isSetValue(TestObj))
        self.assertFalse(base.Operator().isSetValue(base.Operator()))
        self.assertTrue(base.Operator().isSameType(TestObj))
        self.assertFalse(base.Operator().isSameType(int()))

    def test_Content(self):
        TestObj = base.Content()
        self.assertEqual(TestObj.contentlist, [])
        self.assertFalse(base.Content().isSetValue(TestObj))
        self.assertTrue(TestObj.checkAddAllowedConententType(base.Variable, base.Variable()))
        self.assertFalse(TestObj.checkAddAllowedConententType(base.Operator, base.Operator()))
        self.assertTrue(TestObj.checkAddAllowedConententType(base.Call, base.Call()))
        self.assertTrue(TestObj.checkAddAllowedConententType(base.Structure, base.Structure()))
        self.assertTrue(TestObj.checkAddAllowedConententType(base.Function, base.Function()))
        self.assertTrue(TestObj.checkAddAllowedConententType(base.Class, base.Class()))
        self.assertFalse(TestObj.checkAddAllowedConententType(base.Content, base.Content()))
        self.assertFalse(TestObj.checkAddAllowedConententType(base.DesignPattern, base.DesignPattern()))
        self.assertFalse(TestObj.addContent(base.DesignPattern, base.DesignPattern()))
        self.assertFalse(TestObj.addContent(base.Variable, base.Variable()))
        V = base.Variable()
        V.datatype = 'int'
        V.name = 'test'
        V.value = '123'
        V.operator = '='
        self.assertTrue(TestObj.addContent(base.Variable, V))
        self.assertTrue(base.Content().isSetValue(TestObj))
        self.assertFalse(base.Content().isSetValue(base.Content()))
        self.assertTrue(base.Content().isSameType(TestObj))
        self.assertFalse(base.Content().isSameType(int()))

    def test_Call(self):
        TestObj = base.Call()
        self.assertEqual(TestObj.parameterlist, [])
        self.assertTrue(base.Call().isSameType(TestObj))
        self.assertFalse(base.Call().isSameType(int()))
        TestObj.addParameter('abc')
        self.assertEqual(TestObj.parameterlist,['abc'])
        TestObj.name = 'abc'
        self.assertTrue(base.Call().isSetValue(TestObj))
        self.assertFalse(base.Call().isSetValue(base.Call()))

    def test_Loop(self):
        TestObj = base.Loop()
        self.assertEqual(TestObj.condition,'')
        self.assertEqual(TestObj.contentlist,[])
        self.assertTrue(base.Loop().isSameType(TestObj))
        O = base.Operator()
        O.str1 = 'abc'
        O.operator = '=='
        O.str2 = 'bcd'
        TestObj.condition = O
        self.assertFalse(base.Loop().isSameType(int()))
        self.assertTrue(base.Loop().isSetValue(TestObj))
        self.assertFalse(base.Loop().isSetValue(base.Loop()))
        V = base.Variable()
        V.datatype = 'int'
        V.name = 'test'
        V.value = '123'
        V.operator = '='
        self.assertTrue(TestObj.addContent(base.Variable, V))

    def test_Function(self):
        TestObj = base.Function()
        self.assertEqual(TestObj.parameterlist,[])
        self.assertTrue(base.Function().isSameType(TestObj))
        self.assertFalse(base.Function().isSameType(int()))
        TestObj.addParameter('abc')
        TestObj.name = 'test'
        self.assertTrue(base.Function().isSetValue(TestObj))
        self.assertFalse(base.Function().isSetValue(base.Function()))
        self.assertEqual(type(TestObj.content),type(base.Content()))

    def test_Class(self):
        TestObj = base.Class()
        self.assertEqual(TestObj.variablelist,[])
        self.assertEqual(TestObj.methodlist,[])
        self.assertTrue(base.Class().isSameType(TestObj))
        self.assertFalse(base.Class().isSameType(int()))
        TestObj.name = 'abc'
        self.assertTrue(base.Class().isSetValue(TestObj))
        self.assertFalse(base.Class().isSetValue(base.Class()))
        V = base.Variable()
        V.datatype = 'int'
        V.name = 'test'
        V.value = '123'
        V.operator = '='
        self.assertTrue(TestObj.addVariable(V))
        self.assertFalse(TestObj.addVariable(int()))
        F = base.Function()
        F.name = 'abc'
        self.assertTrue(TestObj.addMethod(F))
        self.assertFalse(TestObj.addMethod(int()))
        self.assertFalse(TestObj.isInherit(TestObj))
        TestObj.inherit_class = 'abc'
        self.assertTrue(TestObj.isInherit(TestObj))

    def test_DesignPattern(self):
        TestObj = base.DesignPattern()
        self.assertEqual(TestObj.type,'')
        self.assertEqual(TestObj.classlist,[])
        self.assertTrue(base.DesignPattern().isSameType(TestObj))
        self.assertFalse(base.DesignPattern().isSameType(int()))
        C = base.Class()
        self.assertTrue(TestObj.addClass(C))
        self.assertFalse(TestObj.addClass(int()))
        

if __name__ == '__main__':
    unittest.main()
