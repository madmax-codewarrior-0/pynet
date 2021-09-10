#!/usr/bin/python3
from __future__ import print_function, unicode_literals

ip_addr1 = '10.1.0.1'
ip_addr2 = '10.1.1.1'
ip_addr3 = '10.1.2.1'

# A fancy divider
divider = '#' * 80

# Formatted contents
contents = "{:<20}{:<20}{:<20}".format(ip_addr1,ip_addr2,ip_addr3)

# Concatenate everything into a single string object
full_thing = divider + "\n\n" + contents + "\n\n" + divider

# Print the string
print(full_thing)
