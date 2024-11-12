from abc import ABC, abstractmethod

# Interfaz iAnimal
class IAnimal(ABC):
    @abstractmethod
    def hacer_sonido(self):
        pass

    @abstractmethod
    def comer(self, comida):
        pass

    @abstractmethod
    def obtener_kilos_comidos(self):
        pass

# Clase base Animal
class Animal(IAnimal):
    def __init__(self, nombre, peso, edad):
        self._nombre = nombre
        self._peso = peso
        self._edad = edad

    def obtener_nombre(self):
        return self._nombre

    def obtener_peso(self):
        return self._peso

    def obtener_edad(self):
        return self._edad
