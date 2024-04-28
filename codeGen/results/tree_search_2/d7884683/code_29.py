def max_partitions():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        
        for i in range(1, n + 1):
            for j in range(i):
                if sum(arr[:j]) == sum(arr[j:]):
                    dp[i][j] = 1 + dp[n-1-i][i-j]
        
        print(max(max(row) for row in dp))

max_partitions()
