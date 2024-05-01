def max_common_substrings():
    N = int(input())
    str1 = input().strip()
    str2 = input().strip()

    dp = [[False] * (N + 1) for _ in range(N + 1)]
    
    max_count = 0
    
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] or (i == 1 and j == 1)
            else:
                dp[i][j] = False
                
            if dp[i][j] and i < N and j < N:
                max_count += 1
    print(max_count)

max_common_substrings()
