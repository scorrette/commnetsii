from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import Node
from mininet.log import setLogLevel, info
from dijkstra import Graph

# create graph based on number of vertices
def createGraph(h_count, r_count, net):
    v_count = h_count + r_count #total node/vertice count
    g = Graph(v_count) #initialized graph

    links= []
    dist = []
    nodeHop_map=[]

    for each in net.links:
        links.append(each)
    for x in range(v_count):
        for y in range(v_count):
            for link in links:
                if (net.hosts[x] == link.intf1.node and net.hosts[y] == link.intf2.node) or (net.hosts[y] == link.intf1.node and net.hosts[x] == link.intf2.node):
                    g.graph[x][y] = 1
                    g.graph[y][x] = 1
                elif x == y:
                    g.graph[x][y] = 0

    # picks first router which we assume to be default RP as source, and returns distance list with corresponding vertice as index after dijkstra
    dist = g.dijkstra(h_count)
    for i in range(h_count):
        if i == 0:
            continue
        else:
            nodeHop_map.append((net.hosts[i], dist[i]))

    return nodeHop_map

def getNodeHopMap( net ):
    rcount = 0
    hcount = 0

    for h in net.hosts:
        if h.name[0] =='h':  #confirm host is a client 
            hcount = hcount + 1
        else:
            rcount = rcount + 1

    return createGraph(hcount, rcount, net)

if __name__ == '__main__':
    getNodeHopMap()
