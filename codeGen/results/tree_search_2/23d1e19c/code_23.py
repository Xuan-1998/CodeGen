import sys

def main():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    path = list(map(int, input().split()))
    rec_dp = [[(0, 0) for _ in range(len(path) + 1)] for _ in range(n + 1)]

    # Build the graph and initialize the dynamic programming table
    for edge in [list(map(int, input().split())) for _ in range(m)]:
        u, v = edge
        graph[u].append(v)
    rec_dp[0][0] = (0, 0)  # Base case: start with no recomputations

    for i in range(1, n + 1):
        for j in range(len(path) + 1):
            if i == path[j]:
                # Update the dynamic programming table
                rec_dp[i][j] = (min(rec_dp[i - 1][j - 1][0] + 1, rec_dp[i][j - 1][0]), max(rec_dp[i - 1][j - 1][1] + 1, rec_dp[i][j - 1][1]))
            elif j > 0 and i in graph[path[j - 1]]:
                # No need to recompute; copy from the previous vertex
                rec_dp[i][j] = rec_dp[graph[path[j - 1]].index(i)][j - 1]
            else:
                # Recomputation needed; initialize with infinity
                rec_dp[i][j] = (float('inf'), float('-inf'))

    min_recomputation, max_recomputation = rec_dp[n][len(path)]
    print(min_recomputation, max_recomputation)

if __name__ == "__main__":
    main()
