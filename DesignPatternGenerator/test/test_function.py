import unittest

from ..modules import function
class Test_function(unittest.TestCase):
    def test_Function(self):
        F = function.Function()
        self.assertEqual(F.parameterlist,[])
        self.assertEqual(F.contentlist,[])

if __name__ == '__main__':
    unittest.main()
