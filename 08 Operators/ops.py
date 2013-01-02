#!/usr/local/bin/python3
# ops.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC


def main():
    print("This is the ops.py file.")
    b(5)

    x, y = 0x55, 0xaa
    b(x)
    b(y)

    # bitwise or
    b(x | y)
    # bitwise and
    b(x & y)
    # bitwise exclusive or
    b(x ^ y)
    b(x ^ 0x03)
    # shift bits left 4 places.
    # right 4 get filled with zeros.
    # This multiplies number by 2**4 = 16
    b(0xff << 4)
    b(x << 4)

    # shift bits right 4 places.
    # left 4 get filled with zeros.
    # This divides number by 2**3 = 8
    b(0xff >> 3)
    b(x >> 3)

    #ones complement, operates on implementation word size, > 8 bits 
    b(~x)



def b(n):
    print('{:08b}'.format(n))

if __name__ == "__main__": main()
