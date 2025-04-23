
#!/usr/bin/env python
#Iterating Over Nested Data Structures

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
        
    return clients_list

def print_result(result_list):
    print("IP \t\t\tMac Address\n-----------------------------------------")
    for client in result_list:
        print(client["ip"]+ "\t\t" + client["mac"])
      
   
   

scan_result = scan("10.0.3.2/24")
print_result(scan_result)