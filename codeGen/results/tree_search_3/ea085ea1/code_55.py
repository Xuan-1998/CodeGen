def findMaxCommonSubstrings():
    N = int(input())
    str1 = input().strip()
    str2 = input().strip()

    dp = [[False] * (N+1) for _ in range(N+1)]
    max_common_substrings = 0

    for i in range(1, N+1):
        for j in range(i, N+1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]
                if not (dp[i-1][j-1]):
                    max_common_substrings += 1
            else:
                dp[i][j] = False

    return max_common_substrings

print(findMaxCommonSubstrings())
