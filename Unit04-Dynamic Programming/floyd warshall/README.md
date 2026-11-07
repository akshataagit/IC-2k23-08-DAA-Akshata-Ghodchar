
# Experiment 5: All-Pairs Shortest Path Using Floyd-Warshall

## Problem Statement
Write a Python program to find the shortest paths
between all pairs of vertices in a weighted graph
using the Floyd-Warshall algorithm.

## Algorithm / Approach
1. Read the number of vertices.
2. Read the adjacency matrix.
3. Represent missing edges using infinity.
4. Initialize the distance matrix using the adjacency matrix.
5. Consider every vertex as an intermediate vertex.
6. Update the shortest distance between every pair
   of vertices using the intermediate vertex.
7. Display the final shortest distance matrix.

## Pseudocode
START
1. Read n and adjacency matrix
2. Initialize dist = graph
3. For k = 0 to n-1:
      For i = 0 to n-1:
          For j = 0 to n-1:
              dist[i][j] = min(
                  dist[i][j],
                  dist[i][k] + dist[k][j]
              )
4. Print shortest distance matrix
STOP

## Sample Input
Enter number of vertices: 4

Enter adjacency matrix (-1 for no edge):
0 5 -1 10
-1 0 3 -1
-1 -1 0 1
-1 -1 -1 0

## Sample Output
Shortest Distance Matrix:
0 5 8 9
INF 0 3 4
INF INF 0 1
INF INF INF 0

## Time Complexity
O(V^3), because three nested loops are used.

## Space Complexity
O(V^2), for storing the distance matrix.
