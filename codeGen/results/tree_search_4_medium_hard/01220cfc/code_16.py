def canJump(jumps):
    dp = [False] * (len(jumps) + 1)
    dp[0] = True

    for i in range(len(jumps)):
        if dp[i]:
            for j in range(i+1, min(i+2, len(jumps)+1)):
                dp[j] = True
        else:
            break

    return dp[-1]
