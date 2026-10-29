#!/usr/bin/env python3
# -*- coding: utf-8 -*-

a = 1
b = 2

def pythagorean_triplet(a, b):
    c = (a**2 + b**2)**0.5
    if a + b + c == 1000:
        return a * b * c
    else:
        return 0


while a < 1000:
    while b < 1000:
        if pythagorean_triplet(a, b) != 0:
            result = pythagorean_triplet(a, b)
            break
        b += 1
    a += 1
    b = a + 1

print(int(result))