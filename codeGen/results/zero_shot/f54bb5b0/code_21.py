import sys
sys.setrecursionlimit(100000)

def dfs(node, parent, depth, dp, adj):
    dp[depth][node] = 1
    for neighbor in adj[node]:
        if neighbor != parent:
            dfs(neighbor, node, depth + 1, dp, adj)
            for d in range(k):
                dp[d + 1][node] += dp[d][neighbor]

def count_pairs(node, parent, dp, adj, k):
    count = 0
    for neighbor in adj[node]:
        if neighbor != parent:
            for d in range(k):
                count += dp[d][neighbor] * (dp[k - d - 1][node] - (d + 1 < k and dp[d + 1][neighbor]))
            count += count_pairs(neighbor, node, dp, adj, k)
    return count

if __name__ == "__main__":
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    k = int(data[1])
    
    adj = [[] for _ in range(n + 1)]
    index = 2
    for _ in range(n - 1):
        a = int(data[index])
        b = int(data[index + 1])
        adj[a].append(b)
        adj[b].append(a)
        index += 2
    
    dp = [[0] * (n + 1) for _ in range(k + 1)]
    
    dfs(1, -1, 0, dp, adj)
    
    result = count_pairs(1, -1, dp, adj, k) // 2
    
    print(result)

