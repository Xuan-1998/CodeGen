from sys import stdin, stdout

n = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))
dp = [1]*n
for i in range(1, n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j]+1)
lis = max(dp)
print(lis)
