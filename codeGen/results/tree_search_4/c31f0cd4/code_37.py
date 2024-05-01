def find_distinct_sums():
    n = int(input())
    arr = list(map(int, input().split()))
    
    # Calculate prefix sum array for efficient calculation of cumulative sums
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i+1] = prefix_sum[i] + arr[i]
        
    # Initialize dp table and set to store distinct sums
    dp = [[0] * (sum(arr) + 1) for _ in range(n + 1)]
    distinct_sums = set()
    
    # Fill the dp table and store distinct sums
    for i in range(1, n + 1):
        for j in range(prefix_sum[i], -1, -1):
            if j > sum(arr): 
                break
            dp[i][j] = dp[i-1][j-arr[i-1]] + (dp[i-1][j] if i > 1 else 1)
            distinct_sums.add(j)
    
    # Print the distinct sums in increasing order
    print(' '.join(map(str, sorted(distinct_sums))))


if __name__ == "__main__":
    find_distinct_sums()
