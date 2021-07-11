import unittest
from pocs.python.plz.greetings import greetings

class GreetingTest(unittest.TestCase):
  def test_greeting(self):
    self.assertTrue(greetings.greeting())
