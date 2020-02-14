import unittest

from case.test_login import TestLogin
from case.test_user_file import TestUserFile
from tools.HTMLTestRunner import HTMLTestRunner

suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestLogin))
suite.addTest(unittest.makeSuite(TestUserFile))
with open("./report/report.html","wb") as f:
   HTMLTestRunner(stream=f).run(suite)
