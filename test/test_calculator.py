import unittest

from src.calulator import suma

class CalculatorTest(unittest.TestCase):
   
    #Prueba unitaria para la función suma
    def test_suma(self):
        self.assertEqual(suma(4, 3), 7)

