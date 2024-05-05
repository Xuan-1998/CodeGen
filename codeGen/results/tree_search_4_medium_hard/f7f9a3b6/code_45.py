def split_string(s, a):
    n = len(s)
    if n <= 0:
        return "Error: Input length is invalid."

    dp = [[0] * (n + 1) for _ in range(n + 1)]
    unique_chars = set()
    repeated_chars = {}

    # Count unique and repeated characters
    for c in s:
        if c not in unique_chars:
            unique_chars.add(c)
        else:
            if c not in repeated_chars:
                repeated_chars[c] = a[ord(c) - ord('a')]
            repeated_chars[c] -= 1

    # Dynamic programming
    for i in range(n + 1):
        dp[i][0] = 1
        for k in range(1, n + 1):
            if k <= i:
                if s[i - k:i] not in unique_chars and repeated_chars.get(s[i - k], 0) >= 0:
                    dp[i][k] = (dp[i - k][k] * (i - k)) % (10**9 + 7)
                else:
                    dp[i][k] = 0
            else:
                dp[i][k] = 0

    # Find the number of ways to split the string
    num_ways = dp[n][1]
    for k in range(2, n + 1):
        num_ways = (num_ways * (dp[n][k])) % (10**9 + 7)

    # Find the length of the longest substring over all ways
    max_length = max(dp[i][i] for i in range(n + 1))

    # Find the minimum number of substrings
    min_substrings = n // max_length

    print(num_ways)
    print(max_length)
    print(min_substrings)

# Example usage:
s = input()
a = [int(x) for x in input().split()]
split_string(s, a)
