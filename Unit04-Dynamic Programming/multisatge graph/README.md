
# Experiment 4: Multistage Graph Using Dynamic Programming

## Problem Statement
Write a Python program to find the minimum-cost path
in a multistage graph using Dynamic Programming.

A multistage graph is a directed weighted graph in
which vertices are divided into different stages.
Edges move from an earlier stage to a later stage.

## Algorithm / Approach
1. Read the number of vertices and their stage numbers.
2. Read the weighted directed edges.
3. Initialize the cost of the destination vertex to zero.
4. Initialize all other costs to infinity.
5. Process vertices in reverse stage order.
6. For each vertex, calculate the minimum cost of
   reaching the destination through its outgoing edges.
7. Store the next vertex in the path array.
8. Reconstruct and display the minimum-cost path.

## Pseudocode
START
1. Read vertices, stages and edges
2. Initialize cost[v] = INFINITY
3. Set cost[destination] = 0
4. For each stage in reverse order:
      For each vertex u in that stage:
          For each edge (u, v):
              cost[u] = min(cost[u], weight(u,v)+cost[v])
              Store the next vertex
5. Reconstruct the path
6. Print minimum cost and path
STOP

## Sample Input
Enter number of vertices: 6
Enter stage number of each vertex: 1 2 2 3 3 4
Enter number of edges: 8
Enter edge (u v weight): 0 1 2
Enter edge (u v weight): 0 2 1
Enter edge (u v weight): 1 3 2
Enter edge (u v weight): 1 4 3
Enter edge (u v weight): 2 3 6
Enter edge (u v weight): 2 4 7
Enter edge (u v weight): 3 5 3
Enter edge (u v weight): 4 5 1
Enter source vertex: 0
Enter destination vertex: 5

## Sample Output
Minimum cost: 7
Shortest path: 0 -> 1 -> 3 -> 5

## Time Complexity
O(V + E), where V is the number of vertices
and E is the number of edges.

## Space Complexity
O(V + E), for the graph, cost and path arrays.
