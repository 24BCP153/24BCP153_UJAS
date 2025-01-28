n = int(input("Enter value of n: "))

fect_n = 1
for i in range(1, n + 1):
    fect_n *= i
if n < 0:
    print("Factorial is not defined for negative numbers.")
else:
    print(f"The factorial of {n} is {fect_n}")
