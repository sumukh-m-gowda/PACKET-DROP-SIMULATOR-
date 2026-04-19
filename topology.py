#!/usr/bin/env python3

from mininet.net import Mininet
from mininet.node import RemoteController, OVSKernelSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink


def create_topology():

    setLogLevel('info')

    net = Mininet(
        controller=RemoteController,
        switch=OVSKernelSwitch,
        link=TCLink
    )

    info('*** Adding controller\n')

    c0 = net.addController(
        'c0',
        controller=RemoteController,
        ip='127.0.0.1',
        port=6633
    )

    info('*** Adding switch\n')

    s1 = net.addSwitch('s1')

    info('*** Adding hosts\n')

    h1 = net.addHost('h1', ip='10.0.0.1/24')
    h2 = net.addHost('h2', ip='10.0.0.2/24')
    h3 = net.addHost('h3', ip='10.0.0.3/24')
    h4 = net.addHost('h4', ip='10.0.0.4/24')

    info('*** Adding links\n')

    net.addLink(h1, s1)
    net.addLink(h2, s1)
    net.addLink(h3, s1)
    net.addLink(h4, s1)

    info('*** Starting network\n')

    net.start()

    CLI(net)

    net.stop()


if __name__ == '__main__':
    create_topology()
