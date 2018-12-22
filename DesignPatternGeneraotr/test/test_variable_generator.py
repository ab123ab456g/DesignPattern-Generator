import unittest
from ..modules.variable_generator import VariableGenerator
from ..modules.variable_generator import IntGenerator
from ..modules.variable_generator import StrGenerator
from ..modules.variable_generator import ListGenerator
from ..modules.variable_generator import DictGenerator
from ..modules.variable_generator import SetGenerator
from ..modules.variable_generator import TupleGenerator
from ..modules.variable_generator import OtherGenerator

class Test_Variable_Generator(unittest.TestCase):
    def test_VariableGenerator(self):
        pass
    def test_IntGenerator(self):
        data = [('a',1),('b',2),('c',3)]
        I_G = IntGenerator()
        I_G.addList(data)
        I_G.print()

    def test_StrGenerator(self):
        pass
    def test_ListGenerator(self):
        pass
    def test_DictGenerator(self):
        pass
    def test_SetGenerator(self):
        pass
    def test_TupleGenerator(self):
        pass
    def test_OtherGenerator(self):
        pass

if __name__ == '__main__':
    unittest.main()
