# from typing import Type
from .animal import Animal
from ..interfaces.locomover import LocomoverInterface

class Pinguim(Animal, LocomoverInterface):

    def nascer(self):
        Animal._nascer()
        print("de um ovo!")

    def locomover(self):
        print("Eu posso nadar ou andar fofinho sobre duas patas")