import numpy as np
import matplotlib.pyplot as plot

from reader import DataReader

class Grapher:
    def __init__(self, reader):
        self.reader = reader

    def graph(self):
        plot.ylabel("Valores de entrada")
        plot.xlabel("Amostragem")

        plot.subplot(1, 2, 1)
        plot.title("Gráfico de linhas")
        self._graph_values()

        plot.subplot(1, 2, 2)
        plot.title("Média das séries")
        self._graph_means()
    
        plot.legend(loc="upper left")
        plot.show()

    def _graph_values(self):
        values = self.reader.get_values()
        for i, value in enumerate(values):
            plot.plot(value, label=f"Série {i}")
        
    def _graph_means(self):
        values = self.reader.get_means()
        xvalues = np.arange(1, len(values) + 1)

        plot.bar(xvalues, values)
        plot.xticks(xvalues, ["Série " + str(x) for x in xvalues])

if __name__ == "__main__":
    reader = DataReader("data.txt")
    grapher = Grapher(reader)
    grapher.graph()
