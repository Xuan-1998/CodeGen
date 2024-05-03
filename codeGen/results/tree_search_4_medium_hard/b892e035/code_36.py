import sys

def calculate_probability():
    T = int(input())
    for _ in range(T):
        n = int(input())
        P = [0] * 17  # initialize probabilities for each number (0-16)
        for i in range(n):
            p, a, b = map(int, input().split())
            P[a] += p
            P[b] += p

        dp = [[0.0] * (n+1) for _ in range(n+1)]
        seen = set()

        # base cases
        dp[0][0] = 1.0
        for j in range(1, n+1):
            dp[0][j] = 0.0

        for i in range(1, n+1):
            for j in range(min(i, len(seen)+1)):
                if P[a-1] > 0:
                    # consider the case where this ticket has a unique number
                    p_unique = P[a-1] * dp[i-1][j]
                    p_duplicate = (1-P[a-1]) * sum(dp[i-1][k] for k in range(j+1))
                    dp[i][j] = max(p_unique, p_duplicate)
                else:
                    # this ticket has a repeated number, so no change
                    dp[i][j] = dp[i-1][j]

            seen.add(a)
            P[a-1] -= 1

        print("%.6f" % (dp[n][n]))

if __name__ == "__main__":
    calculate_probability()
