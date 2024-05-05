python
import math

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    total_words = 1
    for i in range(1, n//2+1):
        if 2*i > n:
            total_words *= (n - i + 1) * m
        else:
            total_words *= (math.ceil((n-1)/i)-i+1) * m
    print(total_words % (10**8 + 7))
