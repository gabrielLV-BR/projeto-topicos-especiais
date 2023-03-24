import numpy as np
import matplotlib.pyplot as plot

from reader import DataReader

class Grapher:
    def __init__(self, values):
        self.values = values

    def graph(self):
        plot.title("Gráfico de linhas")
        plot.ylabel("Valores de entrada")
        plot.xlabel("Amostragem")
        plot.plot(self.values)
        plot.show()

if __name__ == "__main__":
    data = DataReader("data.txt").get_values()
    grapher = Grapher(data)
    grapher.graph()
