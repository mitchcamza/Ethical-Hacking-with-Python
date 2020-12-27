#!/usr/bin/env python

import subprocess   
import optparse     

# 10. Define a function called change_mac with two parameters, and move the code to the body of the function.

def change_mac(interface, new_mac):
    print("[+] Changing MAC address for " + interface + " to " + new_mac)

    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

parser = optparse.OptionParser()    

parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")  
parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")  

# go through all user-input and separates arguments from values (options) provided (-i is an argument and wlan0 is a value)
(options, arguments) = parser.parse_args() 

# variables below store the values for the interface and new mac entered by the user (no longer required after change_mac function definition)
# interface = options.interface
# new_mac = options.new_mac

# call the change_mac function with the values for interface and new_mac as arguments
change_mac(options.interface, options.new_mac)  





