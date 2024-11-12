from animal import Animal
class Animal_Exotico(Animal):
    def __init__(self, nombre, peso, edad, pais_origen, impuestos):
        super().__init__(nombre, peso, edad)
        self.pais_origen = pais_origen
        self.impuestos = impuestos

    def calcular_flete(self):
        return self.impuestos * self._peso