#!/usr/bin/env python3
# 1. Create an ARP response


import scapy.all as scapy

# create the ARP Packet
    # for op=2, the packet that is sent is considered to be a response
    # pdst = target IP
    # hwdst = target MAC
    # psrc = router's IP
packet = scapy.ARP(op=2, pdst="10.0.2.15", hwdst="08:00:27:7b:f0:25", psrc="10.0.2.1")



