
# program to convert dotted decimal ip address to binary

import sys

def to_binary(ip):
    return '.'.join([bin(int(x)+256)[3:] for x in ip])


def validate_ip(ip):
    if(len(ip)!=4):
        return False
    for x in ip:
        if (x < 0 or x > 255):
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


