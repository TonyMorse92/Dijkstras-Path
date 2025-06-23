### Weighted graph for Dijkstra's algorithm


class Weighted_Graph:
	
	def __init__(self):
		self.verticies = []
		self.edges = []

	def add_vertex(self, v):
		self.verticies.append(v)

	def add_edge(self, e, w):
		v1 = e[0]
		v2 = e[1]

		
