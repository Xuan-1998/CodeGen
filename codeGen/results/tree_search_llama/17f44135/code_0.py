n, k = map(int, input().split())
a = list(map(int, input().split()))

left, right = 0, n-1
count = 0

while left <= right:
    if a[left] <= k and (right == n-1 or a[right] > k):
        count += 1
        left += 1
    elif a[right] <= k and (left == 0 or a[left-1] > k):
        count += 1
        right -= 1
    else:
        break

print(count)
