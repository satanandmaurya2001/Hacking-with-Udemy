#!/usr/bin/env python

import subprocess
import optparse

def get_arguments():
    parser = optparse.OptionParser()

    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its Mac address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")
    return parser.parse_args()
    (options, arguments)=parser.parse_args()
    if not options.inteface:
        parser.error("[ .] Please specify an interface, use --help for more info.")#code to to handle error
    elif not options.new_mac:
        parser.error("[ .] Please specify an new mac, use --help for more info.")#code to handle error
    return options

def change_mac(interface, new_mac):
    print("[+] Changing MAC address for " + interface + " to " + new_mac)

  
    subprocess.call(["ip", "link", "set",interface, "down"]) 
    subprocess.call(["ip", "link", "set",interface, "address" ,new_mac]) 
    subprocess.call(["ip", "link", "set",interface, "up"] ) 


# parser = optparse.OptionParser()

# parser.add_option("-i", "--interface", dest="interface", help="Interface to change its Mac address")
# parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")

# (options, arguments)=parser.parse_args()


# interface = options.interface
# new_mac = options.new_mac
# (options, get_arguments) = get_arguments
options = get_arguments()
change_mac(options.interface, options.new_mac)

