from unittest import TestCase
from aula06 import multiplicar
from aula06 import divisão

class TestMultiplicar(TestCase):

    def test_multiplicar_dois_por_tres(self):
        self.assertEqual(multiplicar(2,3), 6)

class TestDivisao(TestCase):

    def test_divisão_dois_por_tres(self):
        self.assertEqual(divisão(2,3), -1)

if __name__ == '__main__':
    unittest.main()