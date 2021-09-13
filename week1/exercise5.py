#!/usr/bin/python3

# The originally given router arp table
arp1 = "Internet  10.220.88.29           94   5254.abbe.5b7b  ARPA   FastEthernet4"
arp2 = "Internet  10.220.88.30            3   5254.ab71.e119  ARPA   FastEthernet4"
arp3 = "Internet  10.220.88.32          231   5254.abc7.26aa  ARPA   FastEthernet4"

# Print the header and divider
print("{:>20}{:>20}".format("IP ADDR","MAC ADDRESS"))
print(("-" * 20) + " " + ("-" * 20))

# For each arp in the table, print the IP (position 2) 
# and the MAC address (position 4)
for binding in (arp1,arp2,arp3):
    print("{:>20}{:>20}".format(binding.split()[1],binding.split()[3]))
