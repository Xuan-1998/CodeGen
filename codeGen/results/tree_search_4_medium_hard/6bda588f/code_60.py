def min_sum_of_function(s):
    n = int(input())
    a = list(map(int, input().split()))
    dp = [0] * (n + 1)
    for i in range(2, n):
        left_sum = sum(a[:i])
        right_sum = sum(a[i:])
        if i % 2 == 0:
            dp[i] = min(dp[i-1] + a[i//2] * s + (right_sum - 2*s), dp[i-2] + a[i//2-1] * (s-a[i//2]) + (right_sum - 2*s))
        else:
            dp[i] = min(dp[i-1] + a[(i+1)//2] * s + (left_sum - 2*s), dp[i-2] + a[(i-1)//2] * (s-a[(i+1)//2]) + (left_sum - 2*s))
    return dp[n-1]
