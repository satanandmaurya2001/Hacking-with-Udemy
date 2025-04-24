# Handling Command-line Arguments
# Example usage from terminal:
# python3 mac_ch7.py --interface eth0 --mac 00:11:22:33:44:55
# This lets the user specify interface and new MAC address directly in the terminal.

#!/usr/bin/env python
# Tells the operating system to use the Python interpreter set in the environment for execution.

import subprocess
# Used to run system commands like "ifconfig" from within Python.

import optparse
# optparse is a module that allows you to build user-friendly command-line interfaces.
# It helps collect and process arguments like --interface and --mac.

parser = optparse.OptionParser()
# Creating an OptionParser object to handle command-line options.

parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
# This defines an option `-i` or `--interface` that stores its value in `interface`.
# The user uses this to specify the network interface (like eth0 or wlan0).

parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")
# This defines an option `-m` or `--mac` that stores its value in `new_mac`.
# This will be the new MAC address that the user wants to set.

(options, arguments) = parser.parse_args()
# This line parses the command-line arguments and separates them into `options` and `arguments`.
# `options` will hold values passed with --interface and --mac.

interface = options.interface
# Extracting the user-provided interface name from the parsed options.

new_mac = options.new_mac
# Extracting the user-provided new MAC address from the parsed options.

print("[+] changing MAC address for " + interface + " to " + new_mac)
# Informing the user about what the script is going to do.

# The following commands handle the MAC address change using subprocess.

subprocess.call(["ifconfig", interface, "down"])
# First, bring the interface down. This is necessary before changing the MAC address.

subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
# Change the MAC address to the user-specified value.

subprocess.call(["ifconfig", interface, "up"])
# Bring the interface back up to activate the new MAC address.

