import sys

def solve(n, m, T):
    dp = [[[0, []] for _ in range(T + 1)] for _ in range(n + 1)]

    # Initialize the base case: when t = 0, we can only visit the start vertex (1)
    dp[1][0] = [1, [1]]

    memo = {}

    def dfs(i, t):
        if (i, t) not in memo:
            if i == n:
                result = [1, [n]]
            else:
                result = []
                for j, w in edges[i]:
                    if dp[j][t - w][0] > 0 and t - w >= 0:
                        temp_result = dfs(j, t - w)
                        if len(temp_result[1]) + 1 > len(result[1]):
                            result = [temp_result[0] + 1, temp_result[1] + [i]]
            memo[(i, t)] = result
        return memo[(i, t)]

    edges = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v, w = map(int, sys.stdin.readline().split())
        edges[u].append((v, w))

    result = dfs(1, T)
    print(result[0])
    print(' '.join(map(str, result[1])))

if __name__ == "__main__":
    n, m, T = map(int, sys.stdin.readline().split())
    solve(n, m, T)
