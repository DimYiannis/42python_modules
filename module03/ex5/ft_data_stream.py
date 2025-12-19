
def fib(n):
    a = 0
    b = 1
    for i in range(0, n):
        yield a
        tmp = a
        a = b
        b = tmp + b

def prime(n):
    for num in range(2, n):
        count = 0
        for i in range(1, num + 1):
            if num % i == 0:
                count += 1
        if count == 2:
            yield num

print("=== Game Data Stream Processor ===\n")

print("Processing 1000 game events...\n")

print("=== Stream Analytics ===\n")

print("=== Generator Demonstration ===\n")
fib_gen = fib(10)
prime_gen = prime(12)

print(f"Fibonacci sequence (first 10): ", end="")
for i in range(0, 10):
    if i == 9:
        print(f"{next(fib_gen)}")
    else:
        print(f"{next(fib_gen)}", end=", ")

print()

print(f"Prime numbers (first 5): ", end="")
for i in range(5):
    if i == 4:
         print(f"{next(prime_gen)}")
    else:
        print(f"{next(prime_gen)}", end=", ")
    
