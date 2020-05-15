#!/usr/bin/env python

import subprocess   
import optparse     


def change_mac(interface, new_mac):
    """Changes the MAC address for the specified interface"""

    print("[+] Changing MAC address for " + interface + " to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])


parser = optparse.OptionParser() 
parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")  
parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")  
(options, arguments) = parser.parse_args() 

# variables below store the values for the interface and new mac entered by the user (no longer required after change_mac function definition)
# interface = options.interface
# new_mac = options.new_mac

# call the change_mac function with the values for interface and new_mac as arguments
change_mac(options.interface, options.new_mac)  
