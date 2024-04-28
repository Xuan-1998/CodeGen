def findShortestSubArray(S):
    T = set(T)  # Convert string T into a set for O(1) lookups

    dp = [0] * len(S)
    max_length = 0
    start_idx = end_idx = None

    for i in range(len(S)):
        if S[i] not in T:
            if start_idx is None:
                start_idx = i
            end_idx = i
            while end_idx + 1 < len(S) and S[end_idx + 1] not in T:
                end_idx += 1

            for j in range(start_idx, end_idx + 1):
                dp[j] = 1

        max_length = max(max_length, end_idx - start_idx + 1)

    return max_length
