import subprocess
import sys

# Set your wireless interface name here
INTERFACE = "wlan0"

def run_cmd(cmd):
    try:
        result = subprocess.run(cmd, shell=True, check=True, capture_output=True, text=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"[!] Command failed: {e.cmd}")
        print(e.stderr)

def enable_monitor_mode():
    print("[*] Killing interfering processes...")
    run_cmd("sudo airmon-ng check kill")

    print(f"[*] Switching {INTERFACE} to Monitor mode...")
    run_cmd(f"sudo ip link set {INTERFACE} down")
    run_cmd(f"sudo iw {INTERFACE} set type monitor")
    run_cmd(f"sudo ip link set {INTERFACE} up")

    print("[+] Monitor mode enabled.")
    run_cmd(f"iwconfig {INTERFACE}")

def disable_monitor_mode():
    print(f"[*] Switching {INTERFACE} to Managed mode...")
    run_cmd(f"sudo ip link set {INTERFACE} down")
    run_cmd(f"sudo iw {INTERFACE} set type managed")
    run_cmd(f"sudo ip link set {INTERFACE} up")

    print("[*] Restarting NetworkManager...")
    run_cmd("sudo service NetworkManager restart")

    print("[+] Managed mode enabled.")
    run_cmd(f"iwconfig {INTERFACE}")

def main():
    if len(sys.argv) != 2 or sys.argv[1] not in ["monitor", "managed"]:
        print("Usage: sudo python3 wifi_mode_switcher.py [monitor|managed]")
        sys.exit(1)

    mode = sys.argv[1]

    if mode == "monitor":
        enable_monitor_mode()
    elif mode == "managed":
        disable_monitor_mode()

if __name__ == "__main__":
    main()
