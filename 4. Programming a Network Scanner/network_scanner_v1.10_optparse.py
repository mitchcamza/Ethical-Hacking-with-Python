#!/usr/bin/env python

import scapy.all as scapy
import optparse             # optparse has depreciated, but still works
                            # argparse is the successor to optparse


def get_argument():
    parser = optparse.OptionParser()
    parser.add_option("-t", "--target", dest="target", help="Target IP/ IP range.")
    (options, arguments) = parser.parse_args()
    return options


def scan(ip):
    """ perform the network scan and return the result """
    arp_request = scapy.ARP(pdst = ip)                                  # create an instance of the scapy class
    broadcast = scapy.Ether(dst = "ff:ff:ff:ff:ff:ff")                  # create an Ethernet object from scapy and set the dest MAC to the broadcast MAC
    arp_request_broadcast = broadcast/arp_request                       # combine the two above packets into one, using a forward slash
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]  # only store the answered requests as a list ([0] represents the answered list element)
    
    clients_list = []
    for element in answered_list: 
        client_dict = {"ip":element[1].psrc, "mac":element[1].hwsrc}    # create a dict for each element in the list
        clients_list.append(client_dict)                                # add the dict as an element in the list                                                                                                           
    return clients_list


def print_result(results_list):
    """ prints the scan results """
    
    # print the heading
    print("_______________________________________________________")
    print("IP\t\t\tMAC Address")
    print("-------------------------------------------------------")

    # print the results
    for client in results_list:
        print(client["ip"] + "\t\t" + client["mac"])


options = get_argument()
scan_result = scan(options.target)  # call the scan function and assign it to a variable named scan_result
print_result(scan_result)           # call the print_result function and pass the scan result function as an argument
