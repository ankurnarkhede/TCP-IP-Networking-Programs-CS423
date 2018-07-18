import sys
import math
import re


class IP:
    def __init__(self, ip_address):

        # python regex for ips
        self.REGEX_BIN = "^[01]{32}$"
        self.REGEX_DEC = "^([1]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])\.([1]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])\.([1]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])\.([1]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])$"

        # ip properties
        self.entered = ip_address

        if (self.validate_ip (self.entered)):
            print ("ip validated")

            # decimal ip
            self.decimal_str = self.entered
            self.decimal_int_splitted = (list (map (int, self.decimal_str.split ('.'))))

            # binary ip
            self.binary_str = self.dec_to_binary (self.decimal_int_splitted)

            # ip class
            self.class_ip = self.get_class (self.binary_str)
            self.mask = None


        else:
            print ("Invalid IP address entered")
            main ()

    def dec_to_binary(self, ip):
        return ''.join ([bin (int (x) + 256)[3:] for x in ip])

    def get_class(self, ip):
        # determining class of ip
        if ((self.binary_str)[0] == '0'):
            print ("Class of IP address: A")
            print ("NetId: " + '.'.join ([str (x) for x in ip[0]]))
            print ("HostId: " + '.'.join ([str (x) for x in ip[1:5]]))
            return 'A'
        elif ((self.binary_str)[0:2] == '10'):
            print ("Class of IP address: B")
            print ("NetId: " + '.'.join ([str (x) for x in ip[0:2]]))
            print ("HostId: " + '.'.join ([str (x) for x in ip[2:5]]))
            return 'B'
        elif ((self.binary_str)[0:3] == '110'):
            print ("Class of IP address: C")
            print ("NetId: " + '.'.join ([str (x) for x in ip[0:3]]))
            print ("HostId: " + '.'.join ([str (x) for x in ip[3:5]]))
            return 'C'
        elif ((self.binary_str)[0:4] == '1110'):
            print ("Class of IP address: D")
            return 'D'
        elif ((self.binary_str)[0:4] == '1111'):
            print ("Class of IP address: E")
            return 'E'

    def __str__(self):
        return

    def validate_ip(self, ip):

        regex = re.compile (self.REGEX_DEC)
        if (not regex.search (ip)):
            return False
        return True


def main():
    print ("Enter dotted decimal IP address: ")
    try:
        ip_str = sys.stdin.readline ().strip ()

        print (ip_str)
    except Exception:
        print ("Invalid IP address entered")
        main ()

    # ip operations
    ip_1 = IP (ip_str)

    # class_info(ip)

    sys.exit (0)


# main
if __name__ == "__main__":
    main ()

