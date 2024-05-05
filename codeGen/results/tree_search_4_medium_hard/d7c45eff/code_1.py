from itertools import combinations

def solve(n, k):
    s = input().strip()
    dp = [[0] * (k + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(min(i, k) + 1):
            if j == 0:
                # Base case: empty string
                dp[i][j] = 1
            elif j == 1:
                # One character; we can only delete or duplicate the entire string
                dp[i][j] = 1 if s[i - 1] <= s[0] else 2
            else:
                # More than one character; consider deleting or duplicating
                if j > i // 2:
                    # If there are more characters to come, it's better to duplicate
                    dp[i][j] = min(dp[i - 1][k - j], 2)
                else:
                    # Otherwise, we can delete the last character and consider the remaining string
                    dp[i][j] = min(dp[i - 1][j - 1] + (s[i - 1] <= s[0]), dp[i - 1][k - j] + (s[i - 1] >= s[0]))

    return ''.join(c for c, count in sorted((c, count) for c, count in combinations(s, k)))

if __name__ == "__main__":
    n, k = map(int, input().split())
    print(solve(n, k))
