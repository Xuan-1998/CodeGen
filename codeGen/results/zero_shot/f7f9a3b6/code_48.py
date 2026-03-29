def split_string(s, a):
    n = len(s)
    dp = [0] * (n + 1)

    for i in range(1, n + 1):
        c = s[i-1]
        if ord(c) - 1 < 26 and a[ord(c)-1] >= i:
            dp[i] = dp[i-1] + 1
        else:
            dp[i] = dp[i-1]

    ways = dp[-1]
    max_length = max(dp)
    min_substrings = len(s) // max_length

    return ways % (10**9 + 7), max_length, min_substrings


n = int(input())
s = input()
a = [int(x) for x in input().split()]

ways, max_length, min_substrings = split_string(s, a)
print(ways)
print(max_length)
print(min_substrings)
