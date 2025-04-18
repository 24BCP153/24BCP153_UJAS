class Matrix:
    def __init__(self, data):
        self.data = data

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
                total = 0
                for k in range(3):
                    total += self.data[i][k] * other.data[k][j]
                row.append(total)
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

    def display(self):
        for row in self.data:
            print(row)


m1 = Matrix([[1,2,3],[4,5,6],[7,8,9]])
m2 = Matrix([[9,8,7],[6,5,4],[3,2,1]])

print("Addition:")
m1.add(m2).display()
print("Multiplication:")
m1.multiply(m2).display()
print("Transpose of Matrix 1:")
m1.transpose().display()
