"""
Byte xorValue = 0;
int len;
char *p = "<L1><PA><FE><MA><WC><FE>welcome" ;
len = strlen(p);
for (int i=0; i<len; i++)
xorValue ^= *p++;
"""

import sys


def checksum_message(p):
    xorValue = 0
    for i in range(len(p)):
        xorValue ^= ord(p[i])
    chksum = str(hex(xorValue))[2:].upper()
    # Pad with 0 if needed
    if len(chksum) == 1:
        chksum = '0' + chksum
    return chksum


if __name__ == "__main__":
    if len(sys.argv) > 1:
        print(checksum_message(sys.argv[1]))
    else:
        print(checksum_message())
