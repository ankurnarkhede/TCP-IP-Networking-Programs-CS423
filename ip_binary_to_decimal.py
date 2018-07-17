# program to convert dotted binary ip address to decimal

import sys
import re

def to_decimal(ip):
    return '.'.join ([str (int (ip[i*8:(i*8)+8], 2)) for i in range(4)])



def validate_ip(ip):
    if(len(ip)!=32):
        return False

    regex = re.compile("^[01]{32}$")
    if(not regex.search(ip)):
        return False

    return True

def main():
    print ("Enter dotted binary IP address: ")
    try:
        ip = (sys.stdin.readline ().strip ())
    except Exception:
        print ("Invalid IP address entered")
        main()

    if (not validate_ip(ip)):
        print ("Invalid IP address entered")
        main()

    print ("IP in binary format: "+to_decimal(ip))
    exit(0)


# main
if __name__ == "__main__":
    main()

