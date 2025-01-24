import networkx as nx

class Graph:

	def __init__(self, filename: str):
		self.graph = nx.read_adjlist(filename, create_using=nx.DiGraph, delimiter=";") # Initializes the graph object
		self.nodes = self.graph.number_of_nodes()
		self.edges = self.graph.number_of_edges()


	def __str__(self):
		return f"The number of nodes in this graph is {self.nodes} and the number of edges is {self.edges}"


	def bfs(self, start, end=None):
		# Making sure the start node is in graph
		if start not in self.graph:
			return None

		Q = []
		visited = []
		Q.append(start)
		visited.append(start)
		while len(Q)!=0:
			v = Q.pop(0)
			N = self.graph[v]
			for nodes in N:
				if nodes not in visited:
					visited.append(nodes)
					Q.append(nodes) 
	

