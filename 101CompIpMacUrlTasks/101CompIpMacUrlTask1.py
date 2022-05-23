# James Taddei
# 101Computing IP, MAC, and URL Python Task #1
# 5/23/22

"""
    Description:
    Write a program to generate and output:
        A random IPv4 address
        A random IPv6 address
        A random MAC address

    https://www.101computing.net/ip-addresses-ipv4-ipv6-mac-addresses-urls/
"""

from random import randint

def main():
    print(create_random_IPv4())
    print(create_random_IPv6())
    print(create_random_MAC())

def create_random_IPv4():
    """
        Generates and returns a random IPv4 address.
    """

    ipv4 = ""
    for i in range(4): # creates the random numbers separated by periods
        ipv4 += str(randint(0,255)) + "."

    ipv4 = ipv4[0:len(ipv4)-1] # removes a period at the end of the string

    return ipv4

def create_random_IPv6():
    """
        Generates and returns a random IPv6 address.
    """

    ipv6 = ""
    for i in range(8): # creates 8 sets of 4 digit hexadecimal numbers separated by colons
        for j in range(4):
            ipv6 += random_hexa_value()

        ipv6 += ":" # separating colon

    ipv6 = ipv6[0:len(ipv6)-1] # removes a colon at the end of the string

    return ipv6

def create_random_MAC():
    """
        Generates and retuns a random MAC address.
    """

    mac = ""
    for i in range(6): # creates 6 sets of 2 digit hexadecimal numbers separated by colons
        for j in range(2):
            mac += random_hexa_value()

        mac += ":" # separating colon

    mac = mac[0:len(mac)-1]

    return mac

def random_hexa_value():
    """
        Generates and returns a random hexadecimal digit (with capital letters).
    """

    val = randint(0,15)
    if (val >= 10): # if the digit needs to be represented by a letter
        val = chr(55 + val)
        # 65 = a, offset so that 'val' of 10 = a

    return str(val)

main()
