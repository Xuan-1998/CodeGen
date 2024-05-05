def solve():
    n = int(input())
    s = input()
    a = list(map(int, input().split()))

    # Initialize 2D table dp
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    # Base case: only one way to split an empty string
    for i in range(n + 1):
        dp[i][i] = 1

    # Fill up the dp table
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length
            if all(c <= a[ord(c) - ord('a')] for c in set(s[i:j])):
                ways = 0
                for k in range(i + 1, j):
                    ways += dp[i][k-1]
                dp[i][j] = min(ways, dp[i][j-1])
            else:
                dp[i][j] = dp[i][j-1]

    # Calculate the number of ways to split the message
    num_ways = dp[0][n]
    print(num_ways % (10**9 + 7))

    # Find the length of the longest substring
    max_length = max((k-j for k in range(n+1) for j in range(k)), default=0)
    print(max_length)

    # Find the minimum number of substrings
    min_substrs = len([i for i in range(n+1) if dp[0][i] % (10**9 + 7) == num_ways])
    print(min_substrs)
