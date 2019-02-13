# Yinglan Chen
# Feb 2019
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
To modify floyd-warshall, we can exclude all bridge nodes in k
So that the shorted path between any pair of nodes, whether bridge or not, 
will not touch any bridge points
"""

# use matrix representation because edges are dense

# LIBRARIES
import csv
import sys

# GLOBAL
INT_MAX = sys.maxsize

# MAIN
def main():
	nodes = [] # problem extracting nodes; file inconsistent
	bridge_nodes = [] # read from bridge.csv, use hashset
 	###### template for creating bridge_nodes 
    with open('./starter_data/pgh_node.csv', newline='') as csvfile:
        bridgeheader = csv.reader(csvfile)
        header = next(nodereader) # skip title
        for row in bridgereader:
            append(row[?]); 
    ###### end of template 
    # create empty path matrix
    A = [[INT_MAX for j in range(num_nodes)] for i in range(num_nodes)]
    # initialize
    for i in range(num_nodes):
    	A[i][i] = 0
    for edge in range():
    	update A[u][v] = edge weights
    	
    # update
    for k in range(num_nodes):
    	# do not use bridge node when computing edge weights
    	if (k in bridge_nodes): continue 
    	for i in range(num_nodes):
    		for j in range(num_nodes):
    			A[i][j] = min(A[i][j], (A[i][k] + A[k][j]))

    # write output to some csv file
	return 0




if __name__ == '__main__':
	main()