#!/usr/bin/python3
from mininet.net import Mininet
from mininet.log import setLogLevel, info
from mininet.cli import CLI
from mininet.clean import Cleanup
from node import MyHost


class ExampleNet1(Mininet):
    def __init__(self):
        Mininet.__init__(self, controller=None, cleanup=True)

        # Creating Hosts
        info("*** Creating routers\n")
        r1 = self.addHost('r1', cls=MyHost, ip='10.0.1.1/24', port='8888', id=1, staticRP=True)
        r2 = self.addHost('r2', cls=MyHost, ip='10.0.1.2/24', port='8888', id=2)
        r3 = self.addHost('r3', cls=MyHost, ip='10.0.2.2/24', port='8888', id=3)
        r4 = self.addHost('r4', cls=MyHost, ip='10.0.4.1/24', port='8888', id=4)
        r5 = self.addHost('r5', cls=MyHost, ip='10.0.4.2/24', port='8888', id=5)
        r6 = self.addHost('r6', cls=MyHost, ip='10.0.3.2/24', port='8888', id=6)
        r7 = self.addHost('r7', cls=MyHost, ip='10.0.7.1/24', port='8888', id=7)
        r8 = self.addHost('r8', cls=MyHost, ip='10.0.7.2/24', port='8888', id=8)
        r9 = self.addHost('r9', cls=MyHost, ip='10.0.6.2/24', port='8888', id=9)

        info("*** Creating hosts\n")
        h1 = self.addHost('h1', cls=MyHost, ip='192.168.1.1/24', defaultRoute='via 192.168.1.2/24')
        h2 = self.addHost('h2', cls=MyHost, ip='192.168.2.1/24', defaultRoute='via 192.168.2.2/24')
        h3 = self.addHost('h3', cls=MyHost, ip='192.168.3.1/24', defaultRoute='via 192.168.3.2/24')

        # Establishing the links from hosts to routers
        info("*** Creating links\n")
        self.addLink(r1, r2, intfName1='r1-eth0', intfName2='r2-eth0')
        self.addLink(r2, r3, intfName1='r2-eth1', intfName2='r3-eth0')
        self.addLink(r3, h1, intfName1='r3-eth1', intfName2='h1-eth0')
        self.addLink(r3, r6, intfName1='r3-eth2', intfName2='r6-eth0')
        self.addLink(r4, r5, intfName1='r4-eth0', intfName2='r5-eth0')
        self.addLink(r5, r6, intfName1='r5-eth1', intfName2='r6-eth1')
        self.addLink(r6, h2, intfName1='r6-eth2', intfName2='h2-eth0')
        self.addLink(r6, r9, intfName1='r6-eth3', intfName2='r9-eth0')
        self.addLink(r7, r8, intfName1='r7-eth0', intfName2='r8-eth0')
        self.addLink(r8, r9, intfName1='r8-eth1', intfName2='r9-eth1')
        self.addLink(r9, h3, intfName1='r9-eth2', intfName2='h3-eth0')

        # Setting interface ip addresses since params1 or params2 just will not work
        info("*** Initializing IPs\n")
        r2.setIP('10.0.2.1/24', intf='r2-eth1')

        r3.setIP('10.0.3.1/24', intf='r3-eth2')

        r5.setIP('10.0.5.1/24', intf='r5-eth1')

        r6.setIP('10.0.5.2/24', intf='r6-eth1')
        r6.setIP('10.0.6.1/24', intf='r6-eth3')

        r8.setIP('10.0.8.1/24', intf='r8-eth1')

        r9.setIP('10.0.8.2/24', intf='r9-eth1')

        r3.setIP('192.168.1.2/24', intf='r3-eth1')
        r6.setIP('192.168.2.2/24', intf='r6-eth2')
        r9.setIP('192.168.3.2/24', intf='r9-eth2')


