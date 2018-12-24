import unittest

from ..modules import loop
class Test_loop(unittest.TestCase):
    def test_Loop(self):
        L = loop.Loop()
        self.assertEqual(L.condition,'')
        self.assertEqual(L.contentlist,[])

if __name__ == '__main__':
    unittest.main()
