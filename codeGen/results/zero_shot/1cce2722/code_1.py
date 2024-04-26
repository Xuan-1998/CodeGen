def max_points(n, arr):
    max_val = max(arr)
    counts = [0] * (max_val + 1)
    for num in arr:
        counts[num] += num
    
    dp = [0] * (max_val + 1)
    dp[1] = counts[1]
    
    for i in range(2, max_val + 1):
        dp[i] = max(dp[i-1], dp[i-2] + counts[i])
    
    return dp[max_val]

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split()))
    print(max_points(n, arr))
