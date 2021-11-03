#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys


def main(input_num):

    idx = dict()
    set_num = sorted(set(input_num))
    
    for i, num in enumerate(set_num):
      idx[num] = str(i)
      
    ans = []
    for num in input_num:
        ans.append(idx[num])

    print(" ".join(ans))


if __name__ == "__main__":
    n = input()
    input_num = sys.stdin.readline().strip().split(" ")
    input_num = [int(i) for i in input_num]
    main(input_num)
