def can_reach_last_index(jumps):
    n = len(jumps)
    dp = {0: True}  # base case: always possible to reach the first index

    for i in range(1, n):
        max_jump = jumps[i]
        if max_jump >= i - dp.get(i-1, False):  # check if previous index is reachable
            dp[i] = dp.get(i-1, False)  # update dp with the result from the previous index

    return dp.get(n-1, False)  # return whether it's possible to reach the last index


# Example usage:
jumps = [2, 3, 0, 1, 4]
print(can_reach_last_index(jumps))  # Output: True
