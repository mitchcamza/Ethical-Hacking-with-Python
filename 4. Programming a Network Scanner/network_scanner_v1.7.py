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


    # print the scan results:
    clients_list = []
    for element in answered_list: 
        client_dict = {"ip":element[1].psrc, "mac":element[1].hwsrc}  # create a dict for each element in the list
        clients_list.append(client_dict)                              # add the dict as an element in the list
        print(element[1].psrc + "\t\t" + element[1].hwsrc)                                                                                                           
    print(clients_list)

print_title()
scan("10.0.2.1/24")