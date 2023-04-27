from test4 import NetworkTopo, run
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import Node
from mininet.log import setLogLevel, info
from dijkstra import Graph
def createGraph(v_count,vertices,net): #create graph based on number of vertices
    g = Graph(v_count) #initialized graph
    links= []
    for each in net.links:
        links.append(each)
    for each in net.hosts:
        for link in links:
            if each == link.intf1.node:
                print("yes")
    for x in range(v_count):
        for y in range(v_count):
            for link in links:
                if (net.hosts[x] == link.intf1.node and net.hosts[y] == link.intf2.node) or (net.hosts[y] == link.intf1.node and net.hosts[x] == link.intf2.node):
                    g.graph[x][y]=1
                    g.graph[y][x]=1
                elif x==y:
                    g.graph[x][y] = 0
    print(g.graph)
    g.dijkstra(0)

def run1():
    topo = NetworkTopo()
    net = Mininet(topo=topo, controller = None)
    router_count=0
    router_list = []
    router_list2=[]
    for each in net.hosts: ##can i use net.hosts?
        #if each.name[0] =='r':  #confirm host is not a client but a router
        router_count = router_count + 1;  
        router_list.append(each)
    for each in router_list:
        print(each)
    run(net)
    createGraph(router_count,router_list,net)

if __name__ == '__main__':
    setLogLevel('info')
    run1()
