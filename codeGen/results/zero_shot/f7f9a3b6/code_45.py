import sys

def solve():
    n = int(input())
    s = input()
    a = [int(x) for x in input().split()]
    
    dp = [0] * (n + 1)
    max_len = [0] * (n + 1)

    dp[0] = 1
    max_len[0] = 0

    for i in range(1, n + 1):
        for c in s[:i]:
            if a[ord(c) - 97] > 0:
                prev_max = max_len[i-a[ord(c)-97]-1]
                dp[i] += dp[i-1]
                max_len[i] = max(max_len[i], prev_max + 1)
    
    print(dp[n-1] % (10**9 + 7))
    print(max_len[n-1])
    print(min(i for i in range(n+1) if dp[i]))

solve()
