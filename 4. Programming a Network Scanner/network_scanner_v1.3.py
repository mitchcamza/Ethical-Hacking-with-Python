#!/usr/bin/env python

import scapy.all as scapy

def scan(ip):
    arp_request = scapy.ARP(pdst = ip)                 # create an instance of the scapy class
    # arp_request.show()                                 # shows the details of the specified packet 
    broadcast = scapy.Ether(dst = "ff:ff:ff:ff:ff:ff") # create an Ethernet object from scapy and set the dest MAC to the broadcast MAC
    broadcast.show()
    arp_request_broadcast = broadcast/arp_request      # combine the two above packets into one, using a forward slash
    # arp_request_broadcast.show()
    

scan("10.0.0.1/24")