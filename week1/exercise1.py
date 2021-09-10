from __future__ import print_function, unicode_literals

gateway1 = '10.1.0.1'
gateway2 = '10.1.1.1'
gateway3 = '10.1.2.1'

divider = '#' * 80

contents = "{:20}{:20}{:20}".format(gateway1,gateway2,gateway3)

full_thing = divider + "\n\n" + contents + "\n\n" + divider

print(full_thing)
