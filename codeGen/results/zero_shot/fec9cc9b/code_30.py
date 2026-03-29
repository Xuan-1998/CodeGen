def is_ladder(arr, l, r):
    for i in range(l, r):
        if arr[i] < arr[i-1]:
            return False
    for i in range(l, r):
        if arr[i] > arr[i-1]:
            return False
    return True

n, m = map(int, input().split())
arr = list(map(int, input().split()))
queries = []
for _ in range(m):
    l, r = map(int, input().split())
    queries.append((l, r))

for query in queries:
    l, r = query
    print("Yes" if is_ladder(arr, l-1, r) else "No")
