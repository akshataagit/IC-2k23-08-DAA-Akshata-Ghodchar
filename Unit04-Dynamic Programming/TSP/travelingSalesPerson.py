
from functools import lru_cache


def tsp(graph, n):
    ALL_VISITED = (1 << n) - 1

    @lru_cache(None)
    def solve(mask, pos):
        # All cities visited: return to starting city
        if mask == ALL_VISITED:
            return graph[pos][0]

        ans = float('inf')

        for city in range(n):
            if not (mask & (1 << city)):
                if graph[pos][city] != float('inf'):
                    new_cost = (
                        graph[pos][city] +
                        solve(mask | (1 << city), city)
                    )
                    ans = min(ans, new_cost)

        return ans

    minimum_cost = solve(1, 0)

    if minimum_cost == float('inf'):
        return None, []

    # Reconstruct the optimal tour
    path = [0]
    mask = 1
    pos = 0

    while mask != ALL_VISITED:
        for city in range(n):
            if not (mask & (1 << city)):
                if graph[pos][city] == float('inf'):
                    continue

                new_mask = mask | (1 << city)

                if (graph[pos][city] + solve(new_mask, city)
                        == solve(mask, pos)):
                    path.append(city)
                    mask = new_mask
                    pos = city
                    break

    path.append(0)

    return minimum_cost, path


n = int(input("Enter number of cities: "))

if n <= 0:
    print("Number of cities must be positive.")
else:
    print("Enter cost matrix (-1 for no direct route):")

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
        if any(graph[i][i] != 0 for i in range(n)):
            print("Diagonal entries must be zero.")
        else:
            cost, path = tsp(graph, n)

            if cost is None:
                print("No complete tour exists.")
            else:
                print("Minimum travel cost:", cost)
                print("Optimal tour:", " -> ".join(map(str, path)))
