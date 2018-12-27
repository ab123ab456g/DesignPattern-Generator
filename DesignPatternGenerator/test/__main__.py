import unittest
from .test_basic import Test_basic
from .test_base import Test_base
from .test_variable import Test_variable
from .test_operator import Test_operator
from .test_structure import Test_structure
from .test_loop import Test_loop
from .test_designpattern import Test_designpattern

from .test_generator import Test_Generator



#from .test_generator import module1
# from test_generator import module2
def test_runner(obj):
    suite = unittest.TestSuite()
    Test_Job = obj
    suite.addTests(Test_Job)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
    print()
    print()
    print()
    print()
    print()
    print()


Test_Job = unittest.TestLoader().loadTestsFromTestCase(Test_basic)
test_runner(Test_Job)
Test_Job = unittest.TestLoader().loadTestsFromTestCase(Test_base)
test_runner(Test_Job)
Test_Job = unittest.TestLoader().loadTestsFromTestCase(Test_Generator)
test_runner(Test_Job)


# Test_Job = unittest.TestLoader().loadTestsFromTestCase(Test_variable)
# test_runner(Test_Job)

# Test_Job = unittest.TestLoader().loadTestsFromTestCase(Test_operator)
# test_runner(Test_Job)

# Test_Job = unittest.TestLoader().loadTestsFromTestCase(Test_structure)
# test_runner(Test_Job)

# Test_Job = unittest.TestLoader().loadTestsFromTestCase(Test_loop)
# test_runner(Test_Job)

# Test_Job = unittest.TestLoader().loadTestsFromTestCase(Test_function)
# test_runner(Test_Job)

# Test_Job = unittest.TestLoader().loadTestsFromTestCase(Test_class)
# test_runner(Test_Job)

# Test_Job = unittest.TestLoader().loadTestsFromTestCase(Test_designpattern)
# test_runner(Test_Job)

# Test_Job10 = unittest.TestLoader().loadTestsFromTestCase(Test_Generator)
# test_runner(Test_Job)
