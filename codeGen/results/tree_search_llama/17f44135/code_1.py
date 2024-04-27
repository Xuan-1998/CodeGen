n, k = map(int, input().split())
a = list(map(int, input().split()))

start, end = 0, n - 1
max_problems = 0

while start <= end:
    if a[start] <= k and (end == n - 1 or a[end] > k):
        max_problems += 1
        start += 1
    elif a[end] <= k and (start == 0 or a[start] > k):
        max_problems += 1
        end -= 1
    else:
        break

print(max_problems)
