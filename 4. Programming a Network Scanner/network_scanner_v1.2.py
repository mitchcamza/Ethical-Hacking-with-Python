#!/usr/bin/env python

import scapy.all as scapy

def scan(ip):
    arp_request = scapy.ARP(pdst = ip)  # create an instance of the scapy class
    print(arp_request.summary())        # calls a method in the ARP, implemented by scapy
    # scapy.ls(scapy.ARP())             # lists all the fileds that can be set
    

scan("10.0.0.2")