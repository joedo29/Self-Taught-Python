# Find factorial of a number
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return (n * factorial(n - 1))

n1 = float(input("Enter a number: "))
x1 = factorial(n1)
n2 = float(input("Enter a number: "))
x2 = factorial(n2)
n3 = float(input("Enter a number: "))
x3 = factorial(n3)
print(x1/x2/x3)
