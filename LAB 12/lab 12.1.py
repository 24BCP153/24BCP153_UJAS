class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def add(self, other):
        return ComplexNumber(self.real + other.real, self.imag + other.imag)

    def subtract(self, other):
        return ComplexNumber(self.real - other.real, self.imag - other.imag)

    def display(self):
        print(f"{self.real} + {self.imag}i")


c1 = ComplexNumber(3, 2)
c2 = ComplexNumber(1, 7)
result_add = c1.add(c2)
result_sub = c1.subtract(c2)

print("Addition Result:", end=" ")
result_add.display()
print("Subtraction Result:", end=" ")
result_sub.display()
