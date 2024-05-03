import sys
from math import comb

T = int(sys.stdin.readline())
for _ in range(T):
    n = int(sys.stdin.readline())
    probabilities = []
    for _ in range(n):
        p1, a1, b1 = map(float, sys.stdin.readline().split())
        probabilities.append((p1, a1, b1))
    
    correct_numbering_prob = 1
    used_numbers = set()
    for p1, a1, b1 in probabilities:
        if a1 not in used_numbers and b1 not in used_numbers:
            correct_numbering_prob *= (p1 * comb(n-1, 1) + (1-p1) * comb(n-2, 1))
        elif a1 not in used_numbers:
            correct_numbering_prob *= p1 * comb(n-1, 1)
        elif b1 not in used_numbers:
            correct_numbering_prob *= (1-p1) * comb(n-2, 1)
        else:
            correct_numbering_prob *= (p1 + (1-p1)) / 2
        used_numbers.add(a1)
        used_numbers.add(b1)
    
    print(correct_numbering_prob)
