# Experiment: Minimum Cost Spanning Tree Using Kruskal's Algorithm

## 1. Problem Statement

Given a connected, weighted and undirected graph, find the Minimum Spanning Tree with the minimum possible total edge weight.

The Minimum Spanning Tree must connect all vertices without forming any cycle and must contain exactly V-1 edges.

## 2. Algorithm / Approach

Kruskal's Algorithm is a Greedy algorithm used to find the Minimum Spanning Tree.

1. Sort all graph edges in ascending order of their weights.
2. Initialize each vertex as a separate set.
3. Select the edge with the minimum weight.
4. Check whether the selected edge forms a cycle.
5. If it does not form a cycle, include it in the MST.
6. Merge the sets of the two vertices using Union-Find.
7. Repeat until V-1 edges are selected.
8. Calculate and display the total minimum cost.

The algorithm uses the Disjoint Set Union (DSU) data structure with path compression and union by rank to efficiently detect cycles.

## 3. Pseudocode

```text
KruskalMST(graph):

    Sort all edges in ascending order of weight

    Initialize each vertex as a separate set

    totalCost = 0
    edgeCount = 0

    For each edge (u, v, weight):

        Find parent of u and v

        If parent[u] != parent[v]:

            Include edge in MST

            Union the two sets

            totalCost += weight

            edgeCount++

        If edgeCount == V-1:
            Break

    Display MST edges
    Display totalCost
```

## 4. Sample Input

```text
Enter number of vertices: 5
Enter number of edges: 7

Enter source, destination and weight:

0 1 2
0 3 6
1 2 3
1 3 8
1 4 5
2 4 7
3 4 9
```

## 5. Sample Output

```text
Edges in Minimum Spanning Tree:

0 - 1 : 2
1 - 2 : 3
1 - 4 : 5
0 - 3 : 6

Minimum Cost = 16
```

## 6. Time and Space Complexity

- Time Complexity: O(E log E), mainly because of sorting the edges.
- Space Complexity: O(V + E), for storing edges and the Disjoint Set data structures.

## 7. Conclusion

Kruskal's Algorithm finds the Minimum Spanning Tree by selecting edges in ascending order of weight while avoiding cycles. It uses the Union-Find data structure for efficient cycle detection and is particularly useful for sparse graphs.