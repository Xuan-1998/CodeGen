def shortest_common_subsequence(S, T):
    m, n = len(S), len(T)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if S[i - 1] == T[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                for k in range(j):
                    if S[i - 1] != T[k]:
                        dp[i][j] = max(dp[i - 1][k], dp[i][j])
                        break

    res = 0
    for i in range(m, 0, -1):
        for j in range(n, 0, -1):
            if S[i - 1] != T[j - 1]:
                res += 1
                break
        else:
            continue
        break

    return m + n - res

if __name__ == "__main__":
    import sys
    S = input().strip()
    T = input().strip()
    print(shortest_common_subsequence(S, T))
