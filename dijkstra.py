#!/usr/bin/python3
class Graph():
 
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]

    def minDistance(self, dist, sptSet):
 
        # Initialize minimum distance for next node
        min = 1e7
 
        # Search for the vertex(not closest) that is not in the shortest path tree set
        for v in range(self.V):
            if dist[v] < min and sptSet[v] == False:
                min = dist[v]
                min_index = v
 
        return min_index
 
#dijkstra function
    def dijkstra(self, src):
 
        dist = [1e7] * self.V
        dist[src] = 0
        shortestpathSet = [False] * self.V
 
        for cout in range(self.V):
            min_dist = self.minDistance(dist, shortestpathSet)
            shortestpathSet[min_dist] = True
 
            for each in range(self.V):
                if (self.graph[min_dist][each] > 0 and
                   shortestpathSet[each] == False and
                   dist[each] > dist[min_dist] + self.graph[min_dist][each]):
                    dist[each] = dist[min_dist] + self.graph[min_dist][each]
        return dist