class ExampleNet2(Mininet):
    def __init__(self):
        Mininet.__init__(self, controller=None, cleanup=True)

        # Creating Hosts
        info("*** Creating routers\n")
        r1 = self.addHost('r1', cls=MyHost, ip='10.0.1.1/24')
        r2 = self.addHost('r2', cls=MyHost, ip='10.0.1.2/24')
        r3 = self.addHost('r3', cls=MyHost, ip='10.0.1.3/24')
        r4 = self.addHost('r4', cls=MyHost, ip='10.0.1.4/24')
        r5 = self.addHost('r5', cls=MyHost, ip='10.0.2.2/24')
        r6 = self.addHost('r6', cls=MyHost, ip='10.0.3.2/24')
        r7 = self.addHost('r7', cls=MyHost, ip='10.0.4.2/24')

        info("*** Creating hosts\n")
        h1 = self.addHost('h1', cls=MyHost, ip='192.168.1.1/24', defaultRoute='via 192.168.1.2/24')
        h2 = self.addHost('h2', cls=MyHost, ip='192.168.2.1/24', defaultRoute='via 192.168.2.2/24')
        h3 = self.addHost('h3', cls=MyHost, ip='192.168.3.1/24', defaultRoute='via 192.168.3.2/24')
        h4 = self.addHost('h4', cls=MyHost, ip='192.168.4.1/24', defaultRoute='via 192.168.4.2/24')

        # Establishing the links from hosts to routers
        info("*** Creating links\n")
        self.addLink(r1, r2, intfName1='r1-eth0', intfName2='r2-eth0')
        self.addLink(r1, r3, intfName1='r1-eth1', intfName2='r3-eth0')
        self.addLink(r1, r4, intfName1='r1-eth2', intfName2='r4-eth0')
        self.addLink(r2, r5, intfName1='r2-eth1', intfName2='r5-eth0')
        self.addLink(r3, r6, intfName1='r3-eth1', intfName2='r6-eth0')
        self.addLink(r4, r7, intfName1='r4-eth1', intfName2='r7-eth0')
        self.addLink(r5, r6, intfName1='r5-eth1', intfName2='r6-eth1')
        self.addLink(r6, r7, intfName1='r6-eth3', intfName2='r7-eth1')

        self.addLink(r1, h1, intfName1='r1-eth3', intfName2='h1-eth0')
        self.addLink(r5, h2, intfName1='r5-eth2', intfName2='h2-eth0')
        self.addLink(r6, h3, intfName1='r6-eth2', intfName2='h3-eth0')
        self.addLink(r7, h4, intfName1='r7-eth2', intfName2='h4-eth0')

        # Setting interface ip addresses since params1 or params2 just will not work
        info("*** Initializing IPs\n")
        r2.setIP('10.0.2.1/24', intf='r2-eth1')
        r3.setIP('10.0.3.1/24', intf='r3-eth1')
        r4.setIP('10.0.4.1/24', intf='r4-eth1')

        r5.setIP('10.0.5.1/24', intf='r5-eth1')
        r6.setIP('10.0.5.2/24', intf='r6-eth1')
        r6.setIP('10.0.6.1/24', intf='r6-eth3')
        r7.setIP('10.0.6.2/24', intf='r7-eth1')

        r1.setIP('192.168.1.2/24', intf='r1-eth3')
        r5.setIP('192.168.2.2/24', intf='r5-eth2')
        r6.setIP('192.168.3.2/24', intf='r6-eth2')
        r7.setIP('192.168.4.2/24', intf='r7-eth2')


class ExampleNet3(Mininet):
    def __init__(self):
        Mininet.__init__(self, controller=None, cleanup=True)

        # Creating Hosts
        info("*** Creating routers\n")
        r1 = self.addHost('r1', cls=MyHost, ip='10.0.1.1/24')
        r2 = self.addHost('r2', cls=MyHost, ip='10.0.1.3/24')
        r3 = self.addHost('r3', cls=MyHost, ip='10.0.1.4/24')
        r4 = self.addHost('r4', cls=MyHost, ip='10.0.4.1/24')
        r5 = self.addHost('r5', cls=MyHost, ip='10.0.3.2/24')
        r6 = self.addHost('r6', cls=MyHost, ip='10.0.5.2/24')

        info("*** Creating hosts\n")
        h1 = self.addHost('h1', cls=MyHost, ip='192.168.1.1/24', defaultRoute='via 192.168.1.2/24')
        h2 = self.addHost('h2', cls=MyHost, ip='192.168.2.1/24', defaultRoute='via 192.168.2.2/24')
        h3 = self.addHost('h3', cls=MyHost, ip='192.168.3.1/24', defaultRoute='via 192.168.3.2/24')
        h4 = self.addHost('h4', cls=MyHost, ip='192.168.4.1/24', defaultRoute='via 192.168.4.2/24')

        # Establishing the links from hosts to routers
        info("*** Creating links\n")
        self.addLink(r1, r2, intfName1='r1-eth0', intfName2='r2-eth0')
        self.addLink(r1, r3, intfName1='r1-eth1', intfName2='r3-eth0')
        self.addLink(r2, r4, intfName1='r2-eth1', intfName2='r4-eth0')
        self.addLink(r3, r4, intfName1='r3-eth1', intfName2='r4-eth1')
        self.addLink(r3, r5, intfName1='r3-eth2', intfName2='r5-eth0')
        self.addLink(r5, r6, intfName1='r5-eth1', intfName2='r6-eth0')

        self.addLink(r1, h1, intfName1='r1-eth2', intfName2='h1-eth0')
        self.addLink(r4, h2, intfName1='r4-eth2', intfName2='h2-eth0')
        self.addLink(r6, h3, intfName1='r6-eth1', intfName2='h3-eth0')
        self.addLink(r6, h4, intfName1='r6-eth2', intfName2='h4-eth0')

        # Setting interface ip addresses since params1 or params2 just will not work
        info("*** Initializing IPs\n")
        r4.setIP('10.0.4.2/24', intf='r4-eth1')
        r2.setIP('10.0.4.3/24', intf='r2-eth1')
        r1.setIP('10.0.1.2/24', intf='r1-eth1')
        r3.setIP('10.0.4.4/24', intf='r3-eth1')

        r3.setIP('10.0.3.1/24', intf='r3-eth2')
        r5.setIP('10.0.5.1/24', intf='r5-eth1')

        r1.setIP('192.168.1.2/24', intf='r1-eth2')
        r4.setIP('192.168.2.2/24', intf='r4-eth2')
        r6.setIP('192.168.3.2/24', intf='r6-eth1')
        r6.setIP('192.168.4.2/24', intf='r6-eth2')


if __name__ == '__main__':
    setLogLevel('info')

    Cleanup.cleanup()

    net = ExampleNet3()
    net.build()
    net.start()

    # Start listener on all routers and clients
    for node in net.hosts:
        node.start_listener()
        if node.isStaticRP():
            node.staticRPRoutine()

    # Learn topo/djititjariasdj algortithm

    # Send multicast packet from host

    # whatever else

    CLI(net)
    net.stop()
