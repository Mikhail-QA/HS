import requests
import unittest
from Unit_tests.test_admin_panel import TestFilterSubjects

suite = requests.TestSuite()

suite.addTest(requests.makeSuite(TestFilterSubjects))
