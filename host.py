#!/usr/bin/python
from socket import socket, AF_INET, SOCK_DGRAM
from threading import Thread

class host:
    def __init__(self,ip,port):
        self.ip = ip
        self.port = port

    def listen(self):
        s = socket(AF_INET, SOCK_DGRAM)
        s.bind((self.ip, self.port))
        while True:
            packet, addr = s.recvfrom(1024)
            #TODO packet processing
            print(packet)
    def multicast(self,):
        #TODO
        pass

    def commandListener(self):
        while True:
            inp = input()
            if (inp == "multicast"):
                self.multicast()


if __name__ == '__main__':

    #TODO change ip assignment to arg
    h = host("192.168.0.1","8888")
    receiver = Thread(h.listen)
    receiver.start()

    sender = Thread(h.commandListener())
    sender.start()




