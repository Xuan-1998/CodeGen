def solve():
    N = int(input())
    str1 = input().strip()
    str2 = input().strip()

    dp = [[False] * (N + 1) for _ in range(N + 1)]

    max_common_substrings = 0

    for i in range(N, -1, -1):
        for j in range(N, -1, -1):
            if str1[i] == str2[j]:
                dp[i][j] = True
                max_common_substrings += 1
                if i > 0 and j > 0:
                    dp[i-1][j-1] = True

    print(max_common_substrings)

solve()
