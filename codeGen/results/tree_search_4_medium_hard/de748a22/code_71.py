import sys

def solve():
    n, q = map(int, input().split())
    signs = list(input())

    dp = [[0] * (q + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(q + 1):
            if j == 0:
                continue
            l, r = map(int, input().split())
            k = 0
            for x in signs[l - 1:r]:
                if x == '+':
                    k += 1
                else:
                    k -= 1
                    if k < 0:
                        break
            dp[i][j] = k if k >= 0 else -1

    for i in range(1, n + 1):
        for j in range(1, q + 1):
            print(dp[i][j], end=' ')
        print()

solve()
