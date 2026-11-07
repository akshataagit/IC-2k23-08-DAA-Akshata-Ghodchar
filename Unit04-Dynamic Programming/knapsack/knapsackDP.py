
def knapsack(weights, values, capacity):
    n = len(weights)

    dp = [[0 for _ in range(capacity + 1)]
          for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):

            if weights[i - 1] <= w:
                dp[i][w] = max(
                    values[i - 1] + dp[i - 1][w - weights[i - 1]],
                    dp[i - 1][w]
                )
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]


n = int(input("Enter number of items: "))

weights = list(map(int, input("Enter weights: ").split()))
values = list(map(int, input("Enter values: ").split()))

capacity = int(input("Enter knapsack capacity: "))

if n <= 0 or len(weights) != n or len(values) != n:
    print("Invalid input.")
elif capacity < 0 or any(w <= 0 for w in weights):
    print("Invalid weights or capacity.")
else:
    result = knapsack(weights, values, capacity)
    print("Maximum profit:", result)
