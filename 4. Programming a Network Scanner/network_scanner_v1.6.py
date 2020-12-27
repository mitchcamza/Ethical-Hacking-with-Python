#!/usr/bin/env python

import scapy.all as scapy

def print_title():
    """ print the heading """
    print("_______________________________________________________")
    print("IP\t\t\tMAC Address")
    print("-------------------------------------------------------")

def scan(ip):
    """ perform the network scan """
    arp_request = scapy.ARP(pdst = ip)                          # create an instance of the scapy class
    broadcast = scapy.Ether(dst = "ff:ff:ff:ff:ff:ff")          # create an Ethernet object from scapy and set the dest MAC to the broadcast MAC
    arp_request_broadcast = broadcast/arp_request               # combine the two above packets into one, using a forward slash
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]  # only store the answered requests as a list ([0] represents the answered list element)


    # print each element in the answered_list
    for element in answered_list:   
        # only print the answer part of the list (index pos 1) 
        # print(element[1].show())  # shows all the fields available to print
        # print the client source ip and MAC 
        print(element[1].psrc + "\t\t" + element[1].hwsrc)                                                                                                           
        


print_title()
scan("10.0.2.1/24")