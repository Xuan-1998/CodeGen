n, m = map(int, input().split())
arr = list(map(int, input().split()))
queries = []
for _ in range(m):
    l, r = map(int, input().split())
    queries.append((l, r))

for l, r in queries:
    is_ladder = True
    for i in range(l-1, r):
        if arr[i] > arr[i+1]:
            is_ladder = False
            break
    print("Yes" if is_ladder else "No")
