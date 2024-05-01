    ===BEGIN CODE===


    def main():
        n, m = map(int, input().split())
        graph = [[] for _ in range(n+1)]
        for i in range(m):
            u, v = map(int, input().split())
            graph[u].append(v)
        
        k = int(input())
        path = list(map(int, input().split()))
        dp = [[0]*10001 for _ in range(n+1)]


        def dfs(i, j):
            if i == n:
                return [j, 0]
            if dp[i][j] != 0:
                return dp[i][j]

            res = []
            for v in graph[i]:
                if v in path:
                    res.append(min(dfs(v, j+1)))
                else:
                    res.append([min(dfs(v, j+1))]+[1])
            dp[i][j] = min(res), max(res)
            return dp[i][j]


        print(min(dfs(path[0], 0)), max(dfs(path[0], 0)))

    if __name__ == "__main__":
        main()
    ===END CODE===

