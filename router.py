#!/usr/bin/python
import sys
from socket import socket, AF_INET, SOCK_DGRAM
from threading import Thread

class router:
    def __init__(self,ip,port,isStaticRP):
        self.ip = ip
        self.port = port
        self.staticRP = isStaticRP

    def flood(self):
        #TODO implement
        pass

    def listen(self):
        s = socket(AF_INET, SOCK_DGRAM)
        s.bind((self.ip, self.port))

        while True:
            packet, addr = s.recvfrom(1024)
            #TODO

    def staticRPRoutine(self):
        #TODO add dijkstra here. Calculate Dyn RP
        pass





if __name__ == '__main__':


    # TODO change ip assignment and static RP to sys arg
    isStaticRP = True
    r = router("192.168.0.1","8888",isStaticRP)

    r.flood()

    if isStaticRP:
        r.staticRPRoutine()


    r.listen()