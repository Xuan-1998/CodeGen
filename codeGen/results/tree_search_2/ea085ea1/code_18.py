def common_substrings(str1, str2):
    N = len(str1)
    dp = [[[0] * 3 for _ in range(N)] for _ in range(N)]
    
    max_count = 0
    
    for i in range(1, N+1):
        for j in range(1, N+1):
            if str1[i-1] == str2[j-1]:
                dp[i][j][0] = min(dp[i-1][j-1][0]+1, dp[i-1][j-1][1], dp[i-1][j-1][2]) + 1
            else:
                dp[i][j][0] = max(dp[i-1][j-1][0]-1, dp[i-1][j-1][1], dp[i-1][j-1][2])
                
            if i < N and j < N:
                for k in range(3):
                    dp[i+1][j+1][k] = max(dp[i+1][j+1][k], dp[i][j][k])
    
    return max_count

str1 = input()
str2 = input()

print(common_substrings(str1, str2))
