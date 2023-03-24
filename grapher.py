import numpy as np
import matplotlib.pyplot as plot

from reader import DataReader

class Grapher:
    def __init__(self, values):
        self.values = values

    def graph(self):
        plot.plot(self.values)
        plot.ylabel("Valores de entrada")
        plot.xlabel("Amostragem")
        plot.show()

if __name__ == "__main__":
    data = DataReader("data.txt").get_values()
    grapher = Grapher(data)
    grapher.graph()
