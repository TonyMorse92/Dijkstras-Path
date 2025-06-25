## Weighted graph for Dijkstra's algorithm


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

	# Undirected graph
	def find_path(self, v1, v2, path=[]):
		#print(f"path at start: {path}")
		path = path + [v1]	

		# Any vertex can get to itself
		if v1 == v2:
			return path


		# v1 is the start, might want to rename				
		for v in self.verticies:
			# Don't visit same node multiple times (initially)	
			if v not in path:
				sub_path = self.find_path(v, v2, path)
				if sub_path:
					return sub_path
		return None

	def __str__(self):
		return f"{self.verticies}\n{self.edges}"	


class Edge:
	
	def __init__(self, v1, v2, w):
		self.v1 = v1
		self.v2 = v2
		self.w = w


	def __repr__(self):
		return f"Edge of weight {self.w} between {self.v1} and {self.v2}"




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

print(f"find_path(a,a): {g.find_path('a','a')}")
print("\n\n")
print(f"find_path(a,b): {g.find_path('a','b')}")
print("\n\n")
print(f"find_path(a,d): {g.find_path('a','d')}")
print("\n\n")
print(f"find_path(a,c): {g.find_path('a','c')}")
print("\n\n")

print(f"find_path(c,b): {g.find_path('c','b')}")
print("\n\n")
print(f"find_path(d,a): {g.find_path('d','a')}")
print("\n\n")
