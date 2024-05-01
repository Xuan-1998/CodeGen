def find_lcs(S, T):
    n = len(S)
    m = len(T)
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if S[i - 1] == T[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[-1][-1]

def find_shortest_uncommon_subsequence(S, T):
    n = len(S)
    m = len(T)

    lcs_length = find_lcs(S, T)
    common_subsequence_length = min(n, m)

    uncommon_subsequence_length = max(0, n - lcs_length) if n >= lcs_length else max(0, m - lcs_length)

    return uncommon_subsequence_length

def main():
    S = input().strip()
    T = input().strip()

    result = find_shortest_uncommon_subsequence(S, T)
    print(result)

if __name__ == "__main__":
    main()
