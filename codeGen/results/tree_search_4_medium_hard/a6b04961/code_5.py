import sys

def hedgehog_beauty(n, m, edges):
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for v in range(1, n + 1):
            if i == 1:
                dp[i][v] = 1
            else:
                prev_beauty = 0
                for prev_v in range(1, n + 1):
                    if prev_v != v and edges.count((prev_v, v)) > 0:
                        prev_beauty = max(prev_beauty, dp[i - 1][prev_v])
                dp[i][v] = max(dp[i - 1][v], prev_beauty + 1)

    return max(max(row) for row in dp)


def read_input():
    n, m = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(m)]
    return n, m, edges


if __name__ == "__main__":
    n, m, edges = read_input()
    print(hedgehog_beauty(n, m, edges))
