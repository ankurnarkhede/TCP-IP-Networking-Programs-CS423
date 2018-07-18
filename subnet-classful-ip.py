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
            # print ("ip validated")

            # decimal ip
            self.decimal_str = self.entered
            self.decimal_str_splitted = (list (self.decimal_str.split ('.')))

            # binary ip
            self.binary_str = self.dec_to_binary (self.decimal_str_splitted)
            self.binary_str_splitted = self.dec_to_binary (self.decimal_str_splitted, splitted=1)

            # ip class
            self.class_ip, self.net_id, self.host_id,self.net_mask = self.get_class_info (self.decimal_str_splitted)


        else:
            print ("Invalid IP address entered")
            main ()

    def __str__(self):
        return

    def dec_to_binary(self, ip, splitted=0):
        if (not splitted):
            return ''.join ([bin (int (x) + 256)[3:] for x in ip])
        else:
            return ' '.join ([bin (int (x) + 256)[3:] for x in ip])

    def get_class_info(self, ip):
        # determining class of ip
        if ((self.binary_str)[0] == '0'):

            return 'A', ''.join ([str (x) for x in ip[0]]), '.'.join ([str (x) for x in ip[1:5]]),8

        elif ((self.binary_str)[0:2] == '10'):

            return 'B', '.'.join ([str (x) for x in ip[0, 2]]), '.'.join ([str (x) for x in ip[2:5]]),16

        elif ((self.binary_str)[0:3] == '110'):

            return 'C', '.'.join ([str (x) for x in ip[0:3]]), '.'.join ([str (x) for x in ip[3:5]]),24

        elif ((self.binary_str)[0:4] == '1110'):
            return 'D', 'NA', 'NA','NA'

        elif ((self.binary_str)[0:4] == '1111'):

            return 'D', 'NA', 'NA','NA'

    def validate_ip(self, ip):

        regex = re.compile (self.REGEX_DEC)
        if (not regex.search (ip)):
            return False
        return True

    def print_class_info(self):
        print ('%-20s: %s' % ('Entered IP', self.entered))
        print ('%-20s: %s' % ('Dotted Decimal IP', self.decimal_str))
        print ('%-20s: %s' % ('Binary IP', self.binary_str_splitted))
        print ('%-20s: %s' % ('Class', self.class_ip))
        print ('%-20s: %s' % ('Network Mask', self.net_mask))
        print ('%-20s: %s' % ('Network ID', self.net_id))
        print ('%-20s: %s' % ('Host ID', self.host_id))


def main():
    print ("Enter dotted decimal IP address: ")
    try:
        ip_str = sys.stdin.readline ().strip ()

    except Exception:
        print ("Invalid IP address entered")
        main ()

    # ip operations
    ip_1 = IP (ip_str)
    ip_1.print_class_info ()

    # class_info(ip)

    sys.exit (0)


# main
if __name__ == "__main__":
    main ()

