import unittest

def area_quadrado(lado):
    return lado ** 2

class TestAreaQuadrado(unittest.TestCase):
    def test_area_quadrado(self):
        self.assertEqual(area_quadrado(5), 25)  # 5² = 25
        self.assertEqual(area_quadrado(0), 0)    # 0² = 0

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
