import sys
from sys import stdin, stdout

def dfs(v, a, dp, visited, inStack):
    if v <= 0 or v > len(a):
        return 0
    if visited[v]:
        if inStack[v]:
            return -1
        return dp[v]
    visited[v] = True
    inStack[v] = True
    dp[v] = dfs(v + a[v], a, dp, visited, inStack)
    if dp[v] != -1:
        dp[v] += a[v]
    inStack[v] = False
    return dp[v]

def main():
    n = int(stdin.readline())
    a = [0] + list(map(int, stdin.readline().split()))
    dp = [-2 for _ in range(n+1)]
    visited = [False for _ in range(n+1)]
    inStack = [False for _ in range(n+1)]
    for i in range(1, n+1):
        if not visited[i]:
            dp[i] = dfs(i, a, dp, visited, inStack)
    for i in range(1, n+1):
        stdout.write(str(dp[i]) + '\n')

if __name__ == "__main__":
    sys.setrecursionlimit(10**6)
    main()

