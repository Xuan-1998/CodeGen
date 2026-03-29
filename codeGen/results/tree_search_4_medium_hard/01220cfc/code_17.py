from collections import defaultdict

def can_reach_last_index(jumps):
    dp = defaultdict(bool)
    dp[0] = True  # base case: we can always reach index 0

    for i in range(1, len(jumps)):
        for j in range(i):
            if dp[j] and (j + jumps[j]) >= i:
                dp[i] = True
                break

    return dp[-1]

# Example usage:
input_jumps = [2, 3, 1, 1, 4]
print(can_reach_last_index(input_jumps))  # Output: True
