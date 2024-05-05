from sys import stdin

arr = list(map(int, stdin.readline().split()))
n = len(arr)

dp = [False] * (n + 1)
dp[0] = True

for i in range(1, n + 1):
    for j in range(i):
        if arr[j] >= i - j and dp[j]:
            dp[i] = True
            break

if dp[-1]:
    print(True)
else:
    print(False)
