from collections import defaultdict

n = int(input())
graph = defaultdict(list)

for _ in range(n-1):
    si, ti = map(int, input().split())
    graph[si].append(ti)

# Your code here
