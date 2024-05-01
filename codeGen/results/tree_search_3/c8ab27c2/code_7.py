def shortest_common_subsequence(S, T):
    n = len(S)
    m = len(T)

    # Create a hashmap to store the frequency of prefixes
    prefix_freq = {}
    for i in range(n + 1):
        prefix = S[:i]
        if prefix not in prefix_freq:
            prefix_freq[prefix] = 0
        prefix_freq[prefix] += 1

    dp = [[-1 for _ in range(m)] for _ in range(n)]

    # Fill up the dp table
    for i in range(n):
        for j in range(m):
            if S[i] == T[j]:
                dp[i][j] = 1 + (dp[i - 1][j - 1] if i > 0 and j > 0 else 0)

    # Calculate the length of the shortest subsequence not being a subsequence in T
    for i in range(n):
        for j in range(m):
            if dp[i][j] == -1:
                continue
            prefix = S[:i + 1]
            if prefix_freq.get(prefix, 0) > 0:
                prefix_freq[prefix] -= 1

            # If the current subsequence is not a subsequence in T, update the result
            if all(T[k] != S[i] for k in range(j - dp[i][j] + 1)):
                return i + 1

    return -1


# Example usage:
S = input().strip()
T = input().strip()
print(shortest_common_subsequence(S, T))
