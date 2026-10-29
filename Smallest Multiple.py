#!/usr/bin/env python3
# -*- coding: utf-8 -*-
answ = 20
final = 0
check = True

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

temp = factorial(20)
temp = (((((((temp / 19) / 17) / 13) / 11) / 7) / 5) / 3)
print(temp)
while answ <= temp:
    check = True
    for j in range(1, 21):
        if answ % j == 0:
            final = answ
        else: 
            check = False
            break
    if check == True:
        break
    answ += 20

print(final)