import unittest

from ..modules import designpattern
class Test_designpattern(unittest.TestCase):
    def test_DesignPattern(self):
        DP = designpattern.DesignPattern()
        self.assertEqual(DP.type,'')
        self.assertEqual(DP.classlist,[])

if __name__ == '__main__':
    unittest.main()