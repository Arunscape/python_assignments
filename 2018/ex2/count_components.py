#!/usr/bin/python3
from graph import Graph
from breadth_first_search import breadth_first_search
import csv

def count_components(g) :
    vertices = g.get_vertices()

    numcomponents=0
    while vertices:
        #get next vertex and search what nodes are reach
        for v in vertices:
            vertex=v
            break;
        #this way, I can get vertex from the vertices set without popping

        reached=breadth_first_search(g,vertex) #get dict of reached nodes

        for node in reached:
            vertices.remove(node)
            #remove vertices if reached
        numcomponents += 1

    #print(numcomponents)
    return numcomponents

def read_city_graph_undirected(filename):
    g=Graph() #new graph instance

    with open(filename) as f:
        csvdata=csv.reader(f)

    #file closed with this syntax

        for line in csvdata:
            if line[0]=='V':
                #vertex id is at index 1
                g.add_vertex(line[1])
            elif line[0]=='E':
                #edges are at indices 2 and 3

                #add twice because undirected
                g.add_edge( (line[1], line[2]) )
                g.add_edge( (line[2], line[1]) )

    #return graph class instance
    return g

if __name__ == "__main__":
    yeg_graph = read_city_graph_undirected("edmonton-roads-2.0.1.txt")
    print(count_components(yeg_graph))

#rough work, prettyed up version above, but my thought process can be
#seen here
#messy count_components
# def count_components(g) :
#     vertices = g.get_vertices()
#     #print('vertices: {}'.format(vertices))
#
#     numcomponents=0
#     while vertices:
#         #loops as long as vertices set is not empty
#         #v=vertices.pop() #pops item out of set and stores it in v so I can use it
#
#         #this doesn't remove the initial node, so I don't have to use the
#         #commented out try/except clause to escape attempting to remove
#         #a nonexisting element in the set
#         for v in vertices:
#             vertex=v
#             break;
#         #this way, I can get vertex from the vertices set without popping
#
#         reached=breadth_first_search(g,vertex) #get dict of reached nodes
#         # print('vertices: {}'.format(vertices))
#         # print('reached: ')
#         # print(reached)
#         # print()
#         #print(reached.items())
#
#         #abandoned this, because it turns the dictionary to a alist
#         #which might be slower to access, if I understood the assignment description correctly
#         # for node, reached_from in reached.items():
#         #     print('{} {}'.format(node,reached_from)
#
#
#         for node in reached:
#             # print(vertices)
#             vertices.remove(node)
#             #it works, but this is sloppy
#             # try:
#             #     vertices.remove(node)
#             # except:
#             #     pass
#
#         numcomponents += 1
#
#     print(numcomponents)
#     return numcomponents
