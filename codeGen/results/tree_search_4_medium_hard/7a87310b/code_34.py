def count_matrices():
    t = int(input())
    for _ in range(t):
        n = int(input())
        dp = [0]*(n+1)
        pos_dp = [0]*(n+1)
        dp[1] = 1  # Base case: there's one matrix with trace 1
        pos_dp[1] = 1  # Same as above

        for i in range(2, n+1):
            if i % 2 == 0:
                pos_dp[i] = 0  # If i is even, there are no matrices with a positive determinant
            else:
                pos_dp[i] = dp[i-1]
            for j in range(i-2, -1, -1):
                if i-j > 0 and (i-j) % 2 == 1:  
                    if pos_dp[j] * (dp[i-j-1]) >= 1:
                        pos_dp[i] += pos_dp[j] * (dp[i-j-1])
            dp[i] = sum(dp[j] * (dp[k]) for j in range(i-2) for k in range(i-2)) + dp[(i+1)//2]

        print(pos_dp[n])

count_matrices()
