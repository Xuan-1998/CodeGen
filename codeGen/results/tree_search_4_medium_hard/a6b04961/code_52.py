import sys
from collections import defaultdict

def max_hedgehog_beauty(n, m, edges):
    # Initialize memoization table with default value of 0
    memo = {(i, 0): 0 for i in range(1, n + 1)}

    for u, v in edges:
        for j in range(i := min(u, v), max(u, v) + 1):
            # Update memoization table based on the state transition rules
            memo[(j, len(memo)) if memo.get((j, 0)) else (j, i)] = max(
                memo.get((j, k - 1), k) * min(k, n - k) for k in range(1, i + 1)
            )

    return max(memo.values())

if __name__ == "__main__":
    with open("input.txt", "r") as f:
        n, m = map(int, f.readline().split())
        edges = [map(int, line.split()) for line in f.readlines()]
    
    print(max_hedgehog_beauty(n, m, edges))
