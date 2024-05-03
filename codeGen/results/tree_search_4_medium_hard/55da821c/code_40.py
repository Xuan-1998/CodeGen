import sys

def min_replant(n, m):
    dp = [[float('inf')] * n for _ in range(m)]
    dp[0][n-1] = 0

    for i in range(n):
        s, x = int(input()), float(input())
        section = (s - 1) % m
        remaining_plants = n - 1 - i

        if dp[section][remaining_plants] > dp[section][remaining_plants-1]:
            dp[section][remaining_plants] = dp[section][remaining_plants-1] + 1
        else:
            for j in range(m):
                if dp[j][n-i-1] < float('inf'):
                    dp[j][n-i-1] += 1

    return min(dp[-1])

if __name__ == "__main__":
    n, m = map(int, input().split())
    print(min_replant(n, m))
