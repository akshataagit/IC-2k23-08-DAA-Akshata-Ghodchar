# Graph Representation using Adjacency List

class Graph:
    def __init__(self, vertices, directed=False):
        self.vertices = vertices
        self.directed = directed

        # Initialize adjacency list
        self.adj_list = {i: [] for i in range(vertices)}

    # Add edge between two vertices
    def add_edge(self, u, v):
        if 0 <= u < self.vertices and 0 <= v < self.vertices:
            self.adj_list[u].append(v)

            if not self.directed:
                self.adj_list[v].append(u)
        else:
            print("Invalid vertex!")

    # Display adjacency list
    def display(self):
        print("\nAdjacency List:")

        for vertex in self.adj_list:
            print(vertex, "->", self.adj_list[vertex])


# Main Program
print("GRAPH USING ADJACENCY LIST")

vertices = int(input("Enter number of vertices: "))

choice = int(input("Enter 1 for Directed Graph, 0 for Undirected Graph: "))

graph = Graph(vertices, choice == 1)

edges = int(input("Enter number of edges: "))

for i in range(edges):
    print(f"\nEnter edge {i + 1}:")
    u = int(input("Enter starting vertex: "))
    v = int(input("Enter ending vertex: "))

    graph.add_edge(u, v)

graph.display()