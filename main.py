#!/usr/bin/python3
from mininet.net import Mininet
from mininet.log import lg, info
from mininet.cli import CLI
from mininet.node import Node
from mininet.clean import Cleanup

class MyHost( Node ):
    def config( self, **params ):
        super( MyHost, self).config( **params )

    def start_listener( self ):
        print('Hello World!')

    def terminate( self ):
        super( MyHost, self ).terminate()

class Net(Mininet):
    def __init__(self):
        Mininet.__init__(self, controller = None, cleanup = True)

        # Creating Hosts
        info("Creating nodes\n")
        r1 = self.addHost('r1', cls = MyHost, inNamespace = False)
        r2 = self.addHost('r2', cls = MyHost, inNamespace = False)
        h1 = self.addHost('h1', cls = MyHost, inNamespace = False)
        h2 = self.addHost('h2', cls = MyHost, inNamespace = False)
        h3 = self.addHost('h3', cls = MyHost, inNamespace = False)

        # Establishing the links from hosts to routers
        info("Creating links\n")
        self.addLink(h1, r1, intfName2='r1-eth0')
        self.addLink(h2, r2, intfName2='r2-eth2')
        self.addLink(h3, r2, intfName2='r2-eth3')
        self.addLink(r1, r2, intfName1='r1-eth1', intfName2='r2-eth1')

        # Setting interface ip addresses since params1 or params2 just will not work
        host1 = self.get('h1')
        host2 = self.get('h2')
        host3 = self.get('h3')
        router1 = self.get('r1')
        router2 = self.get('r2')
        host1.setIP('192.168.1.1/24', intf='h1-eth0')
        host2.setIP('192.168.2.1/24', intf='h2-eth0')
        host3.setIP('192.168.3.1/24', intf='h3-eth0')
        router1.setIP('192.168.1.2/24', intf='r1-eth0')
        router1.setIP('10.0.1.0/24', intf='r1-eth1')
        router2.setIP('10.0.1.1/24', intf='r2-eth1')
        router2.setIP('192.168.2.2/24', intf='r2-eth2')
        router2.setIP('192.168.3.2/24', intf='r2-eth3')

        # Setting default routes for each interface
        h1.cmd('ip route add default via 192.168.1.2')
        h2.cmd('ip route add default via 192.168.2.2')
        h3.cmd('ip route add default via 192.168.3.2')


if __name__ == '__main__':
    Cleanup.cleanup()

    net = Net()

    for node in net:
        net[node].start_listener()

    CLI(net)
    net.stop()
