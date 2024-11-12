from abc import ABC, abstractmethod
from ianimal import IAnimal

class Animal(IAnimal, ABC):
    
    def __init__(self, nombre: str, edad: int, peso: float) -> None:
        self._nombre = nombre  # Atributo protegido
        self._edad = edad
        self._peso = peso
        self.__kilos_comidos = 0.0  # Atributo privado

    # Métodos
    def comer(self, kilos: float) -> None:
        """ Aumenta el contador de kilos comidos. """
        self.__kilos_comidos += kilos

    def obtener_kilos_comidos(self) -> float:
        """ Devuelve la cantidad de kilos comidos. """
        return self.__kilos_comidos

    @abstractmethod
    def hacer_sonido(self) -> str:
        """ Método abstracto para hacer un sonido. """
        pass

    # Getters y Setters
    @property
    def nombre(self) -> str:
        """ Devuelve el valor del atributo privado 'nombre' """
        return self._nombre
    
    @nombre.setter
    def nombre(self, value: str) -> None:
        """ Establece un nuevo valor para el atributo 'nombre' """
        if isinstance(value, str):
            self._nombre = value
        else:
            raise ValueError('Expected str')
        
    @property
    def edad(self) -> int:
        """ Devuelve el valor del atributo privado 'edad' """
        return self._edad
    
    @edad.setter
    def edad(self, value: int) -> None:
        """ Establece un nuevo valor para el atributo 'edad' """
        if isinstance(value, int):
            self._edad = value
        else:
            raise ValueError('Expected int')
        
    @property
    def peso(self) -> float:
        """ Devuelve el valor del atributo privado 'peso' """
        return self._peso
    
    @peso.setter
    def peso(self, value: float) -> None:
        """ Establece un nuevo valor para el atributo 'peso' """
        if isinstance(value, float):
            self._peso = value
        else:
            raise ValueError('Expected float')
