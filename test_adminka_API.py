import unittest
from Unit_tests.test_admin_panel import TestFilterSubjects

suite = unittest.TestSuite()

suite.addTest(unittest.makeSuite(TestFilterSubjects))
