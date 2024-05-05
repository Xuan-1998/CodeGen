import sys

dp = {}

def solve(n, m):
    if (n, m) in dp:
        return dp[(n, m)]

    res = n.bit_length()
    for _ in range(m):
        new_n = 0
        for d in str(n):
            new_n = new_n * 10 + int(d) + 1
        res = max(res, new_n.bit_length())
        n = new_n

    dp[(n, m)] = res % (10**9 + 7)
    return dp[(n, m)]

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    print(solve(n, m))
