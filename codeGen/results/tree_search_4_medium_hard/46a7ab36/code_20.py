import sys

dp = {}
def count_words(n, m):
    if (n, m) not in dp:
        if m == 0:
            dp[(n, m)] = 1
        else:
            result = 0
            for k in range(1, n+1):
                if 2*k + m <= n and ((k/2 + m >= m) or (k/2 + m >= n - k)):
                    result += dp.get((n-2*k, m-1), 0)
            dp[(n, m)] = result % (10**8 + 7)
    return dp[(n, m)]

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    print(count_words(n, m))
