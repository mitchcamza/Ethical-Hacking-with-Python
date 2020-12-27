#!/usr/bin/env python

# 9. Initialising Variables Based on Command-line Arguments

#creates a mac changer that runs on a linux terminal

import subprocess   
import optparse     # allows arguments to be specified by the user 

"""
# create an instance of the optparse class to handle parsing arguments    
# note the case. As a convention in python, names that start with an uppercase are usually classes    
# variable dest stores the name of the interface provided
# the help option (--help, -h) is built in to optparse
# the message that is displayed when user askes for help is set below                            
"""
parser = optparse.OptionParser()    

parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")  
parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")  
(options, arguments) = parser.parse_args() #goes through all user-input and separates arguments from values (options) provided (-i is an argument and wlano is a value)

interface = options.interface
new_mac = options.new_mac

print("[+] Changing MAC address for " + interface + " to " + new_mac)

subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
subprocess.call(["ifconfig", interface, "up"])


