# Python 3 has a std lib module for working with IP addresses:

import ipaddress

print(ipaddress.ip_address('192.168.1.2'))
# output: 192.168.1.2

print(ipaddress.ip_address('2001:af3::'))
# output: 2001:af3::

ipaddress.ip_address('2001:af3::')

# Learn more here: https://docs.python.org/3/library/ipaddress.html
