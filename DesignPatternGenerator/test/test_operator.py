import unittest

from ..modules import operator

class Test_operator(unittest.TestCase):
    def test_operator(self):
        O = operator.Operator()
        self.assertEqual(O.str1,'')
        self.assertEqual(O.operator,'')
        self.assertEqual(O.str2,'')

if __name__ == '__main__':
    unittest.main()

