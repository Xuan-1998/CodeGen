import sys; input = lambda:map(int,sys.stdin.readline().split())
inf=10**9+7
def solve():
    n,m,k,*edges=input()
    dp=[[[0]*10005 for _ in range(20005)]for _ in [1]*n]
    max_index=0
    memo={}

    def dfs(i,j):
        if (i,j)in memo:
            return memo[(i,j)]
        if i==j:
            return 0

        res=float('inf')
        for u,v in edges:
            if u==i:
                res=min(res,dfs(u,v)+v-u+1)
            elif v==i:
                res=min(res,dfs(v,u)+u-v+1)

        memo[(i,j)]=res
        return res

    for i in range(n):
        for j in range(i+1,n):
            dp[i][j]=min(dp[u][i]+v-u+1+dp[v][j]for u,v in edges if u==i or v==i)
            max_index=max(max_index,sum(dfs(i,j)for _ in range(j)))
    print(max_index%inf)

solve()
