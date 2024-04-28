import sys

def good_sequences(n, k):
    MOD = int(1e9) + 7
    s = [0] * (n+1)
    dp = [0] * (n+1)

    for i in range(1, n+1):
        if i % (i+1) == 0:
            s[i] = 1

    for length in range(2, k+1):
        for end in range(length, n+1):
            dp[end] += sum(s[j] for j in range(1, end))
            dp[end] %= MOD

    return dp[n] % MOD


if __name__ == "__main__":
    n, k = map(int, input().split())
    print(good_sequences(n, k))
