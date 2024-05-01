def uncommon_subsequences(S, T):
    # Initialize the memoization dictionary with default values for all possible states (i, k)
    memo = {(i, k): float('inf') for i in range(len(S) + 1) for k in range(len(T) + 1)}

    def dp(i, k):
        if k == len(T):
            return -memo[(i, k)]
        if i == len(S):
            return -len(T) if k else -1

        # Transition from state (i, k) to state (i+1, k+1) if the character at index i in S matches with the next character in T
        if i < len(S) and T[k] == S[i]:
            return min(dp(i + 1, k + 1), -memo[(i, k)])
        # Stay in the same state if they don't match
        else:
            return dp(i + 1, k)

    # Find the shortest uncommon subsequence by iterating over all possible states (i, k) in the dictionary
    res = min(dp(0, 0), key=lambda x: -x)
    return res

S = input().strip()
T = input().strip()

print(uncommon_subsequences(S, T))
