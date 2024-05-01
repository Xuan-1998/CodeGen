dp = [0] * (n+1)
for i in range(1, n+1):
    max_points = 0
    for k in range(i-1, -1, -1):  # adjust the range to include k=i-2 as well
        if a[i-1] == a[k]:  # check if current element is equal to the one being considered for deletion
            max_points = max(max_points, dp[k-1] + i-k-1)  # update maximum points
    dp[i] = max(dp[i-1], max_points)
