# from typing import Type
from .animal import Animal
from ..interfaces.locomover import LocomoverInterface

class Panda(Animal, LocomoverInterface):

    def nascer(self):
        Animal._nascer()
        print("de um mamífero!")