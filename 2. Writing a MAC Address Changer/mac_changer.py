#!/usr/bin/env python

import subprocess   
import optparse     
import re

def get_arguments():
    """Gets arguments from the user"""
    parser = optparse.OptionParser()    
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")  
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")  
    (options, arguments) = parser.parse_args()
    
    # display an error message if no value is entered for the interface and new_mac
    if not options.interface:
        parser.error("[-] Please specify an interface. Use -- help for more info. ")    
    elif not options.new_mac:
        parser.error("[-] Please specify a new mac. Use -- help for more info. ")    
    return options


def change_mac(interface, new_mac):
    """Changes the MAC address for the specified interface"""
    print("[+] Changing MAC address for " + interface + " to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

# Get the interface and new MAC from the user and pass them to the change_mac function
options = get_arguments()  
change_mac(options.interface, options.new_mac)  

# check the ifconfig result for the selected interface to make sure that the MAC address was changed successfully
ifconfig_result = subprocess.check_output(["ifconfig", options.interface])
print(ifconfig_result)

# create a regex rule to search for the MAC address from the ifconfig result
mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)

# if a result was found
if mac_address_search_result:
    # print only the first occurrence of mac_address_search_result
    print(mac_address_search_result.group(0))
else:
    print("[-] Could not read MAC address.")
