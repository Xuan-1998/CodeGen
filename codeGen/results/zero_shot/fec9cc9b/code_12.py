import sys

n, m = map(int, input().split())
arr = list(map(int, input().split()))
queries = []

for _ in range(m):
    l, r = map(int, input().split())
    queries.append((l, r))

for l, r in queries:
    is_ladder = True
    left = l - 1
    right = r

    while left < right and arr[left] <= arr[left + 1]:
        left += 1

    if left >= right or (left < right and arr[right - 1] <= arr[right]):
        print("Yes")
    else:
        print("No")
