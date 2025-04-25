# Handling Command-line Arguments
# python3 mac_ch7.py --interface eth0 --mac 00:11:22:33:44:55

# Initialising Variables Based on Command-line Arguments

#!/usr/bin/env python

import subprocess
import optparse #it allow you get argument from the user and parse them

parser = optparse.OptionParser()

parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")


(options, arguments) = parser.parse_args()

interface = options.interface
new_mac = options.new_mac

print("[+] changing MAC address for " + interface + " to " + new_mac)


# This command is more secure than previous 
subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
subprocess.call(["ifconfig", interface, "up"])




