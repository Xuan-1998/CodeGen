import sys

def and_or_xor(n, k):
    total = 0
    for i in range(k):
        if (1 << i) & n:
            total += (2 ** (k - i - 1))
    return min(total, (1 << k) - 1)

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    print(and_or_xor(n, k) % (10**9 + 7))
