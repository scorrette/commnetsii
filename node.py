#!/usr/bin/python3
import struct
import sys
from topoToGraph import getNodeHopMap
from socket import socket, AF_INET, SOCK_DGRAM
from threading import Thread
from packets import hello, helloACK, multicast, unicast
from mininet.node import Node
import staticTables
import helperMethods

# number of total destinations
N = 3
# number of selected destinations
K = 2


class MyHost(Node):

    def __init__(self, name, ip, port, isStaticRP):
        self.name = name
        self.ipInt = helperMethods.ipv4_to_int(ip)
        self.ip = ip
        self.port = port
        self.staticRP = isStaticRP

    def start_listener(self):
        s = socket(AF_INET, SOCK_DGRAM)
        s.bind((self.ip, self.port))

        while True:
            packet, addr = s.recvfrom(1024)
            pktType = struct.unpack("B", packet[0:struct.calcsize("B")])

            # HELLO
            if pktType == 1:
                _, seq, ttl, src = hello.read_header(packet)
                print(self.name + " received HELLO packet from: " + src)
                print(self.name + " sending reply to " + src)
                helloACK.create_packet(seq, ttl, self.ipInt, src)

            # HELLO ACK
            if pktType == 2:
                _, seq, ttl, src, dest = helloACK.read_header(packet)
                print(self.name + " received HELLOACK from: " + src)

            # Multicast
            if pktType == 3:
                # multicast packets are always encapsulated by unicast
                pass

            # Unicast
            if pktType == 4:
                _, seq, ttl, src, dest = unicast.read_header()

                if dest == self.ipInt:
                    pktContent = unicast.read_content()
                    contentType = struct.unpack("B", pktContent[0:struct.calcsize("B")])

                    # If the packet was a multicast packet destined for itself
                    if contentType == 3:
                        # TODO two behaviors. If this is static RP, forward to dynamic RP. If this is not (then this is dynamic RP) split and unicast packet forward
                        pass

                    else:
                        print(self.name + " received packet from: " + src)
                else:
                    # TODO forward packet
                    pass

                pass

    def multicast(self):
        # IP of all destinations as string
        destsStr = [staticTables.nodes_ex1[x] for x in staticTables.multicast_destinations_ex1]
        dests = [helperMethods.ipv4_to_int() for x in destsStr]

        # create multicast packet
        mcPkt = multicast.create_packet(1, 999, self.ipInt, dests, "Multicast Packet!!!")
        print(self.name + " building multicast packet with destinations: " + str(staticTables.multicast_destinations_ex1))

        # encapsulate multicast packet in unicast
        dest = helperMethods.ipv4_to_int(staticTables.nodes_ex1[staticTables.staticRP_ex1])

        pkt = unicast.create_packet(1, 999, self.ipInt, dest, mcPkt)
        print(self.name + " encapsulating multicast packet with unicast with destination: " + staticTables.staticRP_ex1)



    def commandListener(self):
        while True:
            inp = input()
            if (inp == "multicast"):
                self.multicast()

    def staticRPRoutine(self, k, n):
        def insertionSort(arr):

            if (n := len(arr)) <= 1:
                return arr
            for i in range(1, n):

                key = arr[i]

                # Move elements of arr[0..i-1], that are
                # greater than key, to one position ahead
                # of their current position
                j = i - 1
                while j >= 0 and key < arr[j]:
                    arr[j + 1] = arr[j]
                    j -= 1
                arr[j + 1] = key
            return

        # TODO add dijkstra here. Calculate Dyn RP
        MasterNodeHopMap = getNodeHopMap()
        dist_array = []
        router_longest_dist = []  # array of longest dist of each router
        for routerNodeHopMap in MasterNodeHopMap:
            for dest in routerNodeHopMap:
                dist_array.append(dest[1])
            # dist_array = insertionSort(dist_array)  #sort array
            insertionSort(dist_array)  # sort array
            if k == n:
                router_longest_dist.append(dist_array[
                                               n - 1])  # append the longest dist required for that router which is that last element in the array
            else:
                router_longest_dist.append(dist_array[k - 1])  # otherwise append longest dist depending on K

        index = 0  # index of ideal/dynamic rp
        shortest = 1000  # just intialize shortest dist to some default high number that will not be valid for the topo
        for i in range(len(router_longest_dist)):
            if router_longest_dist[i] < shortest:
                shortest = router_longest_dist[i]
                index = i
        router_name = "r" + str(
            index + 1)  # assuming router starts at r1 and increments, and all the routers from the nodehopmap are sorted in ascending order(they should be)
        self.dynamicRP = router_name  # **sets name of the router to dynamicRP var of node**


if __name__ == '__main__':

    # TODO change ip assignment and static RP to sys arg
    # name, ip, port, isStaticRP
    h = MyHost(sys.argv[1], sys.argv[2], int(sys.argv[3]), sys.argv[4] == 'True')

    if sys.argv[4] == 'True':
        h.staticRPRoutine(K, N)

    h.start_listener()
