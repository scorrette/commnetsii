from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import Node
from mininet.log import setLogLevel, info
from dijkstra import Graph
from staticTables import nodes_ex1, links_ex1,nodes_ex2, links_ex2,nodes_ex3, links_ex3
# create graph based on number of vertices
def createGraph(h_count, r_count,nodes,links):
    v_count = h_count + r_count #total node/vertice count
    g = Graph(v_count) #initialized graph

    links_list= []
    nodes_list = []
    dist = []
    nodeHop_map=[]
    router_nodeHop=[]
    staticRP =""

    #find name of statiicRP which is assumed to be the router connected to h1
    for link in links:
        if link[0] == "h1":
            staticRP = link[1]
        elif link[1] == "h1":
            staticRP = link[0]
    for key in nodes:
        nodes_list.append(key)   #generate list of node names from map
    for x in range(v_count):
        for y in range(v_count):
            for link in links:  #iterates over each tuple which represents a link
                if (nodes_list[x] == links[0] and nodes_list[y] == link[1]) or (nodes_list[y] == link[0] and nodes_list[x] == link[1]):
                    g.graph[x][y] = 1
                    g.graph[y][x] = 1
                elif x == y:
                    g.graph[x][y] = 0
                    
    
            
    # picks first router which we assume to be default RP as source, and returns distance list with corresponding vertice as index after dijkstra
    
    for j in range(r_count):  #find nodehop map for each router
        dist = g.dijkstra(h_count+j)
        router_nodeHop=[]
        for i in range(h_count):
            if i == 0:   #skip h1 to static rp as it should always be 1
                continue
            else:
                router_nodeHop.append((nodes_list[i], dist[i]))
        nodeHop_map.append(router_nodeHop)  #add map of router nodehops, to overall nodeHopmap 
    return nodeHop_map

def getNodeHopMap( ):
    rcount = 0
    hcount = 0

    for nodeName in nodes_ex1:
        if nodeName[0] =='h':  #confirm host is a client 
            hcount = hcount + 1
        else:
            rcount = rcount + 1

    return createGraph(hcount, rcount,nodes_ex1,links_ex1)
