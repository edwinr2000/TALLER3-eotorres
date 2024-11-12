import unittest
from boa_constrictor import Boa_Constrictor
from guarderia import Guarderia

class TestBoaConstrictor(unittest.TestCase):
    def setUp(self):
        self.boa = Boa_Constrictor(nombre="Boa", peso=50, edad=5, pais_origen="Brasil", impuestos=15)

    def test_agregar_raton_lanza_excepcion(self):
        for _ in range(9): 
            self.boa.agregar_raton()
        with self.assertRaises(ValueError, msg="Esperaba que se lanzara una excepción por demasiados ratones"):
            self.boa.agregar_raton()

    def test_agregar_raton_no_lanza_excepcion(self):
        for _ in range(9):
            self.boa.agregar_raton()
        self.assertEqual(len(self.boa.ratones), 9, msg="La boa no tiene el número esperado de ratones")

class TestGuarderia(unittest.TestCase):
    def setUp(self):
        # Crear la guardería
        self.guarderia = Guarderia()

    def test_alimentar_boa_exito(self):
        resultado = self.guarderia.alimentar_boa(self.guarderia.boas[0])
        self.assertEqual(resultado, "Éxito", msg="Esperaba que el resultado fuera 'Éxito' al alimentar la boa")

    def test_alimentar_boa_llena(self):
        boa = self.guarderia.boas[0]
        for _ in range(9):
            boa.agregar_raton()  # Alimentamos la boa con 9 ratones
        resultado = self.guarderia.alimentar_boa(boa)
        self.assertEqual(resultado, "La boa está llena", msg="Esperaba que la boa esté llena cuando se intente alimentarla nuevamente")

    def test_alimentar_boa_inexistente(self):
        # Verificar que se maneje el caso de una boa inexistente
        resultado = self.guarderia.alimentar_boa(None)
        self.assertEqual(resultado, "Esta Boa no existe!", msg="Esperaba que se manejara correctamente la situación de boa inexistente")

if __name__ == '__main__':
    unittest.main()
