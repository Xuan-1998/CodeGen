from collections import defaultdict

def is_path_exists(q):
    graph = defaultdict(list)
    memo = {}

    def dfs(u, k):
        if (u, k) in memo:
            return memo[(u, k)]
        
        res = 0
        for v in graph[u]:
            res += dfs(v, k + 1)
        memo[(u, k)] = res
        return res

    for _ in range(q):
        u, v = map(int, input().split())
        if u > v:
            u, v = v, u
        
        res = 0
        while True:
            if (res, 1) not in memo:
                res += dfs(u, 1)
                break
            u = res
            
        if res >= v:
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    q = int(input())
    is_path_exists(q)
