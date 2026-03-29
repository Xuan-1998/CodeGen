import sys

memo = {}

def count_words(n, m):
    if (n, m) in memo:
        return memo[(n, m)]

    if m == 0:
        return 1
    if m < 0:
        return 0

    res = 0
    for i in range(1, n+1):
        # Check if the current letter can be followed by another letter
        if (i & 1 and i > n//2) or (i % 2 == 0 and i <= n//2):
            res += count_words(n-1, m-1)
        else:
            res += 1

    memo[(n, m)] = res
    return res

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    print((count_words(n, m) + 7) % (10**8+7))
