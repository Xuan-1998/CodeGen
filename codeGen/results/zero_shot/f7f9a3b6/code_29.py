def solve():
    n = int(input())
    s = input()
    a = [int(x) for x in input().split()]

    dp = [[0] * (n + 1) for _ in range(n + 1)]
    max_length = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(min(i, len(s) - i + 1)):
            if ord(s[i-1]) - ord('a') < 26:
                max_consecutive = a[ord(s[i-1]) - ord('a')]
                dp[i][j] = (dp[i-1][j-1] * max_consecutive) % (10**9 + 7)
            else:
                dp[i][j] = 0
            max_length[i][j] = max(max_length[i-1][j], a[ord(s[i-1]) - ord('a')] if j > 0 else 0)

    ways_to_split = dp[n][-1]
    max_substring_len = max_length[n][-1]

    return str(ways_to_split), str(max_substring_len), str(n // (max_length[n][-1] + 1))

if __name__ == "__main__":
    print(*solve(), sep='\n')
