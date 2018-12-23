import unittest

from ..modules import base

class Test_base(unittest.TestCase):
    def test_Name(self):
        b = base.Base()
        self.assertEqual(b.name, '')
        b.name = 'test'
        self.assertEqual(b.name, 'test')

if __name__ == '__main__':
    unittest.main()
