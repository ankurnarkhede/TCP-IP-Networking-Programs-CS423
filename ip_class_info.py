# program to convert dotted decimal ip address to binary

import sys

def to_binary(ip):
    return '.'.join([bin(int(x)+256)[3:] for x in ip])

def class_info(ip):
    # determining clas
    if((to_binary(ip))[0]=='0'):
        print("Class of IP address: A")
        print("NetId: "+'.'.join([str(x) for x in ip[0]]))
        print("HostId: "+'.'.join([str(x) for x in ip[1:5]]))
    elif((to_binary(ip))[0:2]=='10'):
        print("Class of IP address: B")
        print("NetId: "+'.'.join([str(x) for x in ip[0:2]])) 
        print("HostId: "+'.'.join([str(x) for x in ip[2:5]]))   
    elif((to_binary(ip))[0:3]=='110'):
        print("Class of IP address: C")
        print("NetId: "+'.'.join([str(x) for x in ip[0:3]]))
        print("HostId: "+'.'.join([str(x) for x in ip[3:5]]))
    elif((to_binary(ip))[0:4]=='1110'):
        print("Class of IP address: D")
    elif((to_binary(ip))[0:4]=='1111'):
        print("Class of IP address: E")


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
        # print(ip)
    except Exception:
        print ("Invalid IP address entered")
        main()

    if (not validate_ip(ip)):
        print ("Invalid IP address entered")
        main()

    class_info(ip)

    sys.exit(0)


# main
if __name__ == "__main__":
    main()

