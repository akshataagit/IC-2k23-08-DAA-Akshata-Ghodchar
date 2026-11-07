
import heapq


def dijkstra(graph, n, source):
    dist = [float('inf')] * n
    dist[source] = 0

    pq = [(0, source)]

    while pq:
        current_dist, u = heapq.heappop(pq)

        if current_dist > dist[u]:
            continue

        for v, weight in graph[u]:
            new_dist = current_dist + weight

            if new_dist < dist[v]:
                dist[v] = new_dist
                heapq.heappush(pq, (new_dist, v))

    return dist


n = int(input("Enter number of vertices: "))
m = int(input("Enter number of edges: "))

if n <= 0 or m < 0:
    print("Invalid graph size.")
else:
    graph = [[] for _ in range(n)]
    valid = True

    print("Enter edges (u v weight):")

    for _ in range(m):
        u, v, w = map(int, input().split())

        if not (0 <= u < n and 0 <= v < n) or w < 0:
            print("Invalid edge or negative weight.")
            valid = False
            break

        graph[u].append((v, w))

    if valid:
        source = int(input("Enter source vertex: "))

        if not 0 <= source < n:
            print("Invalid source vertex.")
        else:
            distances = dijkstra(graph, n, source)

            print("Shortest distances from source", source)

            for i in range(n):
                if distances[i] == float('inf'):
                    print(f"Vertex {i}: Unreachable")
                else:
                    print(f"Vertex {i}: {distances[i]}")
