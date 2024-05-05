code
n, k, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()

i = 0
while i < n:
    j = i + 1
    while j < n and a[j] - a[i] <= m:
        j += 1
    if j - i >= k:
        print(True)
        break
    i = j
if i == n - 1:
    print(False)
