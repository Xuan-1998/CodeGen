def can_jump(arr):
    n = len(arr)
    dp = [False] * n

    dp[0] = True  # base case: start at the beginning, so any index is reachable
    for i in range(1, n):
        if dp[i-1]:
            jump = arr[i-1]
            for j in range(i-jump, -1, -1):  # iterate from i-jump to 0
                if j == 0:
                    return True  # reached the last index!
                elif dp[j]:
                    break  # found a reachable previous index, so we can reach this one
            else:  # didn't find any reachable previous indices
                dp[i] = False

    return dp[-1]
