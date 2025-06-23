### Weighted graph for Dijkstra's algorithm


class Graph:
	
	def __init__(self):
		self.verticies = []
		self.edges = []

	def add_vertex(self, v):
		self.verticies.append(v)

	def add_edge(self, e):
		v1 = e.v1
		v2 = e.v2

		if v1 not in self.verticies:
			self.add_vertex(v1)
		if v2 not in self.verticies:
			self.add_vertex(v2)
	
		self.edges.append(e)	

	def __str__(self):
		return f"{self.verticies}\n\n{self.edges}"	


class Edge:
	
	def __init__(self, v1, v2, w):
		self.v1 = v1
		self.v2 = v2
		self.w = w


	def __repr__(self):
		return f"Edge of weight {self.w} from {self.v1} to {self.v2}"




e1 = Edge("a", "b", 2)
e2 = Edge("c", "d", 3)
e3 = Edge("a", "d", 2)


g = Graph()

g.add_edge(e1)
g.add_edge(e2)
g.add_edge(e3)


print(g)
