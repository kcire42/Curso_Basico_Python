import unittest

def es_mayor_de_edad(edad):
    if edad >= 18:
        return True
    else:
        return False

class PruebaDeCristalTest(unittest.TestCase):
    pass
    def test_es_mayor_de_edad(self):
        edad = int(input("Ingrese su edad: "))
        resultado = es_mayor_de_edad(edad)
        self.assertEqual(resultado,True)
    def test_es_menor_de_edad(self):
        edad = int(input("Ingrese su edad: "))
        resultado = es_mayor_de_edad(edad)
        self.assertEqual(resultado,False)
        


if __name__ == '__main__':
    unittest.main()