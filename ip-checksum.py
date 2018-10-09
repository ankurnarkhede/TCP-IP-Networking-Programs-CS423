from scapy.all import *
import binascii
import sys


class ip_packet:

    def __init__(self, packet):
        self.packet = packet
        self.packet_length = self.packet.ihl * 4
        self.hex_ip = self.get_hex()

    def view_packet(self):
        self.packet.show()

    def get_hex(self):
        start = 14
        to_bytes = bytes(self.packet)[start:start + self.packet_length]
        hex_ip = binascii.hexlify(to_bytes)
        print("HEX_IP: ", hex_ip)
        return hex_ip

    def ones_compliment(self, binary):
        binary = binary[2:]
        return ('0b' + ''.join([str(int(not (int(x) and 1))) for x in binary]))

    def calculate_checksum(self):

        bin_sum = bin(0)

        checksum_defined = self.hex_ip[5 * 4:5 * 4 + 4]
        print("CHECKSUM={}".format(checksum_defined))
        checksum_defined_bin = bin(int(checksum_defined, 16))
        print("BINARY CHECKSUM={}".format(bin(int(checksum_defined, 16))))

        for i in range(0, len(self.hex_ip) // 4, +1):
            if (i == 5):
                continue
            this_hex = self.hex_ip[i * 4:(i + 1) * 4]

            bin_sum = bin(int(bin_sum, 2) + int(this_hex, 16))


            if (len(bin_sum) > 18):
                bin_sum = bin(int(bin_sum[-16:], 2) + int(bin_sum[:-16], 2))

        bin_sum = '0b' + bin(int(bin_sum, 2) + 65536)[3:]

        checksum_calculated = self.ones_compliment(bin_sum)

        print("Checksum(binary): ", checksum_calculated)

        print("BINARY CHECKSUM= {}".format(bin(int(checksum_defined, 16))))

        if (checksum_defined_bin == checksum_calculated):
            print("VERIFIED")
            sys.exit(0)
        else:
            print("INVALID")

        def verify_checksum(self):
            # verifying on receiving

            bin_sum = bin(0)

            checksum_defined = self.hex_ip[5 * 4:5 * 4 + 4]
            print("CHECKSUM={}".format(checksum_defined))
            checksum_defined_bin = bin(int(checksum_defined, 16))
            print("BINARY CHECKSUM={}".format(bin(int(checksum_defined, 16))))

            for i in range(0, len(self.hex_ip) // 4, +1):
                # if (i == 5):
                #     continue
                this_hex = self.hex_ip[i * 4:(i + 1) * 4]

                bin_sum = bin(int(bin_sum, 2) + int(this_hex, 16))

                if (len(bin_sum) > 18):
                    bin_sum = bin(int(bin_sum[-16:], 2) + int(bin_sum[:-16], 2))

            bin_sum = '0b' + bin(int(bin_sum, 2) + 65536)[3:]

            checksum_calculated = self.ones_compliment(bin_sum)

            print("Checksum(binary): ", checksum_calculated)

            print("BINARY CHECKSUM= {}".format(bin(int(checksum_defined, 16))))

            if (checksum_defined_bin == checksum_calculated):
                print("VERIFIED")
                sys.exit(0)
            else:
                print("INVALID")


def main():
    packet = sniff(1, filter='ip')

    packet_obj = ip_packet(packet[0])
    packet_obj.view_packet()
    packet_obj.calculate_checksum()


if __name__ == '__main__':
    main()
