def makeEqual(arr):
    n = len(arr)
    max_val = max(arr)
    dp = [[False] * (max_val+1) for _ in range(n+1)]
    
    for i in range(1, n+1):
        for k in range(max_val+1):
            if all(a <= arr[i-1] and arr[i-1] >= 0 or dp[i-1][k+(arr[i-1]-k)%2] and all(a < arr[i-1]) for a in arr[:i]):
                dp[i][k] = True
            elif all(a >= arr[i-1] and arr[i-1] <= 0 or dp[i-1][k-(arr[i-1]-k)%2] and all(a > arr[i-1]) for a in arr[:i]):
                dp[i][k] = True
    
    return "YES" if any(dp[n][k] for k in range(max_val+1)) else "NO"

while True:
    n = int(input())
    if n == 0: break
    arr = list(map(int, input().split()))
    print(makeEqual(arr))
