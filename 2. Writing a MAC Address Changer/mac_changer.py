#!/usr/bin/env python

import subprocess   
import optparse     

def get_arguments():
    """Gets arguments from the user"""
    parser = optparse.OptionParser()    
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")  
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")  
    return parser.parse_args()  # return the value that the parser returns


def change_mac(interface, new_mac):
    """Changes the MAC address for the specified interface"""
    print("[+] Changing MAC address for " + interface + " to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

# ***program execution begins here. First get_arguments is called, and then those values are used in the change_mac function call below ***
# declare a variable to store the value returned by get_arguments
(options, arguments) = get_arguments()  
change_mac(options.interface, options.new_mac)  
