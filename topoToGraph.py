from test4 import NetworkTopo
from dijkstra import Graph
def createGraph(v_count,vertices,net): #create graph based on number of vertices
    g = Graph(v_count) #initialized graph
    for x in range(v_count):
        for y in range(v_count):
            if x == y:
                g.graph[x,y] = 0
            elif net[vertices[x].name].cmd("ping " + vertices[y].name)== 0  #   can i do this??  0 packet loss means theres link
                g.graph[x,y] = 1
                g.graph[y,x] = 1  #add in edge into adjacent matrix with cost of 1

g.dijkstra(0)

def run():
    topo = NetworkTopo()
    net = Mininet(topo=topo, controller = None)
    router_count=0
    router_list = []
    for each in net.hosts: ##can i use net.hosts?
        if each.name[0] =='r':  #confirm host is not a client but a router
            router_count = router_count + 1;  
            router_list.append(each)
    
