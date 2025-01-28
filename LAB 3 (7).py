n = int(input("Enter value of n: "))
r = int(input("Enter value of r: "))

fect_n = 1
for i in range(1, n + 1):
    fect_n *= i
print(f"The factorial of {n} is {fect_n}")

fect_r = 1
for i in range(1, r + 1):
    fect_r *= i
print(f"The factorial of {r} is {fect_r}")

result = 1
for i in range(1, n - r + 1):
    result *= i
print(f"The factorial of {result} is {result}")    
    
nCr = fect_n / (fect_r * result
nPr = fect_n / result
print(nCr)
print(nPr)
