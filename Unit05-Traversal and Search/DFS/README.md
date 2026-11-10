# Depth First Search (DFS) – Recursive and Iterative

## 1. Problem Statement

To implement the Depth First Search (DFS) graph traversal algorithm using Python through both recursive and iterative approaches.

DFS is a graph traversal technique that explores a graph by visiting a vertex and then exploring its adjacent vertices as deeply as possible before backtracking.

The recursive approach uses function calls, whereas the iterative approach uses an explicit Stack data structure.

## 2. Objectives

- To understand the concept of Depth First Search.
- To implement Recursive DFS using Python.
- To implement Iterative DFS using a Stack.
- To understand recursion and backtracking.
- To represent a graph using an adjacency list.
- To compare recursive and iterative DFS approaches.

## 3. Algorithm / Approach

### A. Recursive DFS

1. Start the program.
2. Create a graph using an adjacency list.
3. Accept the number of vertices and edges.
4. Select a starting vertex.
5. Initialize all vertices as unvisited.
6. Mark the starting vertex as visited.
7. Display the current vertex.
8. Visit each unvisited adjacent vertex recursively.
9. Continue until no unvisited adjacent vertices remain.
10. Backtrack and stop.

### B. Iterative DFS

1. Start the program.
2. Create a graph using an adjacency list.
3. Initialize all vertices as unvisited.
4. Create an empty stack.
5. Push the starting vertex into the stack.
6. Repeat until the stack becomes empty:
   - Pop the top vertex.
   - If it is not visited, mark it as visited.
   - Display the vertex.
   - Push its unvisited adjacent vertices onto the stack in reverse order.
7. Stop.

## 4. Pseudocode

### A. Recursive DFS

```text
DFS_RECURSIVE(vertex)

    Mark vertex as visited
    Print vertex

    For each neighbor of vertex

        If neighbor is not visited

            DFS_RECURSIVE(neighbor)

    End
```

### B. Iterative DFS

```text
DFS_ITERATIVE(start)

    Create visited array
    Create empty stack

    Push start into stack

    While stack is not empty

        vertex = Pop()

        If vertex is not visited

            Mark vertex as visited
            Print vertex

            For each neighbor in reverse order

                If neighbor is not visited

                    Push neighbor into stack

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

### Recursive DFS

```text
Recursive DFS Traversal: 0 1 3 4 2
```

### Iterative DFS

```text
Iterative DFS Traversal: 0 1 3 4 2
```

## 7. Time and Space Complexity

Let V represent the number of vertices and E represent the number of edges.

| Operation | Time Complexity | Auxiliary Space |
|---|---|---|
| Recursive DFS | O(V + E) | O(V) |
| Iterative DFS | O(V + E) | O(V) |

Graph storage using an adjacency list requires O(V + E) space.

## 8. Applications

- Detecting cycles in graphs.
- Topological sorting.
- Maze solving.
- Pathfinding.
- Finding connected components.
- Backtracking problems.
- Strongly connected components.
- Dependency analysis.

## 9. Conclusion

In this experiment, the Depth First Search algorithm was successfully implemented using Python through recursive and iterative approaches.

Recursive DFS uses function calls to explore vertices, while iterative DFS uses an explicit stack. Both methods perform depth-first graph traversal and are useful in graph searching, cycle detection, pathfinding, and backtracking problems.