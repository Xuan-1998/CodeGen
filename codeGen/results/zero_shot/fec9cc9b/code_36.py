n, m = map(int, input().split())
arr = list(map(int, input().split()))
queries = []
for _ in range(m):
    l, r = map(int, input().split())
    queries.append((l, r))

for query in queries:
    l, r = query
    non_decreasing = True
    non_increasing = True
    for i in range(l-1, r):
        if arr[i] > arr[i+1]:
            non_decreasing = False
        elif arr[i] < arr[i+1]:
            non_increasing = False
            break
    print("Yes" if (non_decreasing and not non_increasing) or (not non_decreasing and non_increasing) else "No")
