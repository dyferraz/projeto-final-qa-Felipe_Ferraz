#Teste 2: Calcular Área do Quadrado
#Nome do Teste: test_area_quadrado
#Objetivo: Validar se a função calcula corretamente a área de um quadrado.
#Biblioteca: unittest.
#Resultado Esperado:
#Lado 5 deve retornar área 25.
#Lado 0 deve retornar 0 

import unittest

def area_quadrado(lado):
    return lado ** 2

class TestAreaQuadrado(unittest.TestCase):
    def test_area_quadrado(self):
        self.assertEqual(area_quadrado(5), 25)  # 5² = 25
        self.assertEqual(area_quadrado(0), 0)    # 0² = 0

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
