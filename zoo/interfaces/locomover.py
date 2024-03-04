from abc import ABC, abstractclassmethod

class LocomoverInterface(ABC):

    @abstractclassmethod
    def locomover(self):
        return