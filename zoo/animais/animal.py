from abc import ABC, abstractclassmethod


class Animal(ABC):

    nome: str
    idade: int

    def __init__(self, nome, idade):
        if not isinstance(nome, str):
            raise ValueError("O nome deve ser do tipo 'string'")
        
        if not isinstance(idade, int):
            raise ValueError("A idade dever ser do tipo 'int'")
        self.nome = nome
        self.idade = idade
        print(self.nome)
        print(self.idade)

    @abstractclassmethod
    def _nascer(self):
        pass



