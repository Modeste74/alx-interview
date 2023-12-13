#!/usr/bin/env python3
"""Defines a function minOperations"""


def minOperations(n):
    """take a number and is supposed to
    determine the minimum no of operation its
    would take to get the exact amount of character
    based on the number passed as a parameter"""
    if n <= 1:
        return 0

    result = 0
    i = 2
    while i <= n:
        while n % i == 0:
            result += i
            n = n // i
        i += 1

    return result
