import sys

t, l, r = map(int, input().split())

def f(n):
    return n * (n.bit_length() - 1)

total_comparisons = sum(ti * f(i) for ti in range(t+1) for i in range(l, r+1)) % (10**9 + 7)
print(total_comparisons)
