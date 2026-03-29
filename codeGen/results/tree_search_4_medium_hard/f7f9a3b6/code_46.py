def solve():
    n = int(input())
    s = input()
    a = [int(x) for x in input().split()]

    dp = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for k in range(i + 1):
            if i < k:
                dp[i][k] = 0
            elif i == k:
                dp[i][k] = 1
            else:
                for j in range(k - 1, min(k, i) + 1):
                    dp[i][k] += dp[i - j - 1][k - 1] * (i - j)
                if i >= a[ord(s[i - 1]) - ord('a')]:
                    dp[i][k] = max(dp[i][k], dp[i - a[ord(s[i - 1]) - ord('a')]][k])

    ways_to_split, max_length, min_substrings = 0, 0, float('inf')
    for k in range(n + 1):
        if k > 0 and dp[n][k] > 0:
            ways_to_split += dp[n][k]
            max_length = max(max_length, n // k)
            min_substrings = min(min_substrings, k)

    print(ways_to_split % (10**9 + 7))
    print(max_length)
    print(min_substrings)


if __name__ == "__main__":
    solve()
