n, k = map(int, input().split())
a = list(map(int, input().split()))
left = 0
right = n - 1
ans = 0

while left <= right:
    if a[left] <= k and (right == n - 1 or a[right] > k):
        ans += 1
        left += 1
    elif a[right] <= k and (left == 0 or a[left - 1] > k):
        ans += 1
        right -= 1
    else:
        if a[left] <= k:
            left += 1
        else:
            right -= 1

print(ans)
