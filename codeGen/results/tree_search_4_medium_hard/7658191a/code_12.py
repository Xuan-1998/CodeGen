def max_score():
    t = int(input())
    for _ in range(t):
        n, k, z = map(int, input().split())
        arr = list(map(int, input().split()))
        
        # Initialize dp and prev arrays
        dp = [0] * (n + 1)
        prev = [-1] * (n + 1)
        
        # Calculate maximum score for each number of moves
        for j in range(1, k + 1):
            for i in range(j, n + 1):
                if j <= z:
                    dp[i] = max(dp[i - 1] + arr[i - 1], dp[i - 1] + arr[i])
                else:
                    dp[i] = max(dp[i - 1] + arr[i], dp[i - 1] + arr[i - 1])
        
        # Print the maximum score that can be achieved
        print(dp[-1])

max_score()
