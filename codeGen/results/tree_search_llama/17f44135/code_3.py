n, k = map(int, input().split())
a = list(map(int, input().split()))
left, right = 0, n - 1
solved = 0

while left <= right and a[left] <= k and a[right] <= k:
    if a[left] <= a[right]:
        solved += 1
        left += 1
    else:
        solved += 1
        right -= 1

print(solved)
