
def multistage_graph(n, stages, graph, source, destination):
    INF = float('inf')

    cost = [INF] * n
    path = [-1] * n

    cost[destination] = 0

    # Process vertices from the last stage to the first
    for stage in range(max(stages) - 1, min(stages) - 1, -1):
        for u in range(n):
            if stages[u] != stage:
                continue

            for v, weight in graph[u]:
                if stages[v] > stages[u]:
                    if weight + cost[v] < cost[u]:
                        cost[u] = weight + cost[v]
                        path[u] = v

    if cost[source] == INF:
        return None, []

    # Reconstruct shortest path
    result_path = []
    current = source

    while current != -1:
        result_path.append(current)
        if current == destination:
            break
        current = path[current]

    return cost[source], result_path


n = int(input("Enter number of vertices: "))

stages = list(map(int, input(
    "Enter stage number of each vertex: ").split()))

if n <= 0 or len(stages) != n:
    print("Invalid input.")
else:
    graph = [[] for _ in range(n)]

    m = int(input("Enter number of edges: "))

    for _ in range(m):
        u, v, w = map(int, input(
            "Enter edge (u v weight): ").split())

        if not (0 <= u < n and 0 <= v < n) or w < 0:
            print("Invalid edge.")
            break

        graph[u].append((v, w))
    else:
        source = int(input("Enter source vertex: "))
        destination = int(input("Enter destination vertex: "))

        if not (0 <= source < n and 0 <= destination < n):
            print("Invalid source or destination.")
        elif stages[source] >= stages[destination]:
            print("Source must belong to an earlier stage.")
        else:
            cost, path = multistage_graph(
                n, stages, graph, source, destination
            )

            if cost is None:
                print("No path exists.")
            else:
                print("Minimum cost:", cost)
                print("Shortest path:", " -> ".join(map(str, path)))
