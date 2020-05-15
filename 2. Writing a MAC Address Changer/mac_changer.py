#!/usr/bin/env python

import subprocess   
import optparse     

"""
# create an instance of the optparse class to handle parsing arguments    
# note the case. As a convention in python, names that start with an uppercase are usually classes    
# variable dest stores the name of the interface provided
# the help option (--help, -h) is built in to optparse
# the message that is displayed when user askes for help is set below                            
"""
parser = optparse.OptionParser()    
parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")  
parser.parse_args()

interface = input("interface > " )
new_mac = input("new MAC > ")

print("[+] Changing MAC address for " + interface + " to " + new_mac)

subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
subprocess.call(["ifconfig", interface, "up"])


