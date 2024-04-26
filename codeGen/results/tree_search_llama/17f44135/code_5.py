n, k = map(int, input().split())
problems = list(map(int, input().split()))
left = 0
right = n - 1
count = 0

while left <= right:
    if problems[left] <= k and problems[right] <= k:
        count += 1
        left += 1
        right -= 1
    elif problems[left] <= k:
        left += 1
    else:
        right -= 1

print(count)
