    def maximum_points(n):
        a = [int(x) for x in input().split()]
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        
        for i in range(1, n + 1):
            if a[i - 1] == a[0]:
                dp[i][0] = max(dp[i - 1][0], dp[i - 1][1])
            else:
                dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + (a[i - 1] != a[0]))
        
        return dp[-1][-1]
    
    if __name__ == "__main__":
        n = int(input())
        print(maximum_points(n))
