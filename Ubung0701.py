class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix
    def __str__(self):
        return str('\n'.join([' '.join([str(i) for i in j]) for j in self.matrix]))
    def __add__(self, mat):
        k = []
        for i in range(len(self.matrix)):
            k.append([])
            for j in range(len(self.matrix)):
                k[i].append(self.matrix[i][j] + mat.matrix[i][j])
        return str('\n'.join([' '.join([str(i) for i in j]) for j in k]))
matrix_1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix_2 = Matrix([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
print(matrix_1, '\n')
print(matrix_2, '\n')
print(matrix_1 + matrix_2)