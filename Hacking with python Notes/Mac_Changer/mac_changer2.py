#!/usr/bin/env python3

import subprocess
import argparse

def change_mac(interface, new_mac):
    print(f"[+] Changing MAC address for {interface} to {new_mac}")

    subprocess.call(["sudo", "ip", "link", "set", interface, "down"])
    subprocess.call(["sudo", "ip", "link", "set", interface, "address", new_mac])
    subprocess.call(["sudo", "ip", "link", "set", interface, "up"])

def get_arguments():
    parser = argparse.ArgumentParser(description="MAC Address Changer")
    parser.add_argument("-i", "--interface", required=True, help="Network interface (e.g., eth0, wlan0)")
    parser.add_argument("-m", "--mac", required=True, help="New MAC address (e.g., 00:11:22:33:44:88)")
    return parser.parse_args()

if __name__ == "__main__":
    args = get_arguments()
    change_mac(args.interface, args.mac)
