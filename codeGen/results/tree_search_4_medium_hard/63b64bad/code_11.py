def dp_program(a):
    n = len(a)
    dp = [[-1 for _ in range(n+1)] for _ in range(n+1)]
    
    for i in range(2, n+1):
        for x in range(1, n+1):
            if a[x-1] <= 0 or a[x-1] > n:
                dp[i][x] = -1
            else:
                last_x = x - a[x-1]
                last_y = y + a[x-1]
                dp[i][x] = dp[i-1][last_x]
                
    return dp[-1][-1]

n = int(input())
a = list(map(int, input().split()))
print(dp_program(a))
