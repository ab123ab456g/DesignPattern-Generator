import unittest

from ..modules import class_
class Test_class(unittest.TestCase):
    def test_Class(self):
        C = class_.Class()
        self.assertEqual(C.parameterlist,[])
        self.assertEqual(C.methodList,[])

if __name__ == '__main__':
    unittest.main()