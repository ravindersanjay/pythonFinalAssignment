import unittest
from DemoQa.library import HTMLTestRunner
from DemoQa.TestCases.myUnitTest import TestStringMethods
# from DemoQa.TestCases.driver import TestStringMethods
from DemoQa.library.config import current_datetime

# ---Can include any number of testcases to run sequentially--#
# test1 = unittest.TestLoader().loadTestsFromTestCase(Test2)
test3 = unittest.TestLoader().loadTestsFromTestCase(TestStringMethods)

# suite = unittest.TestSuite([test1, test2])
suite = unittest.TestSuite([test3])
outfile = open("../reports/TestSummary_TestSuite2.html", "w")
# outfile = open("../reports/TestSummary_TestSuite2" + current_datetime + ".html", "w")
# configure HTMLTestRunner options
runner = HTMLTestRunner.HTMLTestRunner(stream=outfile, title='Test Report', description='Smoke Tests')

# run the suite using HTMLTestRunner
runner.run(suite)
