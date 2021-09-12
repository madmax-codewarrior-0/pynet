#!/usr/bin/python3

show_version = "*0      CISCO881-SEC-K9       FTX0000038X    "

show_version_ntws = show_version.strip()

model_number = show_version.split()[1]
serial_number = show_version.split()[2]

print("'cisco' is in the model number: {}".format(model_number.lower().find('cisco') >= 0))
print("'881' is in the model number: {}".format(model_number.find('881') >= 0))

print("\nModel: {}\nS/N: {}".format(model_number,serial_number))

