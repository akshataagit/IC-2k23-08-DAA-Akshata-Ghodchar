# Graph Representation using Adjacency Matrix

class Graph:
    def __init__(self, vertices, directed=False):
        self.vertices = vertices
        self.directed = directed

        # Initialize adjacency matrix with zeros
        self.matrix = [[0 for _ in range(vertices)]
                       for _ in range(vertices)]

    # Add edge between two vertices
    def add_edge(self, u, v):
        if 0 <= u < self.vertices and 0 <= v < self.vertices:
            self.matrix[u][v] = 1

            if not self.directed:
                self.matrix[v][u] = 1
        else:
            print("Invalid vertex!")

    # Display adjacency matrix
    def display(self):
        print("\nAdjacency Matrix:")

        print("  ", end="")
        for i in range(self.vertices):
            print(i, end=" ")
        print()

        for i in range(self.vertices):
            print(i, end=" ")
            for j in range(self.vertices):
                print(self.matrix[i][j], end=" ")
            print()


# Main Program
print("GRAPH USING ADJACENCY MATRIX")

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