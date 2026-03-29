import sys

n, k, m = map(int, input().split())
a = list(map(int, input().split()))

a.sort()

start = 0
end = 0

for i in range(1, n):
    if a[i] - a[start] > m:
        end = i - 1
        partitions += 1
        start = i

if end < n - 1 and a[n-1] - a[end] > m:
    partitions += 1

print(partitions >= k)
