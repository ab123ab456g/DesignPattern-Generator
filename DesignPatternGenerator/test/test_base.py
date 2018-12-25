import unittest

from ..modules import base

class Test_base(unittest.TestCase):
    def test_Base(self):
        b = base.Base()
        self.assertEqual(b.name, '')
        b.name = 'test'
        self.assertEqual(b.name, 'test')

        v = base.Variable()
        self.assertEqual(v.datatype, '')
        self.assertEqual(v.name, '')
        self.assertEqual(v.value, '')

        O = base.Operator()
        self.assertEqual(O.str1,'')
        self.assertEqual(O.operator,'')
        self.assertEqual(O.str2,'')

        S = base.Structure()
        self.assertEqual(S.name,'')
        self.assertEqual(S.contentlist,[])
        S.addContent('content1')
        S.addContent('content2')
        S.addContent('content3')
        S.addContent('content4')
        self.assertEqual(S.contentlist,['content1', 'content2', 'content3', 'content4'])

        F = base.Function()
        self.assertEqual(F.parameterlist,[])
        self.assertEqual(F.contentlist,[])

        L = base.Loop()
        self.assertEqual(L.condition,'')
        self.assertEqual(L.contentlist,[])

        C = base.Class()
        self.assertEqual(C.parameterlist,[])
        self.assertEqual(C.methodList,[])

        DP = base.DesignPattern()
        self.assertEqual(DP.type,'')
        self.assertEqual(DP.classlist,[])

if __name__ == '__main__':
    unittest.main()
