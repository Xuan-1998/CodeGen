def max_common_substrings():
    N = int(input())
    str1 = input().strip()
    str2 = input().strip()

    dp = [[False] * (N+1) for _ in range(N+1)]

    for i in range(N):
        for j in range(N):
            if str1[i] == str2[j]:
                dp[i+1][j+1] = dp[i][j] or (i==0 and j==0)
            else:
                dp[i+1][j+1] = False

    max_count = 0
    for i in range(N):
        for j in range(N):
            if dp[i][j]:
                count = 0
                k = i
                while k <= N and str1[k:i+1] == str2[j:j+i-k+1]:
                    count += 1
                    k += 1
                max_count = max(max_count, count)

    print(max_count)
