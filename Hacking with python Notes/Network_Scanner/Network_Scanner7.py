
#!/usr/bin/env python
#Improving the Program Using a List of Dictionaries in Python

import scapy.all as scapy

def scan (ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list= scapy.srp(arp_request_broadcast, timeout=1, verbose = False)[0]
   
    print("IP\t\t\t\t\t\tMac Address\n-------------------------------------------------")
    clients_list = []
    for element in answered_list:
        client_dict = {"ip" : element[1].psrc , "mac" : element[1].hwsrc}
        clients_list.append(client_dict)
        print(element[1].psrc + "\t\t" + element[1].hwsrc)
    print(clients_list)    
    print("--------------------------------------------------------------")

   
    
   
   

scan("10.0.3.2/24")