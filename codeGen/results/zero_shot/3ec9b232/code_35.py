import sys

n = int(input())
M = list(map(int, input().split()))
K = 1
for m_i in M:
    K *= (n - m_i + 1) % (10**9 + 7)

print(K)
