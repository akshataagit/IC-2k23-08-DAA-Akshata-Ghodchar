
# Experiment 6: Single-Source Shortest Path Using Dijkstra's Algorithm

## Problem Statement
Write a Python program to find the shortest distance
from a given source vertex to all other vertices in
a weighted graph using Dijkstra's algorithm.

## Algorithm / Approach
1. Read the number of vertices and edges.
2. Create an adjacency list to represent the graph.
3. Read the weighted directed edges.
4. Initialize all distances to infinity.
5. Set the source vertex distance to zero.
6. Insert the source vertex into a priority queue.
7. Extract the vertex having the minimum distance.
8. Update the distances of its adjacent vertices.
9. Repeat until the priority queue becomes empty.
10. Display the shortest distances.

## Pseudocode
START
1. Read graph and source vertex
2. Initialize dist[] = INFINITY
3. Set dist[source] = 0
4. Insert (0, source) into priority queue
5. While priority queue is not empty:
      Extract minimum distance vertex u
      For each adjacent vertex v:
          newDistance = dist[u] + weight(u,v)
          If newDistance < dist[v]:
              Update dist[v]
              Insert updated value into queue
6. Print shortest distances
STOP

## Sample Input
Enter number of vertices: 5
Enter number of edges: 6

Enter edges (u v weight):
0 1 4
0 2 1
2 1 2
1 3 1
2 3 5
3 4 3

Enter source vertex: 0

## Sample Output
Shortest distances from source 0
Vertex 0: 0
Vertex 1: 3
Vertex 2: 1
Vertex 3: 4
Vertex 4: 7

## Time Complexity
O((V + E) log V), using an adjacency list
and a binary heap priority queue.

## Space Complexity
O(V + E), for graph, distance array and priority queue.
