# boa_constrictor.py
from animal_exotico import Animal_Exotico

class Boa_Constrictor(Animal_Exotico):
    def __init__(self, nombre, peso, edad, pais_origen, impuestos):
        super().__init__(nombre, peso, edad, pais_origen, impuestos)
        self.ratones_comidos = 0

    def hacer_sonido(self):
        return "¡Tsss!"

    def agregar_raton(self):
        if self.ratones_comidos >= 20:
            raise ValueError("Demasiados Ratones!")
        self.ratones_comidos += 1

    def obtener_ratones_comidos(self):
        return self.ratones_comidos
