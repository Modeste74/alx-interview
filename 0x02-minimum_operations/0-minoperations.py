#!/usr/bin/env python3
"""Defines a function minOperations"""
import math


def minOperations(n):
    """take a number and is supposed to
    determine the minimum no of operation its
    would take to get the exact amount of character
    based on the number passed as a parameter"""
    if n == 1:
        return 0
    operations = 0
    for i in range(2, int(math.sqrt(n)) + 1):
        while n % i == 0:
            n //= i
            operations += i
    if n > 1:
        operations += n
    return operations
