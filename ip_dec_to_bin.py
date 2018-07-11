# program to convert dotted decimal ip address to binary

import sys
import re

def to_binary(ip):
    return '.'.join([bin(int(x)+256)[3:] for x in ip])


def validate_ip(ip):
    if(len(ip)!=4):
        return False
    
    regex = re.compile("^([1]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])$")
    for x in ip:
        if(regex.search(str(x))):
            pass
        else:
            return False
    return True

def main():
    print ("Enter dotted decimal IP address: ")
    try:
        ip = (list (map (int, sys.stdin.readline ().strip ().split ('.'))))
    except Exception:
        print ("Invalid IP address entered")
        main()

    if (not validate_ip(ip)):
        print ("Invalid IP address entered")
        main()

    print "IP in binary format: "+to_binary(ip)
    exit(0)


# main
if __name__ == "__main__":
    main()

