from .Animal import Animal
from ..interfaces.Locomover import LocomoverInterface


class Galinha(Animal, LocomoverInterface):
    
    def _nascer(self):
        Animal._nascer()
        print("\nNascendo de um ovo!")

    def locomover(self):
        print("Eu ando em dois pés, com unhas pintadas!")

