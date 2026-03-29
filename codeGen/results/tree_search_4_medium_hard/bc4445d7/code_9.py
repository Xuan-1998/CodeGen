def solve():
    n = int(input())
    edges = []
    for _ in range(n - 1):
        u, v = map(int, input().split())
        edges.append((u, v))

    m = int(input())
    prime_factors = list(map(int, input().split()))

    # Initialize dp array
    dp = [[[False] * (10**6 + 7) for _ in range(n)] for _ in range(n)]

    # Update dp array
    for i, j in edges:
        for k in range(1, max(i, j)):
            if sum(label for label in range(k+1, j+1)) % k == 0:
                dp[i][j][k] = True

    # Calculate maximum possible distribution index
    max_distribution_index = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            label_sum = sum(dp[u][v][label] * label for u, v in edges for label in range(1, 10**6 + 7))
            max_distribution_index += label_sum % (10**9 + 7)

    print(max_distribution_index % (10**9 + 7))

if __name__ == "__main__":
    solve()
