#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys;
import seeds;
import minhash;

def _mapper(fields, seeds, funcs):
    key = fields[0]
    values = fields[1].split(",") # value 는 ',' 로 구분되어 있다.
    
    for value in minhash.minhash(values, seeds, funcs) :
        print("%s\t%s" % (value, key))
        

def main(argv):
    with open('seed.txt') as f:
        content = f.readlines()
        raw_seeds, funcs = seeds.load(content)

    line = sys.stdin.readline();
    try:
        while line:
            line = line[:-1];
            fields = line.split(":");
            _mapper(fields, raw_seeds, funcs);
            line = sys.stdin.readline();
    except "end of file":
        return None

if __name__ == "__main__":
     main(sys.argv)
