#!/usr/bin/python3

from pickletools import dis


def magic_calculation(a, b):
    dis.dis(magic_calculation)
    result = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')
            else:
                result += a ** b / i
        except:
            result = b + a
            break
    return (result)