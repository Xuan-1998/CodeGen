from collections import defaultdict

dp = defaultdict(lambda: defaultdict(int))
for i in range(m):
    l, r = map(int, input().split())
    max_non_decreasing = 0
    max_increasing = 0
    for j in range(l-1, r):
        if a[j] <= a[j-1]:
            max_non_decreasing += 1
        elif a[j] >= a[j-1]:
            max_increasing = max(max_increasing, max_non_decreasing + 1)
        else:
            break
    print("Yes" if max_increasing > 0 else "No")
