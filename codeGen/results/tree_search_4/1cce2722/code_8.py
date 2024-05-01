def maximum_points(a):
    n = len(a)
    
    # Initialize dp array with zeros
    dp = [0] * (n + 1)
    
    for i in range(1, n + 1):
        if a[i-1] not in a[:i-1]:
            dp[i] = dp[i-1] + 1
        else:
            k = next((j for j in range(i) if a[j] != a[i-1]), i)
            dp[i] = max(dp[k], dp[i-1])
            
    return dp[n]

n = int(input())
a = list(map(int, input().split()))
print(maximum_points(a))
