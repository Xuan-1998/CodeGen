import sys
from sys import stdin, stdout

def simulate(n, a):
    dp = [-1 for _ in range(n+1)]
    visited = [False for _ in range(n+1)]
    
    def dfs(i):
        if i <= 0 or i > n:
            return 0
        if visited[i]:
            return -1
        visited[i] = True
        dp[i] = dfs(i + a[i-1])
        if dp[i] != -1:
            dp[i] += a[i-1]
        visited[i] = False
        return dp[i]
    
    for i in range(1, n+1):
        if dp[i] == -1:
            dp[i] = dfs(i)
    
    return dp[1:]

def main():
    n = int(stdin.readline())
    a = list(map(int, stdin.readline().split()))
    result = simulate(n, a)
    for res in result:
        stdout.write(str(res) + '\n')

if __name__ == "__main__":
    main()

