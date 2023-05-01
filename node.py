#!/usr/bin/python3
import struct
import sys
from topoToGraph import getNodeHopMap
from socket import socket, AF_INET, SOCK_DGRAM
from threading import Thread

from packets import hello, helloACK, multicast, unicast


class host:
    def __init__(self, id, ip, port, isStaticRP):
        self.id = id
        self.ip = ip
        self.port = port
        self.staticRP = isStaticRP

    def listen(self):
        s = socket(AF_INET, SOCK_DGRAM)
        s.bind((self.ip, self.port))

        while True:
            packet, addr = s.recvfrom(1024)
            pktType = struct.unpack("B", packet[0:struct.calcsize("B")])

            # HELLO
            if pktType == 1:
                _, seq, ttl, src = hello.read_header(packet)
                print(self.id + " received HELLO packet from: " + src)
                print(self.id + " sending reply to " + src)
                helloACK.create_packet(seq, ttl, self.id, src)

            # HELLO ACK
            if pktType == 2:
                _, seq, ttl, src, dest = helloACK.read_header(packet)
                print(self.id + " received HELLOACK from: " + src)

            # Multicast
            if pktType == 3:
                pass

            # Unicast
            if pktType == 4:
                _, seq, ttl, src, dest = unicast.read_header()

                if dest == self.id:
                    pktContent = unicast.read_content()
                    contentType = struct.unpack("B", pktContent[0:struct.calcsize("B")])

                    # If the packet was a multicast packet destined for itself
                    if contentType == 3:
                        # TODO two behaviors. If this is static RP, forward to dynamic RP. If this is not (then this is dynamic RP) split and unicast packet forward
                        pass

                    else:
                        print(self.id + " received packet from: " + src)

                pass

    def multicast(self, ):
        # TODO
        pass

    def commandListener(self):
        while True:
            inp = input()
            if (inp == "multicast"):
                self.multicast()

    def staticRPRoutine(self,k,n,net):
        # TODO add dijkstra here. Calculate Dyn RP
        MasterNodeHopMap= getNodeHopMap(net)
        dist_array=[]
        router_longest_dist=[]  #array of longest dist of each router
        for routerNodeHopMap in MasterNodeHopMap:
            for dest in routerNodeHopMap:
                dist_array.append(dest[1])
            dist_array = insertionSort(dist_array)  #sort array
            if k == n:
                router_longest_dist.append(dist_array[n-1])   #append the longest dist required for that router which is that last element in the array
            else:
                router_longest_dist.append(dist_array[k-1])  #otherwise append longest dist depending on K
            
        index = 0   #index of ideal/dynamic rp
        shortest=1000  #just intialize shortest dist to some default high number that will not be valid for the topo
        for i in range(len(router_longest_dist)):
            if router_longest_dist[i] < shortest:
                shortest = router_longest_dist[i]
                index = i
        router_name = "r" + str(index+1)  #assuming router starts at r1 and increments, and all the routers from the nodehopmap are sorted in ascending order(they should be)
        self.dynamicRP = router_name  #**sets name of the router to dynamicRP var of node**  
    def insertionSort(arr):
         
        if (n := len(arr)) <= 1:
          return arr
        for i in range(1, n):
             
            key = arr[i]
     
            # Move elements of arr[0..i-1], that are
            # greater than key, to one position ahead
            # of their current position
            j = i-1
            while j >=0 and key < arr[j] :
                    arr[j+1] = arr[j]
                    j -= 1
            arr[j+1] = key
        return arr

if __name__ == '__main__':

    # TODO change ip assignment and static RP to sys arg
    isStaticRP = True
    h = host("r1", "192.168.0.1", "8888", isStaticRP)

    if isStaticRP:
        h.staticRPRoutine()

    h.listen()
