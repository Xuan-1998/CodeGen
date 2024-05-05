import sys

def solve():
    n, m, h = map(int, input().split())
    s = list(map(int, input().split()))

    total_players = sum(s)
    dp = [0] * (n + 1)
    dp[0] = 0

    for i in range(1, n + 1):
        prob = sum(dp[j] for j in range(h, i)) / (total_players - i + 1)
        dp[i] = prob

    print(1 - dp[n])

if __name__ == "__main__":
    solve()
