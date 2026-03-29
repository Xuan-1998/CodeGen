def solve(n, s, a):
    MOD = 10**9 + 7

    dp = [[False] * (n+1) for _ in range(n+1)]
    memo = [0] * (26*10000)

    for i in range(n):
        for j in range(i, n):
            if all(s[k] <= a[ord(c)-97] for k in range(i+1, j+1)):
                dp[i][j] = True
            else:
                dp[i][j] = False

    ways = 0
    max_length = 0
    min_substrings = n

    for i in range(n):
        for j in range(i, n):
            if dp[i][j]:
                ways += 1
                max_length = max(max_length, j-i+1)
                min_substrings = min(min_substrings, j-i+1)

    print(ways % MOD)
    print(max_length)
    print(min_substrings)

# Input data
n = int(input())
s = input().strip()
a = [int(x) for x in input().split()]

solve(n, s, a)
