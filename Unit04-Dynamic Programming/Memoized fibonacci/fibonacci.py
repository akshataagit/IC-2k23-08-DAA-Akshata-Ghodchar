
def fibonacci(n, memo):
    if n <= 1:
        return n

    if n in memo:
        return memo[n]

    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)

    return memo[n]


n = int(input("Enter the number of terms: "))

if n <= 0:
    print("Please enter a positive number.")
else:
    memo = {}

    print("Fibonacci Series:")
    for i in range(n):
        print(fibonacci(i, memo), end=" ")
