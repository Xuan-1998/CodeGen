n, k = map(int, input().split())
a = list(map(int, input().split()))
left, right = 0, n - 1
ans = 0

while left <= right:
    if a[left] > k and a[right] > k:
        break
    if a[left] <= k:
        ans += 1
        left += 1
    elif a[right] <= k:
        ans += 1
        right -= 1
    else:
        if a[left] < a[right]:
            ans += 1
            left += 1
        else:
            ans += 1
            right -= 1

print(ans)
