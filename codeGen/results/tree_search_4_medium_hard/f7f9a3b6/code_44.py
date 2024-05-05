def count_ways(s, a):
    MOD = 10**9 + 7

    n = len(s)
    dp = [[0] * (n + 1) for _ in range(27)]
    last_char = {}

    # Initialize base case: no substrings
    for k in range(1, 27):
        dp[0][k] = 1 if k == 1 else 0

    for i in range(n):
        if s[i] not in last_char:
            last_char[s[i]] = i
        if i - last_char[s[i]] + 1 > a[ord(s[i]) - ord('a')]:
            continue
        for k in range(26, 0, -1):
            dp[i][k] += dp[i-last_char[s[i]]-1][min(k-1, 26)]
            dp[i][k] %= MOD

    count = 1
    max_len = 0
    min_len = n
    for k in range(1, 27):
        if dp[-1][k]:
            count *= dp[-1][k]
            count %= MOD
            max_len = max(max_len, k)
            min_len = min(min_len, k)

    return count, max_len, min_len

# Read input
n = int(input())
s = input().strip()
a = [int(x) for x in input().split()]

print(count_ways(s, a))
