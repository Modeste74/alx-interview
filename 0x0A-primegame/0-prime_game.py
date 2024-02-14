#!/usr/bin/python3
"""Defines a function isWinner"""


def isWinner(x, nums):
    """Takes a nimber of rounds 'x' and an array
    of integers 'nums' and returns the winner of the game."""
    def is_prime(num):
        """return False or True based on whether
        a number is a prime number"""
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def find_next_prime(nums):
        """Takes a list of numbers and returns the next prime
        number in the list."""
        for num in nums:
            if is_prime(num):
                return num
        return None

    def play_round(nums):
        """simulates the rounds of the game by repeatedly finding
        the next prime number in the list and removing it together with
        its multiples till there are no more prime number and then it
        returns the winner."""
        while True:
            prime = find_next_prime(nums)
            if prime is None:
                return "Ben"
            nums = [num for num in nums if num % prime != 0]
    maria_wins = 0
    ben_wins = 0
    for n in nums:
        winner = play_round(list(range(1, n + 1)))
        if winner == "Maria":
            maria_wins += 1
        elif winner == "Ben":
            ben_wins += 1
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
