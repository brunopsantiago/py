import unittest
from src.main import soma


class TestSoma(unittest.TestCase):
    def test_retorno_soma(self):
        self.assertEqual(soma(10, 7), 17)

    def test_retorno_soma_1(self):
        self.assertEqual(soma(10, 17), 27)

    def test_retorno_soma_negativo(self):
        self.assertEqual(soma(-10, 17), 7)
