# Construir código necessário em Python para implementar o seguinte projeto: Uma classe abstrata chamada
# de Computador
# que contém os atributos/propriedades: modelo, cor e preço. Esta classe possui um método getInformacoes() que retorna
# todos os valores dos atributos. Esta classe também possui um método abstrato cadastrar().

#O projeto também deve possuir as classes Desktop e Notebook que herdam da classe Computador.
# A classe Desktop possui o atributo/propriedade fracamente privado potenciaDaFonte.
# Esta classe reimplementa o método getInformacoes() herdado de computador.

#A classe Notebook possui o atributo/propriedade fortemente privado tempoDeBateria. Esta classe reimplementa o
# método getInformacoes() herdado de computador

#Construa um arquivo do tipo main com a utilização das classes construídas, para teste dos algoritmos.

from Desktop import Desktop
from Notebook import Notebook

desktop = Desktop("700w", "modelo1", "preto", 6000)
desktop.getInformacoes()
desktop.cadastrar()
print(desktop.potenciaFonte)

notebook = Notebook("400w", "modelo12", "azul", 7000)
notebook.getInformacoes()
notebook.cadastrar()
print(notebook.tempoDeBateria)
