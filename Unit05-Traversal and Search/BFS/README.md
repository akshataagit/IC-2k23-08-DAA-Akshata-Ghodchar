# Breadth First Search (BFS)

## 1. Problem Statement

To implement the Breadth First Search (BFS) graph traversal algorithm using Python. BFS is a graph traversal technique that visits all adjacent vertices of a node before moving to the next level. It uses a Queue data structure to maintain the order of traversal.

## 2. Objectives

- To understand the concept of graph traversal.
- To implement Breadth First Search using Python.
- To understand the working of Queue (FIFO).
- To represent a graph using an adjacency list.
- To traverse a graph starting from a given vertex.
- To understand the applications of BFS.

## 3. Algorithm / Approach

1. Start the program.
2. Create a graph using an adjacency list.
3. Accept the number of vertices and edges from the user.
4. Insert edges into the graph.
5. Accept the starting vertex.
6. Create a visited array and initialize all vertices as unvisited.
7. Create an empty queue.
8. Mark the starting vertex as visited and insert it into the queue.
9. Repeat until the queue becomes empty:
   - Remove the front vertex from the queue.
   - Display the vertex.
   - Visit all adjacent vertices.
   - If an adjacent vertex is not visited, mark it as visited and insert it into the queue.
10. Stop.

## 4. Pseudocode

```text
BFS(graph, start)

    Create visited array
    Create empty queue

    Mark start as visited
    Enqueue start

    While queue is not empty

        vertex = Dequeue()
        Print vertex

        For each neighbor of vertex

            If neighbor is not visited

                Mark neighbor as visited
                Enqueue neighbor

    End
```

## 5. Sample Input

```text
Number of vertices: 5
Number of edges: 5

Edges:
0 1
0 2
1 3
1 4
2 4

Starting vertex: 0
```

## 6. Sample Output

```text
BREADTH FIRST SEARCH

BFS Traversal: 0 1 2 3 4
```

## 7. Time and Space Complexity

Let V represent the number of vertices and E represent the number of edges.

- Time Complexity: O(V + E)
- Auxiliary Space Complexity: O(V)
- Graph Storage Complexity: O(V + E)

## 8. Applications

- Finding the shortest path in an unweighted graph.
- Social networking applications.
- Web crawling.
- Network broadcasting.
- Finding connected components.
- Level-order traversal of trees.
- GPS and navigation systems.

## 9. Conclusion

In this experiment, the Breadth First Search algorithm was successfully implemented using Python. The graph was represented using an adjacency list, and a Queue data structure was used to visit vertices level by level.

BFS is an important graph traversal algorithm used in shortest-path problems, network communication, and searching applications.