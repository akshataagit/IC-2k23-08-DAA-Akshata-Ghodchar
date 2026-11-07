
def floyd_warshall(graph, n):
    dist = [row[:] for row in graph]

    for k in range(n):
        for i in range(n):
            for j in range(n):

                if dist[i][k] != float('inf') and \
                   dist[k][j] != float('inf'):

                    dist[i][j] = min(
                        dist[i][j],
                        dist[i][k] + dist[k][j]
                    )

    return dist


n = int(input("Enter number of vertices: "))

if n <= 0:
    print("Number of vertices must be positive.")
else:
    print("Enter adjacency matrix (-1 for no edge):")

    graph = []

    for i in range(n):
        row = list(map(int, input().split()))

        if len(row) != n:
            print("Invalid matrix.")
            break

        graph.append([
            float('inf') if x == -1 else x
            for x in row
        ])
    else:
        dist = floyd_warshall(graph, n)

        print("\nShortest Distance Matrix:")

        for row in dist:
            print(" ".join(
                "INF" if x == float('inf') else str(x)
                for x in row
            ))

        if any(dist[i][i] < 0 for i in range(n)):
            print("Negative weight cycle detected.")
