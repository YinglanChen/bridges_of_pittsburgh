def main():
	input vertices.csv
	input node.csv


	return 0

def filter left only with internal nodes()

the problem is actually all pair shortest path
can I do better ? 

def dijsktra(graph, src, target):
	# Dijkstra's algorithm to find the shortest path between a and b. It picks the unvisited vertex with the lowest distance, calculates the distance through it to each unvisited neighbor, and updates the neighbor's distance if smaller. Mark visited (set to red) when done with neighbors.
	for all vertices, unvisited
	look up distance using nodes (assuming nodes are close enough so we use euclidean distance)
	initiall distance to all other vertices are infinity
	start from a , udpate a neighbors with their edge weights/ distance 
	find the unvisited vertex with the lowest distance
	calculates the distance through it each unviisted neightbor,
	updates the neighbors if smaller

	go until we reach b

	return shortest path

we will have to use n^2 space becasue almost every pair of vertex(Bridge)
has an edge between them, and it is two way (directed edge)

how to use graph representation 
# - adjancecy list (b1, b2, dist)
- adjancecy matrix [b1][b2] = xxx 


if __name__ == '__main__':
	main()