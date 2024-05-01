import sys

def solve():
    n, m = map(int, input().split())
    edges = []
    for _ in range(m):
        u, v = map(int, input().split())
        edges.append((u, v))
    
    k = int(input())
    path = list(map(int, input().split()))
    
    dp = [sys.maxsize] * (n + 1)
    dp[0] = 0
    
    for i in range(1, n + 1):
        min_recompute = sys.maxsize
        for j in range(len(path) - 1):
            if path[j] == i:
                k_after_i = len(path) - j - 1
                recompute_if_follow = dp[path[j - 1]] + 1
                recompute_if_not_follow = dp[0] + k_after_i
                min_recompute = min(min_recompute, recompute_if_follow, recompute_if_not_follow)
        dp[i] = min_recompute
    
    print(min(dp), max(dp))

if __name__ == "__main__":
    solve()
