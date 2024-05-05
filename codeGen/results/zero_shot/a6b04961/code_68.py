import sys

def read_input():
    n, m = map(int, sys.stdin.readline().split())
    edges = []
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        edges.append((u, v))
    return n, m, edges

def solve(n, m, edges):
    # Create a DP table to store the maximum beauty of a hedgehog with a tail of length i
    dp = [0] * (n + 1)
    
    # Iterate through all edges in the graph and update the DP table accordingly
    for u, v in edges:
        for i in range(min(u, v), n + 1):
            dp[i] = max(dp[i], dp[i - 1] + 1)
    
    # Find the maximum possible beauty of a hedgehog
    max_beauty = 0
    for i in range(n + 1):
        max_beauty = max(max_beauty, dp[i] * (n - i))
    
    return max_beauty

if __name__ == '__main__':
    n, m, edges = read_input()
    print(solve(n, m, edges))
