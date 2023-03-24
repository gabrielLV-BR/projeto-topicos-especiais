class DataReader:
    def __init__(self, path: str):
        self.file = open(path, "r")
        self._read_values()

    def _read_values(self):
        self.values = []
        for line in self.file.readlines():
            series = [float(x) for x in line.split()]
            self.values.append(series)

    def get_values(self):
        return self.values

    def get_means(self):
        means = []
        for series in self.values:
            means.append(sum(series) / len(series))
        return means

if __name__ == "__main__":
    reader = DataReader("data.txt")
    print(reader.get_values())
