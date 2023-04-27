from Computador import Computador


class Desktop(Computador):

    def __init__(self, potenciaFonte, modelo, cor, preco):
        super().__init__(modelo, cor, preco)
        self._potenciaFonte = potenciaFonte

    def getInformacoes(self):
        super().getInformacoes()
        print("Potencia fonte: " + str(self.potenciaFonte))

    @property
    def potenciaFonte(self):
        return self._potenciaFonte

    @potenciaFonte.setter
    def potenciaFonte(self, potenciaFonte):
        self._potenciaFonte = potenciaFonte

    def cadastrar(self):
        print("Cadastrar nova potencia da fonte")
        potenciaFonte = input("Potencia da fonte: ")
        self.potenciaFonte = potenciaFonte
        print("Potencia da fonte cadastrado com sucesso!")
