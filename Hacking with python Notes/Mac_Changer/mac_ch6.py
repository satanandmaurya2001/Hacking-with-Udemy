#Handling User Input

#!/usr/bin/env python

import subprocess

interface = input ("interface > ")
new_mac = input (" new_mac >")

print("[+] changing MAC address for " + interface + " to " + new_mac)


# This command is more secure than previous 
subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
subprocess.call(["ifconfig", interface, "up"])