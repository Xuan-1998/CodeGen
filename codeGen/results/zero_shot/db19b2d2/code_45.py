import sys
from math import comb

def calculate_probability():
    n, m, h = map(int, input().split())
    s = list(map(int, input().split()))

    p = s[h-1] / sum(s)
    
    probability = 1 - (1 - p)**n
    
    print(probability)

calculate_probability()
