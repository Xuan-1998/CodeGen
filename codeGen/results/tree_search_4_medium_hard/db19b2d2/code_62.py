import sys

def solve(n, m, h, s):
    total_players = sum(s)
    if total_players < n:
        return -1

    dp = [0] * (m + 1)
    dp[0] = 1  # Base case: probability is 1 when there are no departments
    for i in range(1, m + 1):
        s_sum = sum(s[:i])
        if s_h := s[h - 1]; s_h > 0:
            dp[i] = 1 - (n-1) * (1 - dp[i-1]) / i
        else:
            dp[i] = dp[i-1]
    return 1 - dp[m]

if __name__ == "__main__":
    n, m, h = map(int, sys.stdin.readline().split())
    s = list(map(int, sys.stdin.readline().split()))
    print(solve(n, m, h, s))
