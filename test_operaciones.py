import unittest
from operaciones import sumar, restar, dividir, multiplicar

class TestOperaciones(unittest.TestCase):

    def test_sumar(self):
        self.assertEqual(sumar(3, 2), 5)
        self.assertEqual(sumar(-1, 1), 0)
        self.assertEqual(sumar(-1, -1), -2)
        self.assertEqual(sumar(0, 0), 0)
        
    def test_restar(self):
        self.assertEqual(restar(3, 2), 1)
        self.assertEqual(restar(-1, 1), -2)
        self.assertEqual(restar(-1, -1), 0)
        self.assertEqual(restar(0, 0), 0)

    def test_dividir(self):
        self.assertEqual(dividir(4, 2), 2)
        self.assertEqual(dividir(-1, 1), -1)
        self.assertEqual(dividir(5, 0), None)
        self.assertEqual(dividir(0, 1), 0)

    def test_multiplicar(self):
        self.assertEqual(multiplicar(3, 2), 6)
        self.assertEqual(multiplicar(-1, 1), -1)
        self.assertEqual(multiplicar(-1, 0), 0)
        self.assertEqual(multiplicar(0, 0), 0)

if __name__ == '__main__':
 unittest.main()