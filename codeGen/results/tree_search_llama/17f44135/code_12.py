n, k = map(int, input().split())
a = list(map(int, input().split()))

left = 0
right = n-1

count = 0
while left <= right:
    if a[left] <= k and a[right] <= k:
        count += 1
        left += 1
        right -= 1
    elif a[left] <= k:
        count += 1
        left += 1
    else:
        right -= 1

print(count)
