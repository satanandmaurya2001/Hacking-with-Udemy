#!/usr/bin/env python

import subprocess
import optparse

def change_mac(interface, new_mac):
    print("[+] Changing MAC address for " + interface + " to " + new_mac)

  
    subprocess.call(["ip", "link", "set",interface, "down"]) 
    subprocess.call(["ip", "link", "set",interface, "address" ,new_mac]) 
    subprocess.call(["ip", "link", "set",interface, "up"] ) 


parser = optparse.OptionParser()

parser.add_option("-i", "--interface", dest="interface", help="Interface to change its Mac address")
parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")

(options, arguments)=parser.parse_args()


change_mac(options.interface, options.new_mac)

