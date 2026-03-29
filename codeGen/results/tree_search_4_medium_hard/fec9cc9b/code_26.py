from sys import stdin

def is_ladder(arr, l, r):
    n = len(arr)
    dp = [[True] * (r - l + 1) for _ in range(n + 1)]

    # Initialize dp[0][j] = True for 0 <= j < n
    for j in range(r - l + 1):
        if arr[l - 1] > arr[j]:
            return False

    for i in range(1, n + 1):
        for j in range(i, r - l + 1):
            if arr[i - 1] <= arr[j]:
                dp[i][j - l] = True
            else:
                break

    return "Yes" if dp[-1][-1] else "No"

n, m = map(int, stdin.readline().split())
arr = list(map(int, stdin.readline().split()))

for _ in range(m):
    l, r = map(int, stdin.readline().split())
    print(is_ladder(arr, l, r))
