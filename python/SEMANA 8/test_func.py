# unittest é um testRunner (realiza testes) da biblioteca python
import unittest
from func import soma, mult

# nesse caso é possível testar mais de uma função mesmo dando erro, diferente do arquivo teste_automatizado
# onde o teste parava quando encontrava uma funcao com erro

class TestSum(unittest.TestCase):
    def test_sum1(self):
        self.assertEqual(soma([1, 2, 3]), 6, "Deve ser 6")
    def test_sum2(self):
        self.assertEqual(mult((2, 3, 4)), 24, "Deve ser 24")

if __name__ == "__main__":
    unittest.main()