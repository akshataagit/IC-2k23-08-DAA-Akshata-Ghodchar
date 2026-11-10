# Graph Representation Using Adjacency Matrix and Adjacency List

## 1. Problem Statement

To implement graph data structures using two different graph representation techniques: Adjacency Matrix and Adjacency List using Python.

The program accepts the number of vertices and edges from the user and constructs a graph. It supports both directed and undirected graphs and displays the graph using the selected representation.

## 2. Objectives

- To understand the basic concept of Graph Data Structures.
- To implement graph representation using an Adjacency Matrix.
- To implement graph representation using an Adjacency List.
- To understand directed and undirected graphs.
- To understand how vertices and edges are represented.
- To compare the memory requirements and performance of both representations.

## 3. Algorithm / Approach

### A. Graph Using Adjacency Matrix

1. Start the program.
2. Accept the number of vertices.
3. Initialize a two-dimensional matrix of size V × V with zeros.
4. Accept the number of edges.
5. For every edge, accept the starting vertex and ending vertex.
6. Set matrix[u][v] = 1.
7. If the graph is undirected, also set matrix[v][u] = 1.
8. Display the adjacency matrix.
9. Stop.

### B. Graph Using Adjacency List

1. Start the program.
2. Accept the number of vertices.
3. Create an empty list for every vertex.
4. Accept the number of edges.
5. For every edge, accept the starting vertex and ending vertex.
6. Add the ending vertex to the adjacency list of the starting vertex.
7. If the graph is undirected, also add the starting vertex to the adjacency list of the ending vertex.
8. Display the adjacency list.
9. Stop.

## 4. Pseudocode

### A. Adjacency Matrix

```text
CREATE_GRAPH(V)
    Create V x V matrix filled with 0

    For each edge (u, v)
        matrix[u][v] = 1

        If graph is undirected
            matrix[v][u] = 1

    Display matrix
```

### B. Adjacency List

```text
CREATE_GRAPH(V)
    Create an empty list for every vertex

    For each edge (u, v)
        Add v to adj_list[u]

        If graph is undirected
            Add u to adj_list[v]

    Display adjacency list
```

## 5. Sample Input

```text
Number of vertices: 4
Graph type: Undirected
Number of edges: 4

Edges:
0 1
0 2
1 2
2 3
```

## 6. Sample Output

### Adjacency Matrix

```text
  0 1 2 3
0 0 1 1 0
1 1 0 1 0
2 1 1 0 1
3 0 0 1 0
```

### Adjacency List

```text
0 -> [1, 2]
1 -> [0, 2]
2 -> [0, 1, 3]
3 -> [2]
```

## 7. Time and Space Complexity

Let:
- V = Number of vertices
- E = Number of edges

| Operation | Adjacency Matrix | Adjacency List |
|---|---|---|
| Space Complexity | O(V²) | O(V + E) |
| Add Edge | O(1) | O(1) average |
| Check Edge | O(1) | O(degree of vertex) |
| Display Graph | O(V²) | O(V + E) |

## 8. Difference Between Adjacency Matrix and Adjacency List

| Adjacency Matrix | Adjacency List |
|---|---|
| Uses a 2D array. | Uses lists or dictionaries. |
| Requires O(V²) space. | Requires O(V + E) space. |
| Suitable for dense graphs. | Suitable for sparse graphs. |
| Checking an edge takes O(1). | Checking an edge takes O(degree). |
| Uses more memory for sparse graphs. | Uses less memory for sparse graphs. |

## 9. Applications

- Computer networks.
- Social networking platforms.
- Google Maps and navigation systems.
- Web page link analysis.
- Artificial Intelligence.
- Network routing algorithms.
- Pathfinding and shortest-path problems.
- Dependency management in software systems.

## 10. Conclusion

In this experiment, graph data structures were successfully implemented using Python through Adjacency Matrix and Adjacency List representations.

The Adjacency Matrix represents connections between vertices using a two-dimensional array, whereas the Adjacency List represents connections using lists associated with each vertex.

Both representations support directed and undirected graphs. The experiment demonstrates the differences in memory usage, edge operations, and efficiency of graph representations.