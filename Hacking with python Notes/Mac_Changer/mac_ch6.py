# Handling User Input

#!/usr/bin/env python
# This line tells the system to run the script with the default Python interpreter set in the environment.
# Useful in Linux for executing the script directly from the terminal.

import subprocess
# Importing the subprocess module allows us to run system-level commands like 'ifconfig' from within Python.

interface = input("interface > ")
# Taking input from the user for the name of the network interface (e.g., eth0, wlan0).
# Example: eth0, wlan0 – which are typically used in networking.

new_mac = input("new_mac > ")
# Asking the user to input the new MAC address that they want to assign to the interface.
# A MAC address is a unique identifier assigned to a network interface.

print("[+] changing MAC address for " + interface + " to " + new_mac)
# Displaying the action that is going to be taken – helpful for user confirmation.

# The following commands change the MAC address using system tools via subprocess.

subprocess.call(["ifconfig", interface, "down"])
# This disables the network interface before changing the MAC address.
# Required because most systems don't allow MAC address changes while the interface is up.

subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
# This changes the MAC address of the specified interface.
# 'hw ether' is used to specify the new hardware (MAC) address.

subprocess.call(["ifconfig", interface, "up"])
# This re-enables the network interface after changing the MAC address.

