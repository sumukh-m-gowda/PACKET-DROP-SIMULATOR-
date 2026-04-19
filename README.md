report_with_screen_shot.pdf is not working in the github just download and view in ur system

# SDN Packet Drop Simulator using Mininet and POX

## Project Title
Packet Drop Simulator using Software Defined Networking (SDN)

## Overview
This project implements a Packet Drop Simulator using Software Defined Networking (SDN). 
The simulator demonstrates how network traffic can be monitored and selectively dropped 
using a centralized SDN controller.

Mininet is used to create the virtual network topology, Open vSwitch acts as the software 
switch, and a POX controller applies packet filtering rules.

The controller inspects packets and decides whether to allow or drop them based on 
predefined conditions.

---

## Objective

- Simulate network behavior using SDN
- Implement packet drop logic using controller rules
- Understand centralized traffic control
- Demonstrate selective packet filtering
- Test communication between hosts

---

## Technologies Used

- Software Defined Networking (SDN)
- Mininet
- POX Controller
- OpenFlow Protocol
- Open vSwitch (OVS)
- Python 3
- Linux (Ubuntu / Debian)

---

## System Architecture

Controller: POX Controller  
Switch: s1  

Hosts:

h1 → 10.0.0.1  
h2 → 10.0.0.2  
h3 → 10.0.0.3  
h4 → 10.0.0.4  

All hosts are connected to switch s1.  
Switch s1 connects to the POX controller.

---

## Project Components

### Mininet Topology

The topology creates:

- One OpenFlow switch
- Four hosts
- Links between hosts and switch
- Connection to remote controller

This simulates a real SDN network.

---

### POX Controller

The POX controller performs packet inspection and filtering.

It:

- Receives packets from switch
- Checks source and destination IP
- Applies packet drop rules
- Forwards allowed packets

---

## Packet Drop Rules

Rule 1:
All packets from host h3 (10.0.0.3) are dropped.

Result:
h3 cannot communicate with any host.

Rule 2:
ICMP packets (ping) from h1 (10.0.0.1) to h4 (10.0.0.4) are dropped.

Result:
Ping from h1 to h4 fails.

Rule 3:
All other packets are allowed and forwarded normally.

---

## Installation

Install required packages:

sudo apt update

sudo apt install -y python3 python3-pip git curl wget net-tools wireshark iperf3 tcpdump xterm mininet

Install POX:

git clone https://github.com/noxrepo/pox.git

cd pox

---

## Running the Project

Step 1: Start POX Controller

cd pox

./pox.py log.level --DEBUG packet_drop_simulator

Step 2: Run Mininet Topology

sudo python3 topology.py

---

## Test Cases

Run inside Mininet CLI.

Test 1:

h1 ping -c 4 h2

Expected Result:
0% packet loss

---

Test 2:

h3 ping -c 4 h2

Expected Result:
100% packet loss

---

Test 3:

h1 ping -c 4 h4

Expected Result:
100% packet loss

---

Test 4:

h2 ping -c 4 h4

Expected Result:
0% packet loss

---

## Expected Controller Output

Packet: 10.0.0.3 -> 10.0.0.2  
Dropping packet from h3  

Packet: 10.0.0.1 -> 10.0.0.4  
Dropping ICMP from h1 to h4  

---

## Features

- Centralized packet control
- Selective packet dropping
- Real-time packet inspection
- SDN-based filtering
- Virtual network simulation

---

## Applications

- Network security testing
- Firewall simulation
- Intrusion detection experiments
- Traffic filtering
- SDN learning and research

---

## Limitations

- Runs only in virtual environment
- Basic packet filtering
- Single switch topology

---

## Future Enhancements

- Multi-switch topology
- Dynamic rule updates
- Web-based monitoring
- Traffic visualization tools
- QoS and bandwidth management

---

## Conclusion

This project demonstrates how Software Defined Networking allows centralized 
control over network traffic. Using Mininet and POX, packet forwarding and 
dropping rules are applied dynamically, simulating firewall-like behavior 
in an SDN environment.
