from sys import stdin, stdout

def dfs(i, a, visited, dp):
    if i <= 0 or i > len(a):
        return 0
    if visited[i]:
        return -1
    if dp[i] != -1:
        return dp[i]
    visited[i] = True
    dp[i] = dfs(i - a[i], a, visited, dp)
    if dp[i] != -1:
        dp[i] += 2 * a[i]
    visited[i] = False
    return dp[i]

def solve():
    n = int(stdin.readline())
    a = [0] + list(map(int, stdin.readline().split()))
    dp = [-1] * (n + 1)
    visited = [False] * (n + 1)
    for i in range(1, n + 1):
        stdout.write(str(dfs(i, a, visited, dp)) + "\n")

solve()

