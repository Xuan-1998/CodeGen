n, m = map(int, input().split())
arr = []
curr_max = None

# Read array elements
for _ in range(n):
    arr.append(int(input()))

# Read queries
queries = []
for _ in range(m):
    l, r = map(int, input().split())
    queries.append((l, r))

for l, r in queries:
    min_val = min(arr[l:r+1])
    is_ladder = True
    for i in range(l, r):
        if arr[i] < min_val or (arr[i] == min_val and not all(x >= min_val for x in arr[i+1:r])):
            is_ladder = False
            break

    print("Yes" if is_ladder else "No")
