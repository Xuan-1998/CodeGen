n, m = map(int, input().split())
edges = []
for _ in range(m):
    u, v = map(int, input().split())
    edges.append((u, v))

k = int(input())
path = list(map(int, input().split()))

# Your solution will go here
