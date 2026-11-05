
def prim_mst(graph, n):

    key = [float('inf')] * n
    parent = [-1] * n
    mst_set = [False] * n

    # Start from vertex 0
    key[0] = 0

    total_cost = 0

    for count in range(n):

        # Find vertex with minimum key value
        u = -1

        for v in range(n):
            if not mst_set[v] and (
                u == -1 or key[v] < key[u]
            ):
                u = v

        if u == -1 or key[u] == float('inf'):
            print("Graph is disconnected!")
            return

        mst_set[u] = True
        total_cost += key[u]

        # Update adjacent vertices
        for v in range(n):

            if (graph[u][v] != 0 and
                not mst_set[v] and
                graph[u][v] < key[v]):

                key[v] = graph[u][v]
                parent[v] = u

    print("\nEdges in Minimum Spanning Tree:")

    for i in range(1, n):
        print(parent[i], "-", i, ":", graph[i][parent[i]])

    print("Minimum Cost =", total_cost)


# Main program
n = int(input("Enter number of vertices: "))

graph = []

print("Enter adjacency matrix:")

for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)

prim_mst(graph, n)
