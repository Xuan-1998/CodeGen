q = int(input())
queries = []
for _ in range(q):
    u, v = map(int, input().split())
    queries.append((u, v))

for u, v in queries:
    if (u & v) == v:
        print("YES")
    else:
        print("NO")
