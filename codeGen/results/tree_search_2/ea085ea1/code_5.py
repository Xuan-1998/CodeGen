def max_common_substrings(str1, str2):
    N = len(str1)
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    
    for i in range(N - 1, -1, -1):
        for j in range(N - 1, -1, -1):
            if str1[i] == str2[j]:
                dp[i][j] = 1
                if i > 0 and j > 0:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + (dp[i][j] == 1)
    
    return sum(1 for row in dp for cell in row if cell)

if __name__ == "__main__":
    str1, str2 = input().split()
    print(max_common_substrings(str1, str2))
