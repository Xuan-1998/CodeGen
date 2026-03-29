import sys

def solve():
    n, k = map(int, input().split())
    s = input()

    dp = {(i, False): i for i in range(n + 1)}
    dp[(n, True)] = s

    result = None
    for i in range(n, -1, -1):
        if len(s) > k:
            if dp[(i, False)] is not None and dp[(i, True)] is not None:
                dp[(i, False)], dp[(i, True)] = min(dp[(i, False)], dp[(i, True)]), max(dp[(i, False)], dp[(i, True)])
        else:
            if s[i:] == s[:k]:
                return s
    return result

print(solve())
