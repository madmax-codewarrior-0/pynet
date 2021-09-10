#!/usr/bin/python3
from __future__ import print_function


# Let's validate the user's input first
try:
    # Python3 has a handy built in library we can leverage
    import ipaddress
except ImportError:
    # Python 2.7 doesn't, so let's define our own IP address 
    # validation function - True if a valid IP, False if not
    def correct_ipaddress(addr):
        # Need exactly four octets in the string
        if len(addr.split('.')) != 4:
            return False
        # For each octet
        for i in addr.split('.'):
            # Confirm if the string object is an represented integer
            if not i.isdigit():
                return False
            # If it is, cast it to an integer
            i = int(i)
            # Validdate the int is greater than 0 and less than 256
            if i < 0 or i > 255:
                return False
        return True

# Accepting user input now that we're ready
try: 
    # Python2.7 - raw_input throws exception in Python3
    user_ip_addr = raw_input("Enter a valid IP address: ")

    # Use our previously defined IP address validator
    if not correct_ipaddress(user_ip_addr):
        print("\n{} is an invalid IP address".format(user_ip_addr))
        exit()
except NameError:
    # Python3
    user_ip_addr = input("Enter a valid IP address: ")

    try:
        # This will attempt to convert the string to a valid IPv4 or IPv6 address
        # An exception is thrown if it isn't a valid IP
        valid_ip = ipaddress.ip_address(user_ip_addr)
        # Now check if it's an IPv4 address
        if valid_ip.version != 4:
            print("\nWe're not doing IPv6 addresses at this time!")
            exit()
    except ValueError:
        print("\n{} is an invalid IP address".format(user_ip_addr))
        exit()

# Passed all checks for 2.7 and 3
# Build the formatted output

header = "{:^15}{:^15}{:^15}{:^15}".format("Octet1","Octet2","Octet3","Octet4")
divider = "_" * (15 * 4)

# Create a list from the following: the output of mapping the 
# function int() over the list created by splitting the input user 
# IP adddress on '.', effectively typecasting each octet to an int
octet_list_dec = list(map(int,(user_ip_addr.split('.'))))

# Print header and divider
print("\n" + header + "\n" + divider + "\n")

# Print the decimal octets
print("{:^15}{:^15}{:^15}{:^15}".format(*octet_list_dec))

# Print the binary octets - here we map the bin() function over the decimal list
# while still splatting the list
print("{:^15}{:^15}{:^15}{:^15}".format(*(map(bin,octet_list_dec))))

# Print the binary octets - again we map the hex() function over the decimal list
print("{:^15}{:^15}{:^15}{:^15}".format(*(map(hex,octet_list_dec))))

# Print another divider
print(divider)
