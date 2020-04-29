class Matrix:
    def __init__(self, matrix_string):
        self.matrix_string = matrix_string.split("\n")

    def row(self, index):
        rows = self.matrix_string[index-1].split(" ")
        return list(map(int, rows))

    def column(self, index):
        return [self.row(i+1)[index-1] for i in range(len(self.matrix_string))]
