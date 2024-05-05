import sys

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    result_len = len(str(n))
    print(result_len % (10**9 + 7))
