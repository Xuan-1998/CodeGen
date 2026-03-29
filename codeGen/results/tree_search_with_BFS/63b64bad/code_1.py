import sys
from sys import stdin, stdout
import threading

def dfs(i):
    if dp[i] != -2:
        return dp[i]
    dp[i] = -1
    nxt = i + a[i] if i % 2 == 0 else i - a[i]
    if nxt < 1 or nxt > n:
        dp[i] = a[i]
    else:
        tmp = dfs(nxt)
        if tmp == -1:
            dp[i] = -1
        else:
            dp[i] = a[i] + tmp
    return dp[i]

def main():
    global n, a, dp
    n = int(stdin.readline())
    a = [0] + list(map(int, stdin.readline().split()))
    dp = [-2 for _ in range(n+1)]
    for i in range(2, n+1):
        stdout.write(f"{dfs(i)}\n")

sys.setrecursionlimit(10**6)
threading.stack_size(10**8)
thread = threading.Thread(target=main)
thread.start()

