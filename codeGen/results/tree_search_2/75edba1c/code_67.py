from sys import stdin

N, K = map(int, stdin.readline().split())
arr = list(map(int, stdin.readline().split()))

max_seen = max(arr)
count = 0
for i in range(N):
    if arr[i] > K:
        count += (max_seen - arr[i]) + 1
    else:
        max_seen = min(max_seen, arr[i])

print(count)
