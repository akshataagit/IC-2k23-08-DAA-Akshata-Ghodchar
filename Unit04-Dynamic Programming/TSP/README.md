
# Experiment 7: Traveling Salesperson Problem Using Dynamic Programming

## Problem Statement
Write a Python program to solve the Traveling Salesperson
Problem (TSP) using Dynamic Programming.

The objective is to find the minimum-cost tour in which
a salesperson visits every city exactly once and returns
to the starting city.

## Algorithm / Approach
1. Read the number of cities.
2. Read the cost matrix representing travel costs.
3. Start the tour from city 0.
4. Use bitmasking to represent visited cities.
5. Define a recursive DP function solve(mask, pos).
6. If all cities are visited, return the cost of returning
   to the starting city.
7. Otherwise, consider every unvisited city.
8. Calculate the cost of visiting that city and solving
   the remaining problem.
9. Store the minimum result using memoization.
10. Reconstruct and display the optimal tour.

## Pseudocode
START
1. Read number of cities n
2. Read cost matrix
3. Initialize memoization using DP
4. Define solve(mask, pos)

5. If all cities are visited:
      Return cost[pos][0]

6. Set minimum cost = INFINITY

7. For each unvisited city:
      newMask = mask OR (1 << city)
      cost = graph[pos][city] +
             solve(newMask, city)
      Update minimum cost

8. Return minimum cost
9. Reconstruct the optimal path
10. Print minimum cost and tour
STOP

## Sample Input
Enter number of cities: 4

Enter cost matrix (-1 for no direct route):
0 10 15 20
10 0 35 25
15 35 0 30
20 25 30 0

## Sample Output
Minimum travel cost: 80
Optimal tour: 0 -> 1 -> 3 -> 2 -> 0

## Time Complexity
O(n^2 * 2^n), where n is the number of cities.

## Space Complexity
O(n * 2^n), for the DP memoization table.
