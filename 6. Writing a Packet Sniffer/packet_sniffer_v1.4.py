#!/usr/bin/env/python
# 3. Analysing sniffed packets and extracting fields from layers

import scapy.all as scapy
from scapy.layers import http

def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet)

def process_sniffed_packet(packet):
    if packet.haslayer(http.HTTPRequest):   # same as filter
        print(packet.show())

sniff("eth0")