#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys;

def _reducer(fields):
    key, value = fields
    print("%s\t%s" % (key, value))
        

def main(argv):
    line = sys.stdin.readline();
    try:
        while line:
            line = line[:-1];
            fields = line.split("\t");
            _reducer(fields);
            line = sys.stdin.readline();
    except "end of file":
        return None

if __name__ == "__main__":
     main(sys.argv)

