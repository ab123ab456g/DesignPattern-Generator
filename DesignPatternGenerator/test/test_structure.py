import unittest

from ..modules.datatypes import Operator
from ..modules.datatypes import structure

class Test_structure(unittest.TestCase):
    def test_structure(self):
        S = structure.If()
        S.addCondition()
        self.assertEqual(S.name,'if')
        self.assertEqual(S.condition.operator, '==')
        self.assertEqual(S.condition.str1, 'var1')
        self.assertEqual(S.condition.str2, 'var2')
        S.addCondition(O)
        self.assertEqual(S.condition.operator, '==')
        self.assertEqual(S.condition.str1, 'var1')
        self.assertEqual(S.condition.str2, 'var2')
        S.addCondition(O2)
        self.assertEqual(S.condition.operator, '==')
        self.assertEqual(S.condition.str1, 'a')
        self.assertEqual(S.condition.str2, 'b')


        S = structure.Elif()
        S.addCondition()
        self.assertEqual(S.conditionlist[0].operator, '==')
        self.assertEqual(S.conditionlist[0].str1, 'var1')
        self.assertEqual(S.conditionlist[0].str2, 'var2')
        S.addCondition(O)
        self.assertEqual(S.conditionlist[1].operator, '==')
        self.assertEqual(S.conditionlist[1].str1, 'var1')
        self.assertEqual(S.conditionlist[1].str2, 'var2')
        S.addCondition(O2)
        self.assertEqual(S.conditionlist[2].operator, '==')
        self.assertEqual(S.conditionlist[2].str1, 'a')
        self.assertEqual(S.conditionlist[2].str2, 'b')
        self.assertEqual(S.name,'elif')
        # self.assertEqual(S.content,[])
        S = structure.Else()
        self.assertEqual(S.name,'else')
        # self.assertEqual(S.content,[])

if __name__ == '__main__':
    unittest.main()