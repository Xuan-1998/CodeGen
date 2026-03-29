def count_ways():
    n = int(input())
    m = list(map(int, input().split()))
    
    # Initialize dp array
    dp = [0] * (n + 1)
    dp[0] = 1
    
    for i in range(1, n):
        prev_dp = dp[i - 1]
        for j in range(i):
            if m[j] < m[i]:
                dp[i] += prev_dp
            elif m[j] > m[i]:
                prev_dp -= prev_dp // (i - j)
        dp[i] %= 10**9 + 7
    
    # Calculate the final answer
    res = 0
    for i in range(n):
        if m[i] == n:
            res += dp[i]
            break
    print(res % (10**9 + 7))

count_ways()
