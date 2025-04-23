#!/usr/bin/env python
#Improving the Program Using a Escape Characters

import scapy.all as scapy

def scan (ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list= scapy.srp(arp_request_broadcast, timeout=1, verbose = False)[0]
   
    print("IP\t\t\t\t\t\tMac Address\n-------------------------------------------------")

    for element in answered_list:
        # print(element[1].show())
        print(element[1].psrc + "\t\t" + element[1].hwsrc)
        
        print("--------------------------------------------------------------")

   
    
   
   

scan("10.0.3.2/24")