#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys;
import random;

def _make_func( seeds, howmany_func=3, howmany_items=3 ):
    func = []
    howmany_rows = len(seeds)
    for idx in range(howmany_func) :
        func.append( random.sample(seeds, howmany_items) )
        
    return func


def load(raw_seeds):
    seeds = []
    for seed in raw_seeds :
        # raw_seeds 는 cid\trank\n 로 구성되어 있다고 가정한다.
        seeds.append( seed.strip() )

    return seeds, _make_func( seeds )


def main(argv):
    with open('seed.txt') as f:
        content = f.readlines()
        seeds, funcs = load(content)
        print seeds, funcs


if __name__ == "__main__":
     main(sys.argv)

