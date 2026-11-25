import time

def iterative_factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

def recursive_factorial(n):
    if n <= 1:
        return 1
    return n * recursive_factorial(n - 1)

n = int(input("Enter a number: "))

start = time.time()
result1 = iterative_factorial(n)
end = time.time()
print("Iterative Factorial =", result1)
print("Iterative Time =", end - start)

start = time.time()
result2 = recursive_factorial(n)
end = time.time()
print("Recursive Factorial =", result2)
print("Recursive Time =", end - start)
