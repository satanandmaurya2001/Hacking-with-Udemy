#Getting Input From the User
# MAC_CHANGER
#     HANDLING USER input
# --> Easiest way of getting user input is through keyboard.
# --> There are a number of ways to achieve that.
# --> input() function prompts the user to enter a value.ValueError

# Ex:
#     age=input("What is your age?")

# Result
#     What is your age?

# The variable age will hold the value of the user input


#!/usr/bin/env python

import subprocess

interface = input ("interface > ")
new_mac = input (" new_mac >")

print("[+] changing MAC address for " + interface + " to " + new_mac)

subprocess.call("ifconfig " + interface + " down",shell=True)
subprocess.call("ifconfig " + interface + " hw ether " + new_mac, shell=True)
subprocess.call("ifconfig " + interface + " up",shell=True)