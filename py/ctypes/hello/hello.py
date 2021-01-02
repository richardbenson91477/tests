#!/usr/bin/env python3

import sys
import ctypes as ct
import codecs

b_in = bytes(80)

def main ():
    h_lib = ct.cdll.LoadLibrary ('./ext_hello.so') 
    res = h_lib.ext_hello (bytes("bob".encode()), b_in)
    _s = codecs.decode (b_in)
    print(_s)

if __name__ == '__main__':
    sys.exit(main ())
