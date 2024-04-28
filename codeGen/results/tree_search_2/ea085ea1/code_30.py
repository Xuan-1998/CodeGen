def max_common_substrings():
    N = int(input())
    str1 = input().strip()
    str2 = input().strip()

    dp = [[0] * (N + 1) for _ in range(N + 1)]

    for k in range(1, N + 1):
        start, end = 0, 0
        max_len = 0
        while start <= N - k:
            while end < N and str1[start:start+k] == str2[end:end+k]:
                if k > max_len:
                    max_len = k
                end += 1
            dp[end][N] = max(dp[max_len-1][end], dp[max_len-1][start])
            start += 1

    print(dp[N][N])

max_common_substrings()
