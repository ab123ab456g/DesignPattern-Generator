import unittest
from .test_basic import Test_basic
from .test_base import Test_base
from .test_variable import Test_variable
from .test_operator import Test_operator

#from .test_generator import module1
# from test_generator import module2


suite = unittest.TestSuite()

Test_Job0 = unittest.TestLoader().loadTestsFromTestCase(Test_basic)
Test_Job1 = unittest.TestLoader().loadTestsFromTestCase(Test_base)
Test_Job2 = unittest.TestLoader().loadTestsFromTestCase(Test_variable)
Test_Job3 = unittest.TestLoader().loadTestsFromTestCase(Test_operator)
# Test_Job4 = unittest.TestLoader().loadTestsFromTestCase(Test_operator)
# Test_Job5 = unittest.TestLoader().loadTestsFromTestCase(Test_operator)
# Test_Job6 = unittest.TestLoader().loadTestsFromTestCase(Test_operator)
# Test_Job7 = unittest.TestLoader().loadTestsFromTestCase(Test_operator)
# Test_Job8 = unittest.TestLoader().loadTestsFromTestCase(Test_operator)
# Test_Job9 = unittest.TestLoader().loadTestsFromTestCase(Test_operator)
# Test_Job10 = unittest.TestLoader().loadTestsFromTestCase(Test_operator)

suite.addTests(Test_Job0)
suite.addTests(Test_Job1)
suite.addTests(Test_Job2)
suite.addTests(Test_Job3)
# suite.addTests(Test_Job4)
# suite.addTests(Test_Job5)
# suite.addTests(Test_Job6)
# suite.addTests(Test_Job7)
# suite.addTests(Test_Job8)
# suite.addTests(Test_Job9)
# suite.addTests(Test_Job10)



runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)