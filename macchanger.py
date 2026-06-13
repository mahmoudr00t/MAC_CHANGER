import subprocess
import optparse
import re
import os


def get_arguments():
    parser = optparse.OptionParser()

    parser.add_option("-i", "--interface", dest="network_interface",
                      help="Network interface to change")

    parser.add_option("-m", "--mac", dest="new_mac",
                      help="New MAC address")

    options, arguments = parser.parse_args()

    if not options.network_interface:
        parser.error("[-] Please specify a network interface. Use -h for help.")

    if not options.new_mac:
        parser.error("[-] Please specify a new MAC address. Use -h for help.")

    if not is_valid_mac(options.new_mac):
        parser.error("[-] Invalid MAC address format. Example: 00:11:22:33:44:55")

    return options


def is_valid_mac(mac):
    return re.fullmatch(r"([0-9a-fA-F]{2}:){5}[0-9a-fA-F]{2}", mac) is not None


def check_root():
    if os.geteuid() != 0:
        print("[-] Please run this program with sudo.")
        print("Example: sudo python3 mac_changer.py -i eth0 -m 00:11:22:33:44:55")
        exit()


def run_command(command):
    result = subprocess.call(command, shell=True)

    if result != 0:
        print("[-] Command failed: " + command)
        exit()


def get_mac(network_interface):
    try:
        ifconfig_result = subprocess.check_output(
            "ifconfig " + network_interface,
            shell=True
        ).decode("utf-8")
    except subprocess.CalledProcessError:
        print("[-] Could not read interface: " + network_interface)
        return None

    mac_address = re.search(
        r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",
        ifconfig_result
    )

    if mac_address:
        return mac_address.group(0)

    return None


def mac_changer(network_interface, new_mac):
    print("[+] Changing MAC address for " + network_interface + " to " + new_mac)

    run_command("ifconfig " + network_interface + " down")
    run_command("ifconfig " + network_interface + " hw ether " + new_mac)
    run_command("ifconfig " + network_interface + " up")


check_root()

options = get_arguments()

old_mac = get_mac(options.network_interface)

if old_mac:
    print("[+] Current MAC address: " + old_mac)
else:
    print("[-] Could not find current MAC address.")

mac_changer(options.network_interface, options.new_mac)

current_mac = get_mac(options.network_interface)

if current_mac == options.new_mac:
    print("[+] MAC address has changed successfully")
    print("[+] New MAC address: " + current_mac)
else:
    print("[-] Something went wrong...")
    print("[-] Current MAC address: " + str(current_mac))