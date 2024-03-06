# from typing import Type
from .Animal import Animal
from ..interfaces.Locomover import LocomoverInterface

class Panda(Animal, LocomoverInterface):

    def _nascer(self):
        Animal._nascer()
        print("\nNascedo de um mamífero!")

    def locomover(self):
        print("Eu posso andar em pé ou usando as quatro patas!")


