def max_joy(n):
    # Read input from stdin
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))

    dp = [[[0] * 2 for _ in range(2)] for _ in range(n)]

    # Initialize base case: no hares fed
    dp[0][False][False] = 0

    for i in range(1, n):
        # For each hare, consider three options:
        # 1. Feed if both adjacent hares are hungry
        # 2. Don't feed if left neighbor is full and right neighbor is hungry
        # 3. Don't feed if both neighbors are full
        dp[i][True][True] = max(dp[i-1][False][False] + a[i], 
                                 dp[i-1][False][True] + b[i], 
                                 dp[i-1][False][False] + c[i])
        
        # For each hare, consider two options:
        # 1. Feed if left neighbor is hungry and right neighbor is full
        # 2. Don't feed
        dp[i][False][True] = max(dp[i-1][True][False] + b[i], 
                                   dp[i-1][False][True])
        
        # For each hare, consider two options:
        # 1. Feed if both neighbors are full
        # 2. Don't feed
        dp[i][False][False] = max(dp[i-1][False][False] + c[i], 
                                   dp[i-1][False][False])

    # Return the maximum joy
    return max([dp[i][True][True] for i in range(n)])

# Read input from stdin and print output to stdout
n = int(input())
print(max_joy(n))
