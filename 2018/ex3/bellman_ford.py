"""
Arun Woosaree
Implements the Bellman-Ford algorithim with Graph potentials

Doctests:
>>> vertices = {1, 2, 3, 4, 5, 6}
>>> edges = {(1,2):5, (2,5):-7, (3,2):2, (4,1):-2, (5,1):3, (5,3):6, (5,4):4, (6,3):2, (6,5):-10}
>>> dist, reached = bellman_ford(vertices, edges, 1)
>>> potential=find_potential(vertices,edges)
>>> dist[5]
-2
>>> reached.keys() == {1, 2, 3, 4, 5}
True
>>> potential[5] + edges[(2,5)] >= potential[2]
True
>>> potential[2] + edges[(2,5)] >= potential[5]
False
>>> edges[(5,4)] = 3   # creates a negative-cost cycle
>>> print(find_potential(vertices, edges))
None
>>>
>>>
>>>
>>> vertices = {1, 2, 3, 4, 5, 6, 7}
>>> edges = {(2,1):1, (5,2):7, (2,3):-2, (1,4):10, (1,5):-3, (3,5):-3, (4,5):-4, (3,6):-2, (5,6):10, (7,1):-100}
>>> dist, reached = bellman_ford(vertices,edges,1)
>>> potential=find_potential(vertices,edges)
>>> dist[3]
2
>>> reached.keys() == {1,2,3,4,5,6}
True
>>> potential[5] + edges[(5,2)] >= potential[2]
True
>>> potential[2] + edges[(2,3)] >= potential[3]
False
>>> edges[(5,2)] = -7   # creates a negative-cost cycle
>>> print(find_potential(vertices, edges))
None
>>>
>>>
>>>
>>> vertices = {1, 2, 3, 4, 5, 6, 7, 8, 9}
>>> edges = {(1,2):1, (1,9):-7, (4,1):2, (4,2):3, (6,2):-3, (8,2):-9, (6,8):9, (3,9):7, (7,3):6, (9,7):-5, (7,6):4, (5,7):5, (5,6):8}
>>> dist, reached = bellman_ford(vertices,edges,1)
>>> potential=find_potential(vertices,edges)
>>> dist[8]
1
>>> reached.keys()=={1,2,3,6,7,8,9}
True
>>> potential[6] + edges[(6,8)]>= potential[8]
True
>>> potential[4] + edges[(4,2)] >= potential[2]
False
>>> edges[(3,9)] = -7   # creates a negative-cost cycle
>>> print(find_potential(vertices, edges))
None
"""

def bellman_ford(vertices, edges, start):
    '''
    Computes shortest paths to every reachable vertex from the vertex "start"
    in the given directed graph.

    vertices: the set of vertices in the graph.
    edges: maps pairs of vertices to values representing edge costs
    example - {('A', 'B'): -3} means the edge from vertex
    'A' to vertex 'B' has cost -3
    start: the start vertex to search from

    Assumes the graph does not have negative cost cycles,
    that all edges have endpoints in "vertices", and that
    "start" is also in "vertices".

    returns dist, reached

    Here reached is the search tree to all reachable vertices along
    minimum-cost paths and dist[v] is the cost to v along
    this path. If v is not reachable, it should not be in the
    search tree nor an index in dist.
    '''
    # debugging
    # print('vertices: {}'.format(vertices))
    # print('edges: {}'.format(edges))
    # print('start: {}'.format(start))

    #Same as with all other searches.
    #Reached dict maps vertices to predecessors on the search tree
    reached={start:start}

    dist=dict() #Keys are vertices, values store distance
    #initially, the weights are infinity, except the source is 0
    for v in vertices:
        dist[v]=float('inf')
    dist[start]=0

    #loops |V|-1 times
    #ex: if V={1,2,3,4,5,6}, then it loops 5 times.
    #i starting from 1
    for i in range(1,len(vertices)):
        for u,v in edges:
            if dist[v] > dist[u] + edges[(u,v)]: #edges[(u,v)] is the cost
                dist[v] = dist[u] + edges[(u,v)]
                reached[v] = u

    #delete unreachable vertices
    for v in vertices:
        if dist[v]==float('inf'):
            del dist[v]
    return dist, reached

def find_potential(vertices, edges):
    '''
    Finds a potential for the graph or determines the graph has
    a negative-cost cycle.

    vertices: the set of vertices in the graph.
    edges: maps pairs of vertices to values representing edge costs
       example - {('A', 'B'): -3}Uploading, please wait... means the edge from vertex
                 'A' to vertex 'B' has cost -3
    start: the start vertex to search from

    If the graph has a negative-cost cycle, this simply returns None.
    Otherwise, it returns a dictionary mapping each vertex to its value
    in a potential function.
    '''
    #initially dist[v] = 0 for every vertex v
    dist=dict()
    for v in vertices:
       dist[v]=0

    #main loop of Bellman-Ford
    for i in range(1,len(vertices)):
        for u,v in edges:
            if dist[v] > dist[u] + edges[(u,v)]: #edges[(u,v)] is the cost
                dist[v] = dist[u] + edges[(u,v)]
                #reached[v] = u
                #no need for reached dict
    for u,v in edges:
        #check for negative cost cycle
        if dist[u] + edges[(u,v)] < dist[v]:
            return None

    #no negative cost cycle so return dict of potentials
    for v in vertices:
        dist[v]=-dist[v]
    return dist



if __name__=="__main__":
    import doctest
    doctest.testmod()
