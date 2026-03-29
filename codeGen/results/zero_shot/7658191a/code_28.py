def solve():
    t = int(input())
    for _ in range(t):
        n, k, z = map(int, input().split())
        arr = list(map(int, input().split()))
        
        # Initialize the dp array with zeros
        dp = [0] * (k + 1)
        
        # Iterate over the possible number of moves
        for i in range(1, k + 1):
            # Check if we can perform a move to the left
            if i - z >= 0:
                dp[i] = max(dp[i], dp[i - z] + arr[i - z])
            
            # Check if we can perform a move to the right
            dp[i] = max(dp[i], dp[i - 1] + arr[i])
        
        print(max(dp))

solve()
