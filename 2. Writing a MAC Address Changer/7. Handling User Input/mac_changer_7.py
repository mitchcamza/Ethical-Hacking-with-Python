#!/usr/bin/env python

#creates a mac changer that runs on a linux terminal

import subprocess   #the subprocess module allows us to run system commands

interface = input("interface > " )
new_mac = input("new MAC > ")

print("[+] Changing MAC address for " + interface + " to " + new_mac)

# string method - risky. user can execute other commands via input
# subprocess.call("ifconfig " + interface + " down", shell = True)
# subprocess.call("ifconfig " + interface + " hw ether " + new_mac, shell = True)
# subprocess.call("ifconfig " + interface + " up", shell = True)

# list method - recommended to avoid hijacking of commands - more secure
subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
subprocess.call(["ifconfig", interface, "up"])


