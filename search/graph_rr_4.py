import networkx as nx

class Graph:
    """
    Class to contain a graph and your bfs function
    
    You may add any functions you deem necessary to the class
    """
    def __init__(self, filename: str):
        """
        Initialization of graph object 
        """
        self.graph = nx.read_adjlist(filename, create_using=nx.DiGraph, delimiter=";")

    def bfs(self, start, end=None):
        """
        Perform breadth-first search traversal on the graph from the start node.
        
        If there's no end node input, return a list of nodes with the order of BFS traversal.
        If there is an end node input and a path exists, return a list of nodes with the order of the shortest path.
        If there is an end node input and a path does not exist, return None.
        """
        # Check if start node exists in the graph
        if start not in self.graph:
            return None
        
        # Initialize the BFS structures
        queue = [start]
        visited = set([start])  # to track visited nodes
        parent_dict = {}  # to track the parent node of each node for path reconstruction
        
        # If an end node is given, prepare to track the path
        if end:
            parent_dict[start] = None  # Start has no parent
        
        # Perform BFS
        while queue:
            current_node = queue.pop(0)
            
            # If we've reached the end node, stop the traversal
            if current_node == end:
                break

            for neighbor in self.graph[current_node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    parent_dict[neighbor] = current_node
                    queue.append(neighbor)
        
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

# Example usage:
if __name__ == "__main__":
    graph = Graph("data/tiny_network.adjlist")
    start_node = "Luke Gilbert"
    end_node = None
    
    # Run BFS with start and end nodes
    result = graph.bfs(start=start_node, end=end_node)
    print(f"BFS Result from {start_node} to {end_node}:")
    print(result)
    
    # Run BFS with only start node (no end node)
    result = graph.bfs(start=start_node)
    print(f"BFS Traversal from {start_node}:")
    print(result)
