import sys
from sys import stdin, stdout

def solve(i, a, dp, visited):
    if i <= 0 or i > n:
        return 0
    if visited[i]:
        if dp[i] == -1:
            return -1
        else:
            return dp[i]
    visited[i] = True
    dp[i] = -1
    tmp = solve(i + a[i-1], a, dp, visited)
    if tmp == -1:
        return -1
    dp[i] = tmp + a[i-1]
    return dp[i]

def main():
    n = int(stdin.readline())
    a = list(map(int, stdin.readline().split()))
    dp = [-1] * (n+1)
    visited = [False] * (n+1)
    for i in range(1, n+1):
        if dp[i] == -1:
            dp[i] = solve(i, a, dp, visited)
        stdout.write(str(dp[i]) + '\n')

if __name__ == "__main__":
    main()

