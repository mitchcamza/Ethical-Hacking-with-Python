#!/usr/bin/env python

import scapy.all as scapy

def scan(ip):
    arp_request = scapy.ARP(pdst = ip)                          # create an instance of the scapy class
    broadcast = scapy.Ether(dst = "ff:ff:ff:ff:ff:ff")          # create an Ethernet object from scapy and set the dest MAC to the broadcast MAC
    arp_request_broadcast = broadcast/arp_request               # combine the two above packets into one, using a forward slash
    answered_list = scapy.srp(arp_request_broadcast, timeout=1)[0]  # only store the answered requests as a list ([0] represents the answered list element)

    for element in answered_list:   # print each element in the answered_list
        # only print the answer part of the list (index pos 1) 
        # print(element[1].show())  # shows all the fields available to print
        print(element[1].psrc)      # print the client source ip                                                     
        print(element[1].hwsrc)     # print the client source MAC                                                     
        print("--------------------------------------------------")

scan("10.0.2.1/24")