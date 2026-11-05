# Experiment: Minimum Cost Spanning Tree Using Prim's Algorithm

## 1. Problem Statement

Given a connected, weighted and undirected graph, find a Minimum Spanning Tree (MST) with minimum total edge weight.

A Minimum Spanning Tree connects all vertices of a graph without forming any cycle and contains exactly V-1 edges, where V represents the number of vertices.

## 2. Algorithm / Approach

Prim's Algorithm is a Greedy algorithm used to find the Minimum Spanning Tree.

1. Start with any vertex, usually vertex 0.
2. Initialize the key value of all vertices to infinity.
3. Set the key value of the starting vertex to zero.
4. Select the vertex with the minimum key value that is not yet included in MST.
5. Include the selected vertex in MST.
6. Update the key values of its adjacent vertices if a smaller edge weight is found.
7. Repeat until all vertices are included.
8. Display the MST edges and their total cost.

## 3. Pseudocode

```text
PrimMST(graph):

    Initialize key[] = infinity
    Initialize mstSet[] = false

    key[0] = 0

    Repeat V times:

        Select vertex u with minimum key
        that is not included in MST

        Add u to MST

        For each adjacent vertex v:

            If v is not in MST and
               weight(u, v) < key[v]:

                parent[v] = u
                key[v] = weight(u, v)

    Display MST edges
    Calculate total cost
```

## 4. Sample Input

```text
Enter number of vertices: 5

Enter adjacency matrix:

0 2 0 6 0
2 0 3 8 5
0 3 0 0 7
6 8 0 0 9
0 5 7 9 0
```

## 5. Sample Output

```text
Edges in Minimum Spanning Tree:

0 - 1 : 2
1 - 2 : 3
0 - 3 : 6
1 - 4 : 5

Minimum Cost = 16
```

## 6. Time and Space Complexity

- Time Complexity: O(V²), using an adjacency matrix.
- Space Complexity: O(V²), for storing the adjacency matrix.

## 7. Conclusion

Prim's Algorithm constructs a Minimum Spanning Tree by repeatedly selecting the minimum-weight edge that connects an already included vertex to a vertex outside the MST. It produces an optimal minimum-cost spanning tree for a connected, weighted and undirected graph.