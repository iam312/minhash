#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys;

def minhash( values, seeds, funcs ) :
    result = []
    for func in funcs :
        for value in values :
            if value in func :
                result.append(value)
                break

    return list(set(result)) # 중복을 제거한다.

