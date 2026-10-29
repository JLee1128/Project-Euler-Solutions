#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sympy as sp
result = 0


def prime_factors(n):
    largest = 0   
    term = n
    i = 1
    while i <= term: 
        if n % i == 0:
            if i > largest:
                if  sp.isprime(i):
                    largest = i
                    term = n // i
            i += 1
        else:
            i += 1
    return largest
    
result = prime_factors(600851475143)

print(result)
    

    