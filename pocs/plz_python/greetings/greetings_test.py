import unittest
from pocs.plz_hello_world.greetings import greetings

class GreetingTest(unittest.TestCase):
  def test_greeting(self):
    self.assertTrue(greetings.greeting())
