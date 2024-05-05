import sys

def min_changes():
    n, k = map(int, input().split())
    s = input()

    dp = [[0] * (k + 1) for _ in range(n + 1)]
    base_case = sum(1 for c in s[:k - 1] if c not in 'RGB')

    for i in range(1, n + 1):
        for j in range(min(i, k), 0, -1):
            mismatch_count = 0
            for char in s[i - j:i]:
                match_count = sum(1 for c in 'RGB' if c == char)
                if match_count == 0:
                    mismatch_count += 1
                dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j - 1] + (k - j), dp[i - j][j - 1] + mismatch_count)

    print(dp[n - k + 1][k - 1])

if __name__ == "__main__":
    min_changes()
