import sys

def main():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(m)]
    k = int(input())
    path = list(map(int, input().split()))
    
    memo = {}
    
    def dfs(u):
        if (u,) in memo:
            return memo[(u,)]
        
        dp_u_t = [[float('inf'), 0] for _ in range(n)]
        for i, v in enumerate(path):
            if u == v:
                continue
            for p in path[i+1:]:
                if p == v:
                    continue
                for j, w in enumerate(edges):
                    if edges[j][0] == u and edges[j][1] == v:
                        dp_u_t[v][0] = min(dp_u_t[v][0], dp_u_t[u][0] + 1)
                        dp_u_t[v][1] = max(dp_u_t[v][1], dp_u_t[u][1] + 1)
        
        memo[(u,)] = dp_u_t
        return dp_u_t
    
    res = dfs(0)
    
    print(min(res[-1][1], res[-1][0]), max(res[-1][1], res[-1][0]))

if __name__ == "__main__":
    main()
