from Computador import Computador


class Notebook(Computador):

    def __init__(self, tempoDeBateria, modelo, cor, preco):
        super().__init__(modelo, cor, preco)
        self.__tempoDeBateria = tempoDeBateria

    def getInformacoes(self):
        super().getInformacoes()
        print("Tempo bateria: " + self.tempoDeBateria)

    @property
    def tempoDeBateria(self):
        return self.__tempoDeBateria

    @tempoDeBateria.setter
    def tempoDeBateria(self, tempoDeBateria):
        self.__tempoDeBateria = tempoDeBateria

    def cadastrar(self):
        print("Cadastrar novo tempo de bateria")
        tempoBateria = input("Tempo de bateria: ")
        self.tempoDeBateria = tempoBateria
        print("Tempo cadastrado com sucesso!")