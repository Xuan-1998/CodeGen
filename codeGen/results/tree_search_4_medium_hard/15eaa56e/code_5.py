import sys

def check_sorting_order(n, m, k, tasks):
    # Initialize a dynamic programming table with False values
    dp = [[False] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(m):
            if all(x == arr[i - 1][j] for x in arr[i]):
                dp[i][j] = True
            else:
                found_violation = False
                for c2 in range(j, m):
                    violation_found = False
                    for r2 in range(i):
                        if arr[r2][c2] > arr[r2 + 1][c2]:
                            violation_found = True
                            break
                    if not violation_found:
                        found_violation = True
                        break
                dp[i][j] = found_violation

    for task in tasks:
        l, r = task
        for j in range(m):
            if dp[r][j]:
                print("Yes")
                return
        print("No")

# Read input from standard input
n, m = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
k = int(sys.stdin.readline().split()[0])
tasks = [[int(x) for x in sys.stdin.readline().split()] for _ in range(k)]

check_sorting_order(n, m, k, tasks)
