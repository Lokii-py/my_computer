class Memory:
    def __init__(self, size=256):
        self.data: list = [0] * size

    def __getitem__(self, index):
        return self.data[index]

    def __setitem__(self, index, value):
        self.data[index] = value