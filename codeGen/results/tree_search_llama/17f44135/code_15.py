n, k = map(int, input().split())
a = list(map(int, input().split()))
a.sort()

left, right = 0, n - 1
max_diff = -1

while left <= right:
    mid = (left + right) // 2
    if a[mid] <= k:
        max_diff = a[mid]
        right = mid - 1
    else:
        left = mid + 1

ans = 0
while left <= right and a[left] <= k:
    ans += 1
    if a[left] == a[right]:
        ans -= 1
        break
    elif a[right] > k:
        ans += 1
        left, right = right, left
    else:
        break

print(ans)
