n = int(input())
arr = list(map(int, input().split()))
DP = [0] * (n+1)
for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            DP[i] = max(DP[i], DP[j]+1)
print(max(DP))
