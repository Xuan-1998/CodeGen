from collections import defaultdict

def max_common_substrings(str1, str2):
    n = len(str1)
    m = len(str2)

    memo = [[[0] * (m + 1) for _ in range(n + 1)] for _ in range(3)]

    for i in range(n + 1):
        for j in range(m + 1):
            if i == 0 and j == 0:
                continue
            memo[0][i][j] = 0

    for k in range(1, n + 1):
        for i in range(k, -1, -1):
            for j in range(min(m, k), -1, -1):
                if str1[i - 1] == str2[j - 1]:
                    memo[0][i][j] = max(memo[0][i - 1][j - 1], memo[0][i - 1][j])
                else:
                    memo[0][i][j] = max(memo[0][i - 1][j], memo[0][i][j - 1])

    result = 0
    for k in range(n + 1):
        for i in range(k, -1, -1):
            for j in range(min(m, k), -1, -1):
                if str1[i - 1] == str2[j - 1]:
                    memo[1][i][j] = max(memo[1][i - 1][j - 1], memo[1][i - 1][j])
                else:
                    memo[1][i][j] = max(memo[1][i - 1][j], memo[1][i][j - 1])

    return memo[0][n][m]

if __name__ == "__main__":
    str1, str2 = input().split()
    print(max_common_substrings(str1, str2))
