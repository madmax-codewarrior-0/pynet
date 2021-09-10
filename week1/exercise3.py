#!/usr/bin/python3
#from __future__ import unicode_literals

ipvsix_addr_one = '2001:558:6025:14:44:b89f:e93b:dddd'
IPVSIX_ADDR_TWO = '::1'
ipv6_addr_3 = 'fe80::ec4:7aff:fe7a:326e'

print("\nipvsix_addr_one is equal to IPVSIX_ADDR_TWO?: {}\n".format(ipvsix_addr_one == IPVSIX_ADDR_TWO))
print("ipvsix_addr_one is not equal to ipv6_addr_3?: {}\n".format(ipvsix_addr_one != ipv6_addr_3))
