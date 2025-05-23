#Teste 1: Verificar Palíndromo
#Nome do Teste: test_eh_palindromo
#Objetivo: Verificar se a função identifica corretamente palavras palíndromas (que são iguais lidas de trás para frente).
#Biblioteca: unittest (padrão do Python).
#Resultado Esperado:
#"ovo" deve retornar True.
#"python" deve retornar False

import unittest

def eh_palindromo(palavra):
    return palavra == palavra[::-1]

class TestPalindromo(unittest.TestCase):
    def test_eh_palindromo(self):
        self.assertTrue(eh_palindromo("ovo"))  # "ovo" é palíndromo
        self.assertFalse(eh_palindromo("python"))  # "python" não é

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
