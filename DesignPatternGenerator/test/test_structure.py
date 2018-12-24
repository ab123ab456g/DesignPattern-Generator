import unittest

from ..modules import Operator
from ..modules import structure

O = Operator.Operator()
O2 = Operator.Operator()
O2.str1 = 'a'
O2.str2 = 'b'
O2.operator = '=='

class Test_structure(unittest.TestCase):
    def test_structure(self):
        S = structure.Structure()
        self.assertEqual(S.name,'')
        self.assertEqual(S.contentlist,[])
        S.addContent('content1')
        S.addContent('content2')
        S.addContent('content3')
        S.addContent('content4')
        self.assertEqual(S.contentlist,['content1', 'content2', 'content3', 'content4'])

        S = structure.If()
        S.setCondition()
        self.assertEqual(S.name,'if')
        self.assertEqual(S.contentlist,[])
        self.assertEqual(S.condition.operator, '==')
        self.assertEqual(S.condition.str1, 'var1')
        self.assertEqual(S.condition.str2, 'var2')
        S.setCondition(O)
        self.assertEqual(S.condition.operator, '==')
        self.assertEqual(S.condition.str1, 'var1')
        self.assertEqual(S.condition.str2, 'var2')
        S.setCondition(O2)
        self.assertEqual(S.condition.operator, '==')
        self.assertEqual(S.condition.str1, 'a')
        self.assertEqual(S.condition.str2, 'b')


        S = structure.Elif()
        S.addCondition()
        S.addCondition(O)
        S.addCondition(O2)
        S.setCondition(O)
        self.assertEqual(S.conditionlist[0].operator, '==')
        self.assertEqual(S.conditionlist[0].str1, 'var1')
        self.assertEqual(S.conditionlist[0].str2, 'var2')
        S.setCondition(O)
        self.assertEqual(S.conditionlist[1].operator, '==')
        self.assertEqual(S.conditionlist[1].str1, 'var1')
        self.assertEqual(S.conditionlist[1].str2, 'var2')
        S.setCondition(O2)
        self.assertEqual(S.conditionlist[2].operator, '==')
        self.assertEqual(S.conditionlist[2].str1, 'a')
        self.assertEqual(S.conditionlist[2].str2, 'b')
        self.assertEqual(S.name,'elif')
        self.assertEqual(S.contentlist,[])
        S = structure.Else()
        self.assertEqual(S.name,'else')
        self.assertEqual(S.contentlist,[])

if __name__ == '__main__':
    unittest.main()