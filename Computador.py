from abc import ABC, abstractmethod


class Computador(ABC):

    def __init__(self, modelo, cor, preco):
        self.modelo = modelo
        self.cor = cor
        self.preco = preco

    def getInformacoes(self):
        print("Modelo: " + self.modelo)
        print("Cor: " + self.cor)
        print("Preco: " + str(self.preco))

    @abstractmethod
    def cadastrar(self):
        pass

    def modelo(self):
        return self.modelo

    def cor(self):
        return self.cor

    def preco(self):
        return self.preco

    def setModelo(self, value):
        self.modelo = value

    def setCor(self, value):
        self.cor = value

    def setPreco(self, value):
        self.preco = value
