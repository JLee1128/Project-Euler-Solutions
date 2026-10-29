#!/usr/bin/env python3
# -*- coding: utf-8 -*-
answ = 0

def is_palindrome(n):
    return str(n) == str(n)[::-1]

for i in range(100, 1000):
    for j in range(100, 1000):
        if is_palindrome(i * j):
            if i * j > answ:
                answ = i * j

print(answ)