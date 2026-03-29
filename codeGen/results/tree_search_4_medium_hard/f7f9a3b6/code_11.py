from collections import defaultdict

def solve():
    n = int(input())
    s = input()
    a = [int(x) for x in input().split()]

    dp = [[0]*(n+1) for _ in range(n+1)]
    for i in range(1, n):
        for j in range(i+1, n+1):
            if all(s[k:j].count(c) <= a[ord(c)-97] for c in set(s[k:j])):
                dp[i][j] = (dp[i-1][i] if i > 0 else 1) + sum(dp[k-1][j-1] for k in range(j, i-1, -1))
            else:
                dp[i][j] = sum(dp[k-1][j-1] for k in range(j, i-1, -1))

    num_ways = 0
    for i in range(n):
        if dp[i][n]:
            num_ways += 1
            break

    print(num_ways % (10**9 + 7))
    max_length = max(len(s[:i]) for i in range(n) if dp[i][n])
    print(max_length)
    min_split = min(i for i in range(n) if dp[i][n])
    print(min_split)

solve()
