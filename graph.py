class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = []

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.vertices and vertex2 in self.vertices:
            self.vertices[vertex1].append(vertex2)
            self.vertices[vertex2].append(vertex1)

# {'A': ['B'], 'B': ['A']}

    def display(self):
        for vertex, neighbors in self.vertices.items():
            print(f"{vertex}: {neighbors}")

# Creating a graph
#my_graph = Graph()
#my_graph.add_vertex("A")
#my_graph.add_vertex("B")
#my_graph.add_edge("A", "B")
#my_graph.display()

my_graph = Graph()

my_graph.add_vertex("A")
my_graph.add_vertex("B")
my_graph.add_vertex("C")
my_graph.add_vertex("D")

my_graph.add_edge("A", "B")
my_graph.add_edge("A", "C")
my_graph.add_edge("B", "C")
my_graph.add_edge("C", "D")

print("Graph representation:")
print(my_graph.display())