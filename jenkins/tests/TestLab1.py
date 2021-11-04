import unittest
from Lab1 import Equation

class TestEquation(unittest.TestCase):
  #setUp method is overridden from the parent class TestCase
  def setUp(self):
    self.equation = Equation(1,-10,9)
  #Each test method starts with the keyword test_
  def test_getDiscriminant(self):
    self.assertEqual(self.equation.getDiscriminant(), 64)

# Executing the tests in the above test case class
if __name__ == "__main__":
  unittest.main()