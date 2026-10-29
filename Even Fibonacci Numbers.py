#!/usr/bin/env python3
# -*- coding: utf-8 -*-
result = 0
answ = 0
n = 0

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
        

while  answ < 4000000:
    answ = fib(n)
    if fib(n) % 2 == 0:
        result += fib(n)
    n += 1

print(result)



