def max_common_substrings():
    N = int(input())
    str1 = input().strip()
    str2 = input().strip()

    dp = [[[0 for _ in range(N)] for _ in range(N)] for _ in range(3)]

    for i in range(N):
        for j in range(i, N):
            for k in range(N):
                for l in range(k, N):
                    if str1[i:j+1] == str2[k:l+1]:
                        dp[0][i][j] = 1
                        dp[1][k][l] = 1

    max_count = 0
    for i in range(N):
        for j in range(i, N):
            if dp[0][i][j] and dp[1][i][j]:
                max_count += 1

    print(max_count)

max_common_substrings()
