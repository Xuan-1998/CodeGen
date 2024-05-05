def infinite_zoo(u, v):
    return str((u & v) == v)

q = int(input())
for _ in range(q):
    u, v = map(int, input().split())
    print(infinite_zoo(u, v))
