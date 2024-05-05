def canCross(stones):
    dp = [False] * len(stones)
    dp[0] = True

    for i in range(1, len(stones)):
        if not dp[i]:
            continue
        minJump = float('inf')
        for j in range(i+1, len(stones)):
            jump = stones[j] - stones[i]
            if abs(jump) <= 2:
                minJump = min(minJump, jump)
        if minJump != float('inf') or dp[minJump-1]:
            dp[j] = True

    return dp[-1]

# Example usage
stones = list(map(int, input().split()))
print(canCross(stones))
