from collections import defaultdict

def find_max_common_substrings():
    N = int(input())
    str1, str2 = input().strip(), input().strip()

    dp = [[0] * (N + 1) for _ in range(2)]

    memo = defaultdict(int)

    for i in range(N):
        for j in range(i + 1):
            if str1[j:i+1] == str2[i-j:i+1]:
                dp[0][i - j + 1] = max(dp[0][i - j], dp[0][j])
                dp[1][i - j + 1] = max(dp[1][i - j], dp[1][j])

    return sum(max(dp[0]), max(dp[1]))

print(find_max_common_substrings())
