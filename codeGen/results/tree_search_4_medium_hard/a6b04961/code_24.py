import sys

def read_input():
    n, m = map(int, sys.stdin.readline().split())
    edges = []
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        edges.append((u, v))
    return n, m, edges

def solve(n, m, edges):
    memo = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        if i == 1:
            degree_sum = sum(dgree == 2 for _, v in edges)
        else:
            degree_sum = sum(degree == 2 for u, v in edges if u < i and v >= i)
        memo[i][i] = degree_sum
    for length in range(2, n + 1):
        for start in range(n - length + 1):
            end = start + length
            if start != end:
                memo[end][end] = max(memo[start][start] + (degree_sum := sum(degree == 2 for u, v in edges if u >= start and v <= end)), memo[end-1][end-1])
    return memo[n][n]

def main():
    n, m, _ = read_input()
    print(solve(n, m, []))

if __name__ == "__main__":
    main()
