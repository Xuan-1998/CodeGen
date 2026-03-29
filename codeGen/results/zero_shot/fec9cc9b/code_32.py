import random

n = 10
m = 3
arr = [random.randint(1, 10) for _ in range(n)]

for i in range(m):
    l, r = random.randint(0, n-1), random.randint(i, n-1)
    print("Yes" if is_ladder(arr, l, r) else "No")
