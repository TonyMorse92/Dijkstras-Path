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

	# Path starts at v1 and terminates at v2. 
	# I guess I'm implicitly treating this as a directed graph.
	# Can generalize to undirected later
	def find_path(self, v1, v2, path=None):
		print(f"path at start: {path}")
		if path is None:
			path = []	
		for e in self.edges:
			if e.v1 == v1 and e.v2 == v2:
				print("got here.")	
				path.append(e)
				break
				
			elif e.v1 == v1:
				print("second")
				find_path(e.v2, v2)
				
		return path

	def __str__(self):
		return f"{self.verticies}\n{self.edges}"	


class Edge:
	
	def __init__(self, v1, v2, w):
		self.v1 = v1
		self.v2 = v2
		self.w = w


	def __repr__(self):
		return f"Edge of weight {self.w} from {self.v1} to {self.v2}"




e1 = Edge("a", "b", 2)
e2 = Edge("b", "c", 2)
e3 = Edge("a", "d", 2)
e4 = Edge("c", "d", 3)


g = Graph()

g.add_edge(e1)
g.add_edge(e2)
g.add_edge(e3)


print(g)
print("\n\n")

print(g.find_path("a","b"))
#g.find_path("a","d")
print(g.find_path("a","c"))
