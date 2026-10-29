#!/usr/bin/env python3
# -*- coding: utf-8 -*-
result = 0
sum_of_squares = 0
square_of_sum = 0

for i in range(1, 101):
    sum_of_squares += i * i
    square_of_sum += i

square_of_sum = square_of_sum * square_of_sum

result = square_of_sum - sum_of_squares

print(result)
