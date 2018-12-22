import unittest
from .test_base import Test_Base
from .test_variable import Test_Variable
from .test_generator import module1
# from test_generator import module2


suite = unittest.TestSuite()

Test_Job1 = unittest.TestLoader().loadTestsFromTestCase(Test_Base)
Test_Job2 = unittest.TestLoader().loadTestsFromTestCase(Test_Variable)

suite.addTests(Test_Job1)
suite.addTests(Test_Job2)

runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)