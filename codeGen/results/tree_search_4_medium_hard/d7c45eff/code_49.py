import sys

def solve():
    n, k = map(int, input().split())
    s = input()

    memo = {}

    def dp(i, j):
        if (i, j) in memo:
            return memo[(i, j)]
        
        res = ''
        for _ in range(j//len(s[i-1:]+s[:i-1])) + (j % len(s[i-1:]+s[:i-1]) != 0):
            res += s[i-1]
        
        if j > 0 and i > 0:
            res = min(res, dp(i-2, j-1)[::-1] + s[i-1], key=lambda x: (x, -ord(x[0])))
        
        memo[(i, j)] = res
        return res

    print(dp(n, k))
