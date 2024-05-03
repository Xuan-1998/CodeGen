def canMakeZero(arr):
    n = len(arr)
    total_sum = sum(arr)
    if total_sum % (n+1) != 0:
        return False
    
    target_sum = total_sum // (n+1)
    current_sum = 0
    for num in arr:
        current_sum += num
        if current_sum > target_sum:
            return False
    return True

def dp(arr):
    n = len(arr)
    dp = [False] * (n + 1)
    dp[0] = canMakeZero(arr[:])
    
    for i in range(1, n+1):
        dp[i] = (dp[i-1] and canMakeZero(arr[i:])) or (canMakeZero(arr[:i]) and dp[n-i])
    
    return dp[-1]

while True:
    try:
        n = int(input())
        arr = list(map(int, input().split()))
        
        if dp(arr):
            print("YES")
        else:
            print("NO")
    except EOFError:
        break
