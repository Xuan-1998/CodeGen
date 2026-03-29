import sys

def max_path_sum(tree):
    N = len(tree)
    dp = [[0] * N for _ in range(N)]

    # Initialize the first row as the values of each node
    for i in range(N):
        dp[0][i] = tree[i]

    # Traverse the left subtree (from root to leaf) and update dp[i][j]
    for i in range(1, N):
        for j in range(i+1):
            if 2*i < N:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + tree[2*i]
            else:
                dp[i][j] = dp[i-1][j]

    # Traverse the right subtree (from root to leaf) and update dp[i][j]
    for i in range(1, N):
        for j in range(i+1, N):
            if 2*i + 1 < N:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + tree[2*i+1]
            else:
                dp[i][j] = dp[i-1][j]

    # The final result is stored in dp[0][N-1], representing the maximum sum of paths
    return max(dp[0])

def read_input():
    N = int(input())
    tree = [int(x) for x in input().split()]
    return tree

if __name__ == "__main__":
    tree = read_input()
    print(max_path_sum(tree))
