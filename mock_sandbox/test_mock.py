import unittest
from nose.plugins.attrib import attr

class MockTestCase(unittest.TestCase):
    def test_something(self):
        self.assertTrue(True)
