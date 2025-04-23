#!/usr/bin/env python
#Testing The Network Scanner With Python 3

import scapy.all as scapy
# import optparse
import argparse

def get_arguments():
    # parser = optparse.OptionParser()
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--target", dest="target", help = "Target IP / IP range.")
    options = parser.parse_args()
    return options

def scan(ip):...

def print_result(results_list):...

options = get_arguments()
scan_result = scan(options.target)
print_result(scan_result)