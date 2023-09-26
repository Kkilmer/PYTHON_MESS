import unittest
from conceito_aula06 import multiplicar
from conceito_aula06 import divisão
from conceito_aula06 import somar

class TestMultiplicar(unittest.TestCase):

    def test_multiplicar_dois_por_tres(self):
        self.assertEqual(multiplicar(2,3), 6)

class TestDivisao(unittest.TestCase):

    def test_divisão_dois_por_tres(self):
        self.assertEqual(divisão(2,3), 5)

class TestSomar(unittest.TestCase):

    def test_somar_dois_por_tres(self):
        self.assertEqual(somar(2,3), 5)

if __name__ == '__main__':
    unittest.main()