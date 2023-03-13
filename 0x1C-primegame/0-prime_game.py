#!/usr/bin/python3
"""0. Prime Game"""


def isWinner(x, nums):
    """Finds the Winner"""
    def isPrime(n):
        """Determines prime number"""
        if n < 2:
            return False
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True

    def play(n):
        """Determines current gameplay"""
        primes = [i for i in range(2, n+1) if isPrime(i)]
        current_player = 'Maria'
        while primes:
            move = None
            for p in primes:
                if n % p == 0:
                    move = p
                    break
            if move is None:
                break
            multiples = [i for i in range(move, n+1, move)]
            primes = [p for p in primes if p not in multiples]
            current_player = 'Ben' if current_player == 'Maria' else 'Maria'
        return current_player

    scores = {'Maria': 0, 'Ben': 0}
    for n in nums:
        winner = play(n)
        if winner is not None:
            scores[winner] += 1

    if scores['Maria'] > scores['Ben']:
        return 'Maria'
    elif scores['Ben'] > scores['Maria']:
        return 'Ben'
    else:
        return None
