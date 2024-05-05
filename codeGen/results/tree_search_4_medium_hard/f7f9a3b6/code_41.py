import sys

def solution():
    n = int(input())
    s = input()
    a = [int(x) for x in input().split()]

    MOD = 10**9 + 7
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(n):
        if i > 0:
            dp[i][0] = dp[i-1][0]
        for k in range(min(i+1, n), -1, -1):
            if i < a[ord(s[i])-97]:
                dp[i][k] += dp[i-a[ord(s[i])-97]][k-1] * (1 or (dp[i-a[ord(s[i])-97]][k-1] > 0))
                dp[i][k] %= MOD
            else:
                if k > 0 and i >= a[ord(s[i])-97]:
                    dp[i][k] += dp[a[ord(s[i])-97]-1][k-1]
                    dp[i][k] %= MOD

    total_ways = sum(dp[n][i] for i in range(n+1))
    total_ways %= MOD
    longest_substring = max(max(row) for row in dp)
    min_substrings = n + 1
    for i in range(n, -1, -1):
        if dp[i][0] > 0:
            min_substrings = min(min_substrings, i+1)

    print(total_ways)
    print(longest_substring)
    print(min_substrings)

if __name__ == "__main__":
    solution()
