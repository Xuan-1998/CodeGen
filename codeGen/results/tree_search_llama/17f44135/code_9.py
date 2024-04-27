n, k = map(int, input().split())
a = list(map(int, input().split()))
left, right = 0, n-1
ans = 0

while left <= right:
    if a[left] <= k and a[right] <= k:
        ans += 1
        left += 1
        right -= 1
    elif a[left] > k:
        right -= 1
    else:
        left += 1

print(ans)
