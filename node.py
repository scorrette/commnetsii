#!/usr/bin/python3
import struct
import sys
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
            pktType = struct.unpack("B", packet)

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
                pass

    def multicast(self, ):
        # TODO
        pass

    def commandListener(self):
        while True:
            inp = input()
            if (inp == "multicast"):
                self.multicast()

    def staticRPRoutine(self):
        # TODO add dijkstra here. Calculate Dyn RP
        pass


if __name__ == '__main__':

    # TODO change ip assignment and static RP to sys arg
    isStaticRP = True
    h = host("r1", "192.168.0.1", "8888", isStaticRP)

    if isStaticRP:
        h.staticRPRoutine()

    h.listen()
