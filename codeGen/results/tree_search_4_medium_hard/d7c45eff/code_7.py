def find_lexicographically_smallest_string(n, k, s):
    dp = [[[] for _ in range(k+1)] for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, min(i+1, k+1)):
            if j == 0:
                dp[i][j] = [''] * (i+1)
            elif i < k and j == 1:
                dp[i][j] = [s[:i]]
            else:
                if s[i-1] <= s[0]:
                    dp[i][j] = [s[:i]] + dp[i-1][min(j-1, k)]
                else:
                    dp[i][j] = dp[i-1][j]

    return ''.join(min(dp[n][k], key=lambda x: (len(x), x)))

if __name__ == '__main__':
    n, k = map(int, input().split())
    s = input()
    print(find_lexicographically_smallest_string(n, k, s))
