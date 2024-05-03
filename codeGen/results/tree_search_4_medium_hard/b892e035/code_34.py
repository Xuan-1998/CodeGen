from math import comb
from functools import lru_cache

def calculate_probability(n, probs):
    @lru_cache(None)
    def memoized_calculate_probability(i, used_numbers, used_probabilities):
        if i == n:
            return 1.0
        total_prob = 0
        for j in range(2):
            if j not in used_numbers:
                next_prob = probs[i][j]
                total_prob += next_prob * memoized_calculate_probability(i+1, used_numbers+[j], used_probabilities+[next_prob])
        return total_prob

    return memoized_calculate_probability(0, [], [0])

T = int(input())
for _ in range(T):
    n = int(input())
    probs = []
    for _ in range(n):
        prob1, num1, num2 = map(float, input().split())
        probs.append([prob1+probs[-1][1] if probs else 0, num1, num2])
    total_prob = calculate_probability(n, [p[0] for p in probs])
    print(total_prob)
