
# Experiment 3: 0/1 Knapsack Using Dynamic Programming

## Problem Statement
Write a Python program to solve the 0/1 Knapsack problem
using Dynamic Programming.

Each item has a weight and a value. Select items such
that the total weight does not exceed the capacity and
the total value is maximized.

Each item can either be selected completely or rejected.

## Algorithm / Approach
1. Read the number of items.
2. Read the weight and value of each item.
3. Read the maximum capacity of the knapsack.
4. Create a DP table of size (n+1) x (capacity+1).
5. Initialize the first row and column with zero.
6. For each item:
   - If its weight is less than or equal to the
     current capacity, choose the maximum of:
       a. Including the item.
       b. Excluding the item.
   - Otherwise, exclude the item.
7. Return the final DP table value.

## Pseudocode
START
1. Read n, weights, values, capacity
2. Create dp[n+1][capacity+1]
3. Initialize all entries to 0
4. For i = 1 to n:
      For w = 0 to capacity:
          If weights[i-1] <= w:
              dp[i][w] = max(
                values[i-1] + dp[i-1][w-weights[i-1]],
                dp[i-1][w]
              )
          Else:
              dp[i][w] = dp[i-1][w]
5. Print dp[n][capacity]
STOP

## Sample Input
Enter number of items: 3
Enter weights: 10 20 30
Enter values: 60 100 120
Enter knapsack capacity: 50

## Sample Output
Maximum profit: 220

## Time Complexity
O(n * W), where n is the number of items
and W is the knapsack capacity.

## Space Complexity
O(n * W), for the DP table.
