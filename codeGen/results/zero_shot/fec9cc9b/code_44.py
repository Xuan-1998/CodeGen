n, m = map(int, input().split())
array = list(map(int, input().split()))
queries = []

for _ in range(m):
    l, r = map(int, input().split())
    queries.append((l, r))

for query in queries:
    start, end = query
    subsegment = array[start:end+1]
    if is_ladder(subsegment):
        print("Yes")
    else:
        print("No")
