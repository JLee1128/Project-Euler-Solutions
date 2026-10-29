#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def n_prime(n):
    count = 0
    num = 1
    while count < n:
        num += 1
        for i in range(2, num + 1): 
            if num % i == 0:            #Finding the prime number 
                break
        if i == num:                    #If the number is largest prime for iteration
            count += 1                  #Incrementing the count of prime numbers found
    return num                          #Returning the nth prime number    

result = n_prime(10001)
print(result)


