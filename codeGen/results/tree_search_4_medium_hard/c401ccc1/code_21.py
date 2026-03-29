import sys

n = int(input())
graph = [0] * (1 << 30)

for _ in range(int(input())):
    u, v = map(int, input().split())
    
    while u:
        graph[u | v] = 1
        v &= ~u
        u &= ~v
    
    if graph[v]:
        print("YES")
    else:
        print("NO")
