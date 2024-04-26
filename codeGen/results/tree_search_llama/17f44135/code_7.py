n, k = map(int, input().split())
a = list(map(int, input().split()))

ans = 0
l = r = 0

while l <= r and r < n:
    if a[l] <= k:
        ans += 1
        l += 1
    else:
        r += 1

print(ans)
