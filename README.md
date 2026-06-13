# MAC Address Changer

A Python-based MAC address changer for Linux that automates network interface configuration and verifies successful changes.

## Features

- Change the MAC address of a specified network interface
- Verify that the MAC address was successfully changed
- Command-line argument support
- Input validation for MAC addresses
- Error handling and status messages
- Beginner-friendly code for learning networking and cybersecurity concepts

## Requirements

- Python 3
- Linux operating system
- Root privileges (sudo)
- ifconfig utility installed

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/mac-address-changer.git
cd mac-address-changer
```

## Usage

```bash
sudo python3 mac_changer.py -i eth0 -m 00:11:22:33:44:55
```

### Arguments

| Argument | Description |
|-----------|-------------|
| `-i` | Network interface |
| `-m` | New MAC address |

### Example

```bash
sudo python3 mac_changer.py -i wlan0 -m 00:11:22:33:44:55
```

## Sample Output

```text
[+] Current MAC address: 08:00:27:12:34:56
[+] Changing MAC address for wlan0 to 00:11:22:33:44:55
[+] MAC address has changed successfully
[+] New MAC address: 00:11:22:33:44:55
```

## Educational Purpose

This project was created as part of my cybersecurity learning journey to better understand:

- MAC Address Spoofing
- Linux Networking
- Python Scripting
- Regular Expressions
- Subprocess Management
- Command-Line Tools

## Disclaimer

This project is intended for educational and authorized testing purposes only. Users are responsible for complying with all applicable laws, regulations, and organizational policies.

## Author

Mahmoud Ediem

GitHub: @mahmoudediem4
