class Matrix:
    def __init__(self, data):
        self.data = data  

    def display(self):
        for row in self.data:
            print(row)

    def add(self, other):
        result = []
        for i in range(3):
            row = []
            for j in range(3):
                row.append(self.data[i][j] + other.data[i][j])
            result.append(row)
        return Matrix(result)

    def multiply(self, other):
        result = []
        for i in range(3):
            row = []
            for j in range(3):
                value = 0
                for k in range(3):
                    value += self.data[i][k] * other.data[k][j]
                row.append(value)
            result.append(row)
        return Matrix(result)

    def transpose(self):
        result = []
        for i in range(3):
            row = []
            for j in range(3):
                row.append(self.data[j][i])
            result.append(row)
        return Matrix(result)


matrix1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix2 = Matrix([[9, 8, 7], [6, 5, 4], [3, 2, 1]])

print("Matrix 1:")
matrix1.display()

print("\nMatrix 2:")
matrix2.display()

print("\nAddition:")
matrix1.add(matrix2).display()

print("\nMultiplication:")
matrix1.multiply(matrix2).display()

print("\nTranspose of Matrix 1:")
matrix1.transpose().display()

#OUTPUT:
# Matrix 1:
# [1, 2, 3]
# [4, 5, 6]
# [7, 8, 9]

# Matrix 2:
# [9, 8, 7]
# [6, 5, 4]
# [3, 2, 1]

# Addition:
# [10, 10, 10]
# [10, 10, 10]
# [10, 10, 10]

# Multiplication:
# [30, 24, 18]
# [84, 69, 54]
# [138, 114, 90]

# Transpose of Matrix 1:
# [1, 4, 7]
# [2, 5, 8]
# [3, 6, 9]
