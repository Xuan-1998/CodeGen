import sys

n, m = map(int, input().split())
a = list(map(int, input().split()))
dp = [[0] * (m + 1) for _ in range(n + 1)]
lastDecreasingElement = [[-1] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(i + 1):
        if a[j - 1] >= a[j]:
            lastDecreasingElement[i][j] = a[j - 1]
            dp[i][j] = (dp[i-1][j-1] > 0) and (a[j - 1] >= a[r]) and not isIncreasing(a, j, r)

for _ in range(m):
    l, r = map(int, input().split())
    if dp[l-1][r-l+1]:
        print("Yes")
    else:
        print("No")

def isNonDecreasing(a, l, r):
    for k in range(l, r + 1):
        if a[k - 1] > a[k]:
            return False
    return True

def isIncreasing(a, l, r):
    for k in range(l, r + 1):
        if a[k - 1] < a[k]:
            return False
    return True
