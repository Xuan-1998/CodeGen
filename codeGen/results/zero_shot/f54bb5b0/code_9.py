python
import sys
from collections import defaultdict, deque

sys.setrecursionlimit(100000)

def dfs(node, parent, depth, dp, adj):
    dp[node][0] = 1
    for neighbor in adj[node]:
        if neighbor == parent:
            continue
        dfs(neighbor, node, depth + 1, dp, adj)
        for d in range(k):
            dp[node][d + 1] += dp[neighbor][d]

def count_pairs(node, parent, dp, adj):
    count = 0
    for neighbor in adj[node]:
        if neighbor == parent:
            continue
        count += count_pairs(neighbor, node, dp, adj)
        for d in range(k - 1):
            count += dp[neighbor][d] * (dp[node][k - 1 - d] - dp[neighbor][k - 2 - d])
    count += dp[node][k]
    return count

def main():
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    k = int(data[1])
    
    adj = defaultdict(list)
    index = 2
    
    for _ in range(n - 1):
        a = int(data[index])
        b = int(data[index + 1])
        adj[a].append(b)
        adj[b].append(a)
        index += 2
    
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    
    dfs(1, -1, 0, dp, adj)
    
    result = count_pairs(1, -1, dp, adj) // 2
    
    print(result)

if __name__ == "__main__":
    main()

