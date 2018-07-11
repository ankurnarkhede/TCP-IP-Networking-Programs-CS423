# program to convert dotted binary ip address to decimal

import sys
import re

def to_decimal(ip):
    return '.'.join([str(int(x,2)) for x in ip])


def validate_ip(ip):
    if(len(ip)!=4):
        return False

    regex = re.compile("^[01]{8}$")
    for i in range(0,4,+1):
        if(regex.search(ip[i])):
            pass
        else:
            return False
    return True

def main():
    print ("Enter dotted binary IP address: ")
    try:
        ip = (list(sys.stdin.readline ().strip ().split ('.')))
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

