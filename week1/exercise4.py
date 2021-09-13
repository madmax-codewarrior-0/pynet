#!/usr/bin/python3

# The original version string
show_version = "*0      CISCO881-SEC-K9       FTX0000038X    "

# Split on all whitespace and assign model number and serial number variables
model_number, serial_number = show_version.split()[1], show_version.split()[2]

# Print if 'cisco' or '881' is in the model_number
print("'cisco' is in the model number: {}".format(model_number.lower().find('cisco') >= 0))
print("'881' is in the model number: {}".format(model_number.find('881') >= 0))

# Print the model number and serial number
print("\nModel: {}\nS/N: {}".format(model_number,serial_number))

