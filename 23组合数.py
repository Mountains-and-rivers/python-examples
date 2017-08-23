#!/usr/bin/env python3
# coding:utf-8

from itertools import permutations, combinations


s = 'A, B, C'
s1 = s.replace(',', ' ').split()
# permutations区分顺序
for item in permutations(s1):
    print(','.join(item))
print('='*30)
# combinations不区分顺序
for item in combinations(s1, r=2):
    print(','.join(item))