
# Experiment 2: Fibonacci Using Memoization

## Problem Statement
Write a Python program to generate the Fibonacci series
using the memoization technique of Dynamic Programming.

## Algorithm / Approach
1. Define a recursive function fibonacci(n, memo).
2. If n is 0 or 1, return n.
3. Check whether the result is already stored in memo.
4. If available, return the stored result.
5. Otherwise, calculate fibonacci(n-1) + fibonacci(n-2).
6. Store the calculated result in memo.
7. Print the Fibonacci series.

## Pseudocode
START
1. Read n
2. Initialize an empty memo dictionary
3. Define fibonacci(n, memo)
4. If n <= 1, return n
5. If n exists in memo:
      Return memo[n]
6. Calculate:
      memo[n] = fibonacci(n-1) + fibonacci(n-2)
7. Return memo[n]
8. Print Fibonacci terms
STOP

## Sample Input
Enter the number of terms: 7

## Sample Output
Fibonacci Series:
0 1 1 2 3 5 8

## Time Complexity
O(n) - Each Fibonacci value is calculated once.

## Space Complexity
O(n) - Memoization storage and recursion stack.
