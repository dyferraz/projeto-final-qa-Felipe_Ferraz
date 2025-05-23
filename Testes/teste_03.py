#Teste 3: Validar E-mail Simples
#Nome do Teste: test_email_valido
#Objetivo: Testar se a função detecta e-mails válidos (formato básico: texto@texto.texto).
#Biblioteca: unittest.
#Resultado Esperado:
#"user@example.com" deve retornar True.
#"user@com" deve retornar False


import unittest

def email_valido(email):
    return '@' in email and '.' in email.split('@')[-1]

class TestEmailValido(unittest.TestCase):
    def test_email_valido(self):
        self.assertTrue(email_valido("user@example.com"))  # E-mail válido
        self.assertFalse(email_valido("user@com"))         # E-mail inválido

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
