"""
Citation: https://www.geeksforgeeks.org/dijkstras-shortest-path-algorithm-greedy-algo-7/
Dijkstra Algorithm
1) Create a set sptSet (shortest path tree set) that keeps track of vertices 
included in shortest path tree, i.e., whose minimum distance from source is 
calculated and finalized. Initially, this set is empty.
2) Assign a distance value to all vertices in the input graph. 
Initialize all distance values as INFINITE. Assign distance value as 0 for the 
source vertex so that it is picked first.
3) While sptSet doesn’t include all vertices
….a) Pick a vertex u which is not there in sptSet and has minimum distance value.
….b) Include u to sptSet.
….c) Update distance value of all adjacent vertices of u. To update the 
distance values, iterate through all adjacent vertices. For every adjacent 
vertex v, if sum of distance value of u (from source) and weight of edge u-v, 
is less than the distance value of v, then update the distance value of v.
end of citation.

Idea2: Floyd-Warshall
Citation: https://www.cs.cmu.edu/~15451/lectures/lec09-dp2.pdf
# After each iteration of the outside loop, A[i][j] = length of the
# shortest i->j path that’s allowed to use vertices in the set 1..k
for k = 1 to n do:
	for each i,j do:
		A[i][j] = min( A[i][j], (A[i][k] + A[k][j]);
end of citation
"""
import csv

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