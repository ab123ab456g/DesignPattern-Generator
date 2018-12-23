import unittest
from ..modules import basic

class Test_basic(unittest.TestCase):
    def test_language(self):
        langlist = ['Python']
        L = basic.Language()
        # test __init__ function
        self.assertEqual(L.uselang,'Python')
        self.assertEqual(L.langlist, langlist)
        self.assertEqual(L.changeStringFormat('abc'),'Abc')
        self.assertTrue(L.checkIsSupport('python'))
        self.assertFalse(L.checkIsSupport('C'))
        L.setUseLang('Python')
        self.assertEqual(L.uselang,'Python')
        L.setUseLang('C')
        self.assertEqual(L.uselang, 'C Not Support')
    def test_keyword(self):
        datatype = ['int', 'str', 'None', 'list', 'dict', 'set', 'tuple', 'other']
        set_value_operaotr = ['=', '+=', '-=', '*=', '/=']
        compute_operator = ['+', '-', '*'  '/' , '%','//', '**']
        compare_operaotor = ['==', '!=', '>', '>=', '<', '<=']
        logic_operator = ['and', 'or', 'not', 'is', 'is not','in']
        bitwise_operator = ['&', '|', '~', 'a^b']
        structure = ['if', 'elif', 'else']
        function = ['def']
        class_ = ['class']
        design_pattern = []
        self.assertEqual(basic.Keyword.datatype,datatype)
        self.assertEqual(basic.Keyword.set_value_operaotr,set_value_operaotr)
        self.assertEqual(basic.Keyword.compute_operator,compute_operator)
        self.assertEqual(basic.Keyword.compare_operaotor,compare_operaotor)
        self.assertEqual(basic.Keyword.logic_operator,logic_operator)
        self.assertEqual(basic.Keyword.bitwise_operator,bitwise_operator)

        self.assertEqual(basic.Keyword.structure, structure)
        self.assertEqual(basic.Keyword.function, function)
        self.assertEqual(basic.Keyword.class_,class_)
        self.assertEqual(basic.Keyword.design_pattern, design_pattern)


if __name__ == '__main__':
    unittest.main()