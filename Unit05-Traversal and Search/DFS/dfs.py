# Depth First Search (DFS)
# Recursive and Iterative Implementation


class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_list = {i: [] for i in range(vertices)}

    # Add edge to graph
    def add_edge(self, u, v):
        if 0 <= u < self.vertices and 0 <= v < self.vertices:
            self.adj_list[u].append(v)
            self.adj_list[v].append(u)
        else:
            print("Invalid edge!")

    # Recursive DFS
    def recursive_dfs_util(self, vertex, visited):
        visited[vertex] = True
        print(vertex, end=" ")

        for neighbor in self.adj_list[vertex]:
            if not visited[neighbor]:
                self.recursive_dfs_util(neighbor, visited)

    def recursive_dfs(self, start):
        if start < 0 or start >= self.vertices:
            print("Invalid starting vertex!")
            return

        visited = [False] * self.vertices

        print("Recursive DFS Traversal:", end=" ")
        self.recursive_dfs_util(start, visited)
        print()

    # Iterative DFS
    def iterative_dfs(self, start):
        if start < 0 or start >= self.vertices:
            print("Invalid starting vertex!")
            return

        visited = [False] * self.vertices
        stack = [start]

        print("Iterative DFS Traversal:", end=" ")

        while stack:
            vertex = stack.pop()

            if not visited[vertex]:
                visited[vertex] = True
                print(vertex, end=" ")

                # Reverse insertion preserves recursive-style
                # left-to-right traversal for this adjacency order.
                for neighbor in reversed(self.adj_list[vertex]):
                    if not visited[neighbor]:
                        stack.append(neighbor)

        print()


# Main Program
print("DEPTH FIRST SEARCH")

vertices = int(input("Enter number of vertices: "))
edges = int(input("Enter number of edges: "))

graph = Graph(vertices)

for i in range(edges):
    print(f"Enter edge {i + 1}:")
    u = int(input("Enter starting vertex: "))
    v = int(input("Enter ending vertex: "))
    graph.add_edge(u, v)

start = int(input("Enter starting vertex for DFS: "))

while True:
    print("\n----- DFS MENU -----")
    print("1. Recursive DFS")
    print("2. Iterative DFS")
    print("3. Display Both")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        graph.recursive_dfs(start)

    elif choice == 2:
        graph.iterative_dfs(start)

    elif choice == 3:
        graph.recursive_dfs(start)
        graph.iterative_dfs(start)

    elif choice == 4:
        print("Program terminated.")
        break

    else:
        print("Invalid choice!")