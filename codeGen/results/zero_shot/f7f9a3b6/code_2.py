def count_ways(s, n, a):
    MOD = 10**9 + 7

    def dp(i, j):
        if i == 0:
            return 1
        res = 0
        for k in range(26):
            if i - (k + 1) >= 0 and s[i-(k+1):i].count(chr(k+97)) <= a[k]:
                res += dp(i-(k+1), j-1)
                res %= MOD
        return res

    ans = dp(n, 1)
    max_len = 0
    min_substrs = n

    for i in range(26):
        if n - (i + 1) >= 0 and s[n-(i+1):n].count(chr(i+97)) <= a[i]:
            max_len = max(max_len, i + 1)
            min_substrs = min(min_substrs, n // (i + 1) + 1)

    return ans, max_len, min_substrs

n = int(input())
s = input()
a = list(map(int, input().split()))

ans, max_len, min_substrs = count_ways(s, n, a)
print(ans % MOD)
print(max_len)
print(min_substrs)
