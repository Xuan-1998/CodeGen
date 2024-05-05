def canJump(arr):
    n = len(arr)
    dp = {0: True}
    
    for i in range(1, n):
        if not dp.get(i-1):
            continue
        
        max_jump = 0
        for j in range(i-1, -1, -1):
            if arr[j] + 1 > i and j <= i-1:
                max_jump = j
            elif max_jump >= j:
                break
        dp[i] = (max_jump >= i) or dp.get(max_jump, False)
    
    return dp[n-1]
