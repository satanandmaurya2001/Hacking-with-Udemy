#!/usr/bin/env python

import scapy.all as scapy

def scan (ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered, unanswered = scapy.srp(arp_request_broadcast, timeout=1)
    print(answered.summary())
    # print(unanswered.summary())
    
   
   

scan("10.0.3.2/24")