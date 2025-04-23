#!/usr/bin/env python

import subprocess
import optparse

parser = optparse.OptionParser()

parser.add_option("-i", "--interface", dest="interface", help="Interface to change its Mac address")
parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")

(options, arguments)=parser.parse_args()

# interface = "eth0"
# new_mac = "00:11:22:33:44:88"

# interface = input("interface>")
# new_mac = input("new MAC > ")

interface = options.interface
new_mac = options.new_mac

print("[+] Changing MAC address for " + interface + " to " + new_mac)

# subprocess.call("ifconfig " + interface + " down", shell=True)     
# subprocess.call("ifconfig " + interface + " hw ether" +new_mac, shell=True) 
# subprocess.call("ifconfig " + interface + " up", shell=True) 

# subprocess.call(["ifconfig ",interface, " down"])     
subprocess.call(["ip", "link", "set",interface, "down"]) 
subprocess.call(["ip", "link", "set",interface, "address" ,new_mac]) 
subprocess.call(["ip", "link", "set",interface, "up"] ) 