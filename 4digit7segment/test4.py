#!/usr/bin/env python

def set_bit(value, bit):
    return value | (1<<bit)

def clear_bit(value, bit):
    return value & ~(1<<bit)

i = int('0b11011000', 2)
print(i)
print(i & ~(1<<7))
print(i & ~0x80)

for j in range(0,8):
    num = clear_bit(i, j)
    print(j, bin(num), num)

#i = int('0b01011000', 2)
#print(i)

