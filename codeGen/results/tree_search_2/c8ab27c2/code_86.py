import sys

def uncommon_subsequence(S, T):
    n, m = len(S), len(T)
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if S[i-1] != T[j-1]:
                dp[i][j] = min(i, dp[i-1][j]) + 1
            else:
                dp[i][j] = dp[i-1][j-1]

    result = -1
    for i in range(n, -1, -1):
        if all(S[k] != T[j] or k >= j for k in range(i)):
            result = i
            break

    return result

if __name__ == "__main__":
    S, T = [line.strip() for line in sys.stdin.readlines()]
    print(uncommon_subsequence(S, T))
