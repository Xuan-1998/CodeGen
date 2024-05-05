def max_score(arr, k, z):
    n = len(arr)
    dp = [0] * (n + 1)

    for i in range(1, n):
        dp[i] = max(dp[i-1], arr[i-1])
        
    left_moves = min(k, z)
    right_moves = k - left_moves
    
    return dp[n-1] + sum(arr[1+n-left_moves:]) + sum(arr[:n-right_moves])

# Example usage
t = int(input())
for _ in range(t):
    n, k, z = map(int, input().split())
    arr = list(map(int, input().split()))
    print(max_score(arr, k, z))
