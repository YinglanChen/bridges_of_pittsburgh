# Yinglan Chen
# Feb 2019
# This file takes in a csv file with all nodes identified by OSM
# filter nodes by within_bound = True and is_bridge
# output a csv file that contain all the bridge nodes 
# this output will be the vertices of the abstracted graph

# Dependency: header of input csv file is as follows:
#   from,to,id,osm_way_id,osm_bridge_relation_id,osm_bridge,osm_highway,
#   osm_label,bridge_id,distance,within_boundaries

# PROBLEMs
# We expect each bridge occupies 2 nodes, but in the output file, 
# a bridge has multiple nodes
# not all bridges have birdge_id

# LIBRARY
import csv

# GLOBALS, dependent on format of csv file
WITHIN_BOUND = 10
OSM_BRIDGE = 5
OSM_LABEL = 7
FROM_ID = 0
TO_ID = 1

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
    # merge node with same id
    # what to do if no label? 
    # for b in range(len(output)):
    #     row = output[b];
    #     if (b == len(output) - 1): continue
    #     next_row = output[b+1]
    #     curr_label = row[osm_label];
    #     next_label = next_row[osm_label];
    #     # find min from and max to merge
    #     if (curr_label == next_label):
    #         from_id = min(row[FROM_ID], next_row[FROM_ID])
    #         to_id = max(row[TO_ID], row[TO_ID])
    #         delete 2 rows and add new row with (from_id, to_id )

    with open('./processed_data/bridges.csv', mode='w', newline='') as csvfile:
        bridge_writer = csv.writer(csvfile, delimiter=',')
        bridge_writer.writerow(header)
        for row in output:
            bridge_writer.writerow(row)
    return 0        
            
if __name__ == '__main__':
    main()