import sys

def is_ladder(a):
    n = len(a)
    dp = [[0] * (n+1) for _ in range(n)]

    for i in range(1, n):
        for j in range(i+1):
            if a[j-1] <= a[i]:
                dp[i][j] = max(dp[i-1][k-1] for k in range(j, i+1) if a[k-1] <= a[k]) + 1
            else:
                dp[i][j] = max(0, dp[i-1][j])

    for query in range(int(input())):
        l, r = map(int, input().split())
        s = last_index = r
        while last_index > l and not is_non_decreasing(a[last_index]):
            last_index -= 1

        if is_non_decreasing(a[last_index:l+1]):
            print("Yes")
        else:
            print("No")

def is_non_decreasing(arr):
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            return False
    return True
