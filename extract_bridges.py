# Yinglan Chen
# Feb 2019
# This file takes in a csv file with all nodes identified by OSM
# filter nodes by within_bound = True and is_bridge
# output a csv file that contain all the bridge nodes 
# this output will be the vertices of the abstracted graph

# Dependency: header of input csv file is as follows:
#   from,to,id,osm_way_id,osm_bridge_relation_id,osm_bridge,osm_highway,
#   osm_label,bridge_id,distance,within_boundaries

# PROBLEM TO DO
# We expect each bridge occupies 2 nodes, but in the output file, 
# a bridge has multiple nodes

# LIBRARY
import csv

# GLOBALS, dependent on format of csv file
WITHIN_BOUND = 10
OSM_BRIDGE = 5


def main():
    # for simplicity, hard code filename here
    # for more general use, use command line arguments
    output = [] 
    with open('./starter_data/pgh_edges.csv', newline='') as csvfile:
        nodereader = csv.reader(csvfile)
        header = next(nodereader) # skip title
        for row in nodereader:
            # discard row if not within bound or not bridge
            if (row[WITHIN_BOUND] == "TRUE" and row[OSM_BRIDGE] == "yes"):
                output.append(row)
            
    with open('./processed_data/bridges.csv', mode='w', newline='') as csvfile:
        bridge_writer = csv.writer(csvfile, delimiter=',')
        bridge_writer.writerow(header)
        for row in output:
            bridge_writer.writerow(row)
    return 0        
            
if __name__ == '__main__':
    main()