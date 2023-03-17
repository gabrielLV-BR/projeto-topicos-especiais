class DataReader:
    def __init__(self, path: str):
        self.file = open(path, "r")
        self.values = [float(x) for x in self.file.readline().split()]

    def get_values(self):
        return self.values

if __name__ == "__main__":
    reader = DataReader("data.txt")
    print(reader.get_values())
