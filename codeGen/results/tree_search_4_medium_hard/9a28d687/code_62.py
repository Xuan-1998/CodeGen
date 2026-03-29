import sys

def main():
    n = int(sys.stdin.readline().strip())
    costs = list(map(int, sys.stdin.readline().split()))
    strings = [sys.stdin.readline().strip() for _ in range(n)]

    dp = [[0] * len(strings[0]) for _ in range(n + 1)]
    dp[0][i] = costs[i] if i < len(costs) else 0 for i in range(len(costs))]

    for i in range(1, n + 1):
        for j in range(len(strings[0])):
            if strings[i - 1] <= strings[j]:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = min(dp[i - 1][len(strings[0]) - 1] + costs[len(costs) - 1], 
                               min((dp[k][j] + costs[j]) for k in range(i)))

    if dp[n][len(strings[0]) - 1] == float('inf'):
        print(-1)
    else:
        print(dp[n][len(strings[0]) - 1])

if __name__ == "__main__":
    main()
