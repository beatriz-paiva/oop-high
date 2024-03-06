# from typing import Type
from .Animal import Animal
from ..interfaces.Locomover import LocomoverInterface

class Pinguim(Animal, LocomoverInterface):

    def _nascer(self):
        Animal._nascer()
        print("\nNascendo de um ovo!")

    def locomover(self):
        print("Eu posso nadar ou andar fofinho sobre duas patas")