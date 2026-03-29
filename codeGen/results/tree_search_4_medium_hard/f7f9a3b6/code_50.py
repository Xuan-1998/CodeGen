def solve():
    n = int(input())
    s = input()
    a = [int(x) for x in input().split()]

    # Initialize memoization dictionary
    memo = {}

    def dp(i, j):
        if (i, j) in memo:
            return memo[(i, j)]

        if i == 0:
            return 0

        m = min(a[ord(s[i-1])-97], sum(1 for c in s[:i] if c not in set(s[:i-1]))))
        dp_val = float('inf')
        for k in range(26):
            if sum(c == chr(m+96) for c in s[:i]) <= m:
                dp_val = min(dp_val, dp(i-1, k) + 1)

        memo[(i, j)] = dp_val
        return dp_val

    # Calculate final results
    ways_to_split = 1
    max_length = 0
    min_substrings = float('inf')

    for i in range(n):
        for j in range(26):
            if i == 0:
                continue
            ways_to_split *= (dp(i, j) + 1)
            max_length = max(max_length, dp(i, j))
            min_substrings = min(min_substrings, dp(i, j))

    print(ways_to_split % (10**9 + 7))
    print(max_length)
    print(min_substrings)

if __name__ == "__main__":
    solve()
