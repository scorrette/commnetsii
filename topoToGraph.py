from test4 import NetworkTopo, run
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import Node
from mininet.log import setLogLevel, info
from dijkstra import Graph
def createGraph(h_count,r_count,vertices,net): #create graph based on number of vertices
    v_count = h_count+r_count #total node/vertice count
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
                    g.graph[x][y]=1
                    g.graph[y][x]=1
                elif x==y:
                    g.graph[x][y] = 0
    print(g.graph)
    dist =g.dijkstra(h_count)  #picks first router which we assume to be default RP as source, and returns distance list with corresponding vertice as index after dijkstra
    for i in range(h_count):
        if i==0:
            continue
        else:
            nodeHop_map.append((net.hosts[i],dist[i]))
    print(nodeHop_map)

def run1(): ##This should be done in top file, but can call createGraph from Top file
    topo = NetworkTopo()
    net = Mininet(topo=topo, controller = None)
    router_count=0
    host_count = 0
    node_list = []
    router_list2=[]
    for each in net.hosts: ##can i use net.hosts?
        if each.name[0] =='h':  #confirm host is a client 
            host_count = host_count +1
        else:
            router_count = router_count + 1  
        node_list.append(each)
    for each in node_list:
        print(each)
    run(net)
    createGraph(host_count , router_count,node_list,net)

if __name__ == '__main__':
    setLogLevel('info')
    run1()
