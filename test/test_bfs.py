# write tests for bfs
import pytest
from search.graph_rr_3 import Graph

def test_bfs_traversal():
	"""
    	TODO: Write your unit test for a breadth-first
    	traversal here. Create an instance of your Graph class 
    	using the 'tiny_network.adjlist' file and assert 
    	that all nodes are being traversed (ie. returns 
    	the right number of nodes, in the right order, etc.)
    	"""
	graph = Graph("data/tiny_network.adjlist")

	result = graph.bfs(start="Luke Gilbert")
	expected_traversal = ['Luke Gilbert', '33483487', '31806696', '31626775', '31540829', 'Martin Kampmann', 'Neil Risch', 'Nevan Krogan', '32790644', '29700475', '34272374', '32353859', '30944313', 'Steven Altschuler', 'Lani Wu', 'Michael Keiser', 'Atul Butte', 'Marina Sirota', 'Hani Goodarzi', '32036252', '32042149', '30727954', '33232663', '33765435', '33242416', '31395880', '31486345', 'Michael McManus', 'Charles Chiu', '32025019']
	assert result == expected_traversal, f"Expected BFS traversal: {expected_traversal}, but got {result}"
	

def test_bfs():
	"""
    	TODO: Write your unit test for your breadth-first 
    	search here. You should generate an instance of a Graph
    	class using the 'citation_network.adjlist' file 
    	and assert that nodes that are connected return 
    	a (shortest) path between them.
    
    	Include an additional test for nodes that are not connected 
    	which should return None. 
    	"""
	graph = Graph("data/citation_network.adjlist")
	
	# Shortest path between two connected nodes
	result_connected = graph.bfs(start='Lani Wu',end='Hani Goodarrzi')
	expected_path = ['Lani Wu', '32042149', 'Hani Goodarzi']
	assert result_connected == expected_path, f"Expected path: {expected_path}, but got {result_connected}"
	
	# Shortetest path between two unconnected nodes
	result_unconnected = graph.bfs(start='34675264',end='34804600')
	assert result_unconnected is None, f"Expected None for unconnected nodes, but got {result_unconnected}"
	
	# Start node does not exist 
	result_missing_start = graph.bfs(start='1',end='Hani Goodarzi')
	assert result_missing_start is None, f"Expected None for invalid start node, but got {result_missing_start}"

	# End node does not exist 
	result_missing_end = graph.bfs(start='Lani Wu',end='101')
	assert result_missing_end is None, f"Expected None for invalid end note, but got {result_missing_end}"
 


