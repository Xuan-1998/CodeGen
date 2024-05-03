===BEGIN CODE===
T = int(input())
for _ in range(T):
    n = int(input())
    probs = []
    for _ in range(n):
        probs.append([float(input()), int(input()), int(input())])
    
    dp = [[0.0, 0.0] for _ in range(2)]
    for i in range(1, n+1):
        p0, num0, num1 = probs[i-1]
        dp[0][1] += p0
        dp[1][1] += p0
        
        if i == 1:
            dp[0][0] = p0
            dp[1][0] = 1 - p0
        else:
            for j in range(2):
                if j == 0:
                    dp[j][1] = (1-p0) * max(dp[k][0] for k in range(j)) + p0 * max(dp[k][1] for k in range(j))
                else:
                    dp[j][1] = (1-p0) * max(dp[k][0] for k in range(j)) + p0 * max(dp[k][1] for k in range(j))
    
    print(max(dp[0][1], dp[1][1]))
===END CODE===
