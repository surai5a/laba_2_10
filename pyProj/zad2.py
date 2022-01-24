#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def garm(*args):
    if args:
        summa = float(0)
        for arg in args:
            summa = summa + (1 // arg)
        n = len(args)
        return n // summa
    else:
        return None


if __name__ == "__main__":
    print(garm(1, 4, 6, 10))
