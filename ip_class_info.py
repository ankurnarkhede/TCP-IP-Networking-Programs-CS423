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

        self.zeros = ['0', '0', '0', '0']
        self.ones = ['255', '255', '255', '255']

        # decimal ip
        self.decimal_str = None
        self.decimal_str_splitted = None

        # binary ip
        self.binary_str =None
        self.binary_str_splitted = None

        # ip class
        self.class_ip=None
        self.net_id=None
        self.host_id=None
        self.net_mask=None
        self.nw_address=None
        self.direct_broadcast=None




    def __str__(self):
        return

    def ip_info(self):

        # getting all ip instances

        # decimal ip
        self.decimal_str = self.entered
        self.decimal_str_splitted = (list(self.decimal_str.split('.')))

        # binary ip
        self.binary_str = self.dec_to_binary(self.decimal_str_splitted)
        self.binary_str_splitted = self.dec_to_binary(self.decimal_str_splitted, splitted=1)

        # ip class
        self.class_ip, self.net_id, self.host_id, self.net_mask, self.nw_address, self.direct_broadcast \
            = self.get_class_info(self.decimal_str_splitted, self.zeros, self.ones)


    def dec_to_binary(self, ip, splitted=0):
        if (not splitted):
            return ''.join([bin(int(x) + 256)[3:] for x in ip])
        else:
            return ' '.join([bin(int(x) + 256)[3:] for x in ip])

    def get_class_info(self, ip, zeros, ones):

        # ip is string ip splitted into list
        # determining class of ip
        if ((self.binary_str)[0] == '0'):
            net_id = ''.join([str(x) for x in ip[0]])
            nw_address = net_id + '.' + str('.'.join([str(y) for y in zeros[0:3]]))
            direct_bcast = net_id + '.' + str('.'.join([str(y) for y in ones[0:3]]))

            return 'A', net_id, '.'.join([str(x) for x in ip[1:5]]), 8, nw_address, direct_bcast

        elif ((self.binary_str)[0:2] == '10'):
            net_id = '.'.join([str(x) for x in ip[0, 2]])
            nw_address = net_id + '.' + str('.'.join([str(y) for y in zeros[0:2]]))
            direct_bcast = net_id + '.' + str('.'.join([str(y) for y in ones[0:2]]))

            return 'B', net_id, '.'.join([str(x) for x in ip[2:5]]), 16, nw_address, direct_bcast

        elif ((self.binary_str)[0:3] == '110'):
            net_id = '.'.join([str(x) for x in ip[0:3]])
            nw_address = net_id + '.' + str('.'.join([str(y) for y in zeros[0:1]]))
            direct_bcast = net_id + '.' + str('.'.join([str(y) for y in ones[0:1]]))

            return 'C', net_id, '.'.join([str(x) for x in ip[3:5]]), 24, nw_address, direct_bcast

        elif ((self.binary_str)[0:4] == '1110'):
            return 'D', 'NA', 'NA', 'NA', 'NA', 'NA'

        elif ((self.binary_str)[0:4] == '1111'):

            return 'D', 'NA', 'NA', 'NA', 'NA', 'NA'

    def validate_ip(self):

        regex = re.compile(self.REGEX_DEC)
        if (not regex.search(self.entered)):
            return False
        return True

    def print_class_info(self):
        print('%-30s: %s' % ('Entered IP', self.entered))
        print('%-30s: %s' % ('Dotted Decimal IP', self.decimal_str))
        print('%-30s: %s' % ('Binary IP', self.binary_str_splitted))
        print('%-30s: %s' % ('Class', self.class_ip))
        print('%-30s: %s' % ('Network Mask', self.net_mask))
        print('%-30s: %s' % ('Network ID', self.net_id))
        print('%-30s: %s' % ('Host ID', self.host_id))
        print('%-30s: %s' % ('Network Address', self.nw_address))
        print('%-30s: %s' % ('Direct broadcast address', self.direct_broadcast))


def main():
    while(1):
        print("\nEnter dotted decimal IP address: ")
        try:
            ip_str = sys.stdin.readline().strip()

            # ip operations
            ip_1 = IP(ip_str)

            if(ip_1.validate_ip()):
                ip_1.ip_info()
                ip_1.print_class_info()
            else:
                print("Invalid IP address entered")
                continue

        except Exception as e:
            print(e)


# main
if __name__ == "__main__":
    main()
