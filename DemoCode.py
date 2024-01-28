def fibonacci_series(n):
    fib_series = []
    a, b = 0, 1

    for _ in range(n):
        fib_series.append(a)
        a, b = b, a + b

    return fib_series


n = 10
result = fibonacci_series(n)

print(f"Fibonacci Series of length {n}: {result}")
