import sys
from math import comb

def solution():
    n, m, h = map(int, input().split())
    s = list(map(int, input().split()))
    
    # Calculate the probability that exactly i players are chosen from the department of interest
    p = [0] * (n + 1)
    for k in range(h, min(h + n, m) + 1):
        if k == h:
            p[k] = 1.0 / comb(m - 1, k - h)
        else:
            p[k] = p[h] * (s[h - 1] / (n - k + 1)) * (1 - p[k - 1])
    
    # Calculate the probability that at least one player is from the department of interest
    ans = sum(p[i] for i in range(1, n + 1))
    
    print(ans)

solution()
