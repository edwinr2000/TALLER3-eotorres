from boa_constrictor import Boa_Constrictor
from huron import Huron

class Guarderia:
    def __init__(self):
        self.boas = [Boa_Constrictor("Boa1", 50, 5, "Brasil", 15),
                     Boa_Constrictor("Boa2", 45, 4, "Perú", 12)]
        self.hurones = [Huron("Huron1", 10, 2, "EEUU", 5),
                        Huron("Huron2", 12, 3, "Canadá", 7)]

    def alimentar_boa(self, boa):
        if boa is None:
            return "Esta Boa no existe!"

        try:
            # Intentar alimentar la boa
            boa.agregar_raton()
            return "Éxito"
        except ValueError:
            # Capturar el error si la boa ha comido demasiados ratones
            return "La boa está llena"
