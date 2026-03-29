code
n, q = map(int, input().split())
signs = list(input())

queries = []
for _ in range(q):
    l, r = map(int, input().split())
    queries.append((l, r))

total_sum = sum(signs)
for query in queries:
    query_sum = sum(s if i >= query[0] and i <= query[1] else 0 for i, s in enumerate(signs))
    print(abs(query_sum - total_sum))
