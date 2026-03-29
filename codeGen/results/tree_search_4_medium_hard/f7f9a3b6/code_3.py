===BEGIN CODE===
def solve():
    n = int(input())
    s = input()
    a = list(map(int, input().split()))

    dp = [[0] * (n + 1) for _ in range(n + 1)]

    # Initialize the base case
    dp[0][n - 1] = 1

    for i in range(n):
        for j in range(i + 1, n + 1):
            if dp[i][j - 1]:
                for k in range(ord('a'), ord('z') + 1):
                    if a[k - ord('a')] <= a[ord(s[i].lower()) - ord('a')] and a[ord(s[j - 1].lower()) - ord('a')] <= a[k - ord('a')]:
                        dp[i][j] = 1
                        break

    # Calculate the number of ways to split the message
    total_ways = 0
    for i in range(n):
        if dp[0][i]:
            total_ways += (n - i)
            break

    # Calculate the length of the longest substring and the minimum number of substrings
    max_length = 1
    min_substrings = float('inf')
    for i in range(n):
        for j in range(i + 1, n + 1):
            if dp[i][j]:
                max_length = max(max_length, j - i)
                min_substrings = min(min_substrings, j - i)

    print((total_ways % (10**9 + 7)))
    print(max_length)
    print(min_substrings)

solve()
