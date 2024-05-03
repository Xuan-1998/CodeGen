def can_make_zero():
    n = int(input())
    arr = list(map(int, input().split()))
    
    dp = [False] * (n + 1)
    dp[0] = True
    
    for i in range(1, n + 1):
        if not dp[i - 1]:
            continue
        
        start_diff = end_diff = float('inf')
        
        for j in range(i):
            curr_diff = abs(arr[j] - arr[i - 1])
            if curr_diff < start_diff:
                start_diff = curr_diff
            elif curr_diff > end_diff:
                end_diff = curr_diff
                
        if min(start_diff, end_diff) == float('inf'):
            dp[i] = True
    
    return "YES" if dp[n - 1] else "NO"


while True:
    print(can_make_zero())
