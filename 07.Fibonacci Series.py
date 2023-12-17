def fibonacci_series(n):
    series = [0, 1]

    for i in range(2, n):
        series.append(series[i-1] + series[i-2])

    return series

number = int(input("Enter the number of terms: "))
fib_series = fibonacci_series(number)
print("Fibonacci Series:")
print(fib_series)
