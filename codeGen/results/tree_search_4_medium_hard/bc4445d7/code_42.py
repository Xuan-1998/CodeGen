import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    edges = [list(map(int, input().split())) for _ in range(n-1)]
    
    # Initialize the table
    dp = [[0, 0] for _ in range(n)]
    dp[0][0] = (0, 1)

    # Fill up the table from bottom to top
    for i in range(1, n):
        children = [j for j in range(n) if edges[j-1][0] == i or edges[j-1][1] == i]
        dp[i][0] = sum(dp[child][0] for child in children)
        dp[i][1] = 1 + sum(dp[child][1] for child in children)

    # Calculate the distribution index
    max_distribution_index = sum(a + (n - 1 - i) * b for a, b in dp[1:])
    
    print(max_distribution_index % (10**9 + 7))

solve()
