def main():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    fixed_path = list(map(int, input().split()))
    k = len(fixed_path)

    # Initialize dp table with infinity values
    dp = [float('inf')] * (n + 1)
    for i in range(k):
        dp[fixed_path[i]] = 0

    # Compute dp values
    for i in range(1, n + 1):
        if i not in fixed_path:
            min_recomputations = float('inf')
            for j in range(i):
                if graph[j][i]:
                    min_recomputations = min(min_recomputations, dp[j] + 1)
            dp[i] = min_recomputations

    # Print minimum and maximum recomputations
    print(dp[0], max(dp))

if __name__ == "__main__":
    main()
