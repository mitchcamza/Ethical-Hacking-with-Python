#!/usr/bin/env python

import scapy.all as scapy

def scan(ip):
    arp_request = scapy.ARP(pdst = ip)                          # create an instance of the scapy class
    broadcast = scapy.Ether(dst = "ff:ff:ff:ff:ff:ff")          # create an Ethernet object from scapy and set the dest MAC to the broadcast MAC
    arp_request_broadcast = broadcast/arp_request               # combine the two above packets into one, using a forward slash
    answered, unanswered = scapy.srp(arp_request_broadcast, timeout=1)     # assign 2 variables to store the 2 values returned by the srp function              
                                                                # srp allows sending packets with a custom ether part
    print(answered.summary())       # show ip addresses in use
    print(unanswered.summary())     # show unused ip addresses

scan("10.0.2.1/24")