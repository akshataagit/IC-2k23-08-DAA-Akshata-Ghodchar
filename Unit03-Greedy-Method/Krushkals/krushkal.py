
def find(parent, i):

    if parent[i] != i:
        parent[i] = find(parent, parent[i])

    return parent[i]


def union(parent, rank, x, y):

    root_x = find(parent, x)
    root_y = find(parent, y)

    if root_x == root_y:
        return

    if rank[root_x] < rank[root_y]:
        parent[root_x] = root_y

    elif rank[root_x] > rank[root_y]:
        parent[root_y] = root_x

    else:
        parent[root_y] = root_x
        rank[root_x] += 1


def kruskal_mst(edges, vertices):

    # Sort edges according to weight
    edges.sort(key=lambda x: x[2])

    parent = [i for i in range(vertices)]
    rank = [0] * vertices

    total_cost = 0
    edge_count = 0

    print("\nEdges in Minimum Spanning Tree:")

    for src, dest, weight in edges:

        x = find(parent, src)
        y = find(parent, dest)

        # Include edge if it does not form a cycle
        if x != y:

            print(src, "-", dest, ":", weight)

            total_cost += weight

            union(parent, rank, x, y)

            edge_count += 1

            if edge_count == vertices - 1:
                break

    if edge_count != vertices - 1:
        print("Graph is disconnected!")
    else:
        print("Minimum Cost =", total_cost)


# Main program
vertices = int(input("Enter number of vertices: "))
e = int(input("Enter number of edges: "))

edges = []

print("Enter source, destination and weight:")

for i in range(e):

    src, dest, weight = map(int, input().split())

    edges.append((src, dest, weight))

kruskal_mst(edges, vertices)
