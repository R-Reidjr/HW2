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
        # Initialize the bfs 
		Q = []
		visited = []
		parent_dict = {start: None}
		Q.append(start)
		visited.append(start)
		while len(Q)!=0:
			v = Q.pop(0)
			if v == end:
				break
			elif v != end:
				N = self.graph[v]
				for neighbor in N:
					if neighbor not in visited:
						visited.append(neighbor)
						parent_dict[neighbor] = v
						Q.append(neighbor)
			
			# If no end node is provided, return the BFS traversal order
			if not end:
				return list(visited)
        
        	# If end node was specified, check if it was visited (path exists)
			if end not in visited:
				return None
        
     		# Reconstruct the path from start to end using the parent_dict
		path = []
		current = end
		while current is not None:
			path.append(current)
			current = parent_dict.get(current)
        
        # Return the path in the correct order (start to end)
		return path[::-1]
		#return visited
	

