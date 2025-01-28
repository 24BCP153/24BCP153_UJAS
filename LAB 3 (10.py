
n = int(input("Enter the number of terms (N): "))


if n <= 0:
    print("Please enter a positive integer.")
elif n == 1:
    print("Fibonacci Series: 0")
else:
    print("Fibonacci Series:", end=" ")
    a, b = 0, 1
    print(a, b, end=" ")
    for _ in range(2, n):
        print(a + b, end=" ")
        b, a = a + b, b
