from collections import defaultdict

def solve():
    n, m = map(int, input().split())
    graph = defaultdict(list)
    
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    
    memo = [[[0] * (n + 1) for _ in range(n + 1)] for _ in range(2)]
    
    def dfs(node, max_length, in_tail):
        if node == n:
            return 0
        
        if not in_tail or max_length > len(memo[0]):
            return -float('inf')
        
        if memo[not in_tail][node][max_length] != 0:
            return memo[not in_tail][node][max_length]
        
        ans = 0
        for neighbor in graph[node]:
            if not in_tail and neighbor >= node:
                continue
            
            beauty = dfs(neighbor, max_length + 1, not in_tail) * (node + 1)
            if ans < beauty:
                ans = beauty
        
        memo[not in_tail][node][max_length] = ans
        return ans
    
    print(dfs(0, 0, True))

if __name__ == "__main__":
    solve()
