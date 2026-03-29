import sys

def solve():
    n, m = map(int, input().split())
    table = [list(map(int, input().split())) for _ in range(n)]
    k = int(input())
    tasks = []
    for _ in range(k):
        l, r = map(int, input().split())
        tasks.append((l-1, r-1))

    dp = [False] * n
    for col in range(m):
        prev_max_val = -float('inf')
        for row in range(n):
            if table[row][col] >= prev_max_val:
                dp[row] = True
            prev_max_val = max(prev_max_val, table[row][col])

    for task in tasks:
        l, r = task
        if any(not dp[i] for i in range(l, r+1)):
            print("No")
        else:
            print("Yes")

if __name__ == "__main__":
    solve()
