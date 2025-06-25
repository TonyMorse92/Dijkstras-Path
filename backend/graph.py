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
	def find_path(self, v1, v2, path=None):
		#print(f"path at start: {path}")
		if path is None:
			path = []
		
		# Any vertex can get to itself
		if v1 == v2:
			return v1


		# v1 is the start, might want to rename				
		for v in self.verticies:
			print(f"Count: {count}")
			if e not in path:
				# Assume there aren't a bunch of duplicate edges
				print(f"e:  {e.v1} and {e.v2}")
				#print(f"e: {e}")
				if e.v1 == v1 and e.v2 == v2:
					path.append(e)
					return path
			
				elif e.v1 == v1:	
					path.append(e)	
					#print("second")
					#print(f"Next find_path(): {e.v2}, {v2}")
					sub_path = self.find_path(e.v2, v2, path)
					#print(f"Path now: {sub_path}")
					#if sub_path:
						#path = path + sub_path
				
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

print(f"find_path(a,b): {g.find_path('a','b')}")
print("\n\n")
print(f"find_path(a,d): {g.find_path('a','d')}")
print("\n\n")
print(g.find_path("a","c"))
#print("\n\n")
