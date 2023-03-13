#!/usr/bin/python3
"""0. Prime Game"""


def isWinner(x, nums):
    """Finds the Winner"""
    def isPrime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True

    def play(n, current_player):
        """Determines current gameplay"""
        primes = [i for i in range(2, n+1) if isPrime(i)]
        if not primes:
            return current_player  # no primes left, current player loses
        for p in primes:
            multiples = [i for i in range(p, n+1, p)]
            if current_player == 'Maria':
                next_player = 'Ben'
            else:
                next_player = 'Maria'
            result = play(n - len(multiples), next_player)
            if result == current_player:
                return current_player  # found a winning move
        return next_player  # no winning moves, next player wins

    scores = {'Maria': 0, 'Ben': 0}
    for n in nums:
        winner = play(n, 'Maria')
        if winner is not None:
            scores[winner] += 1

    if scores['Maria'] > scores['Ben']:
        return 'Maria'
    elif scores['Ben'] > scores['Maria']:
        return 'Ben'
    else:
        return None
