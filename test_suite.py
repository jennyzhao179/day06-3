import unittest

from case.test_login import TestLogin
from case.test_user_file import TestUserFile

suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestLogin))
suite.addTest(unittest.makeSuite(TestUserFile))
unittest.TextTestRunner(verbosity=2).run(suite)
