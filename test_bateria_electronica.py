# test TDD bateria_electronica
import unittest
from bateria_electronica import BateriaElectronica

class TestBateriaElectronica(unittest.TestCase):
    # Creamos una instancia de BateriaElectronica antes de cada prueba
    def setUp(self):
        self.bateria = BateriaElectronica(max_volumen=100, volumen_inicial=50)

    def test_valor_inicial(self):
        # Verifico valores iniciales usando los métodos getter
        self.assertEqual(self.bateria.obtener_volumen(), 50)
        self.assertEqual(self.bateria.obtener_max_volumen(), 100)
        self.assertFalse(self.bateria.obtener_estado())
        
    # Prueba de que la batería se encienda
    def test_encender(self):
        self.bateria.encender()
        self.assertTrue(self.bateria.obtener_estado())

    # Prueba de que la batería se apague
    def test_apagar(self):
        self.bateria.encender()
        self.bateria.apagar()
        self.assertFalse(self.bateria.obtener_estado())

    def test_ajustar_volumen(self):
        # Ajuste de volumen dentro del rango permitido
        self.bateria.ajustar_volumen(70)
        self.assertEqual(self.bateria.obtener_volumen(), 70)
    
    def test_volumen_fuera_rango(self):
        # Ajuste de volumen mayor que el máximo
        self.bateria.ajustar_volumen(120)
        self.assertEqual(self.bateria.obtener_volumen(), 100)  # Lo lleva a 100
    
        # Ajustar volumen menor que 0
        self.bateria.ajustar_volumen(-10)
        self.assertEqual(self.bateria.obtener_volumen(), 0)  # Lo lleva a 0

    def test_str(self):
        self.bateria.encender()
        self.assertEqual(str(self.bateria), "Batería Electrónica - Estado: Encendida, Volumen: 50")

if __name__ == '__main__':
    unittest.main()
