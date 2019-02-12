# Yinglan Chen
# Feb 2019
# This file takes in a csv file with all nodes identified by OSM
# filter nodes by within_bound = True and is_bridge
# output a csv file that contain all the bridge nodes 
# this output will be the vertices of the abstracted graph

# Require
# Format on input edge.csv file:
# - the last column has field "within_boundaries" and values "TRUE" or "FALSE"
# LIBRARY
import csv
# GLOBALS, dependent on format of csv file

WITHIN_BOUND = 10
OSM_BRIDGE = 5
# each bridge occupies 2 nodes
def main():
    # for simplicity, hard code filename here
    # for more general use, use command line arguments
    output = [] 
    with open('./starter_data/pgh_edges.csv', newline='') as csvfile:
        nodereader = csv.reader(csvfile)
        next(nodereader) # skip title

        for row in nodereader:
            if foo_counter > 10: break
            if (row[WITHIN_BOUND] == "TRUE" and row[OSM_BRIDGE] == "yes"):
                output.add(row)
                # write the entire row to an output file 
            # otherwise:
                # discard the road
    return 0        
            

    # finish writing the output file 
    # with open('?.csv', mode='w', newline='') as csvfile:
    #     vertex_writer = csv.writer(csvfile, delimiter=',',
    #                         quotechar='|', quoting=csv.QUOTE_MINIMAL)
    #     for vertices in v:
    #         vertex_writer.writerow(v[])
    #         vertex_writer.writerow(v[])
    

if __name__ == '__main__':
    main()