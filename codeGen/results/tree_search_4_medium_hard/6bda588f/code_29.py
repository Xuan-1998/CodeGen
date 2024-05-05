def min_possible_value():
    t = int(input())  # number of test cases
    for _ in range(t):
        n, s = map(int, input().split())
        a = list(map(int, input().split()))
        dp = [0] * (n + 1)
        
        for i in range(1, n + 1):
            F_inc = dp[i-1] - s * a[i]
            F_exc = dp[i-1] + (a[i] - s) * (a[i] - s)
            dp[i] = min(F_inc, F_exc)
        
        print(dp[n])

min_possible_value()
