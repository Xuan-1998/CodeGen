import sys
input = sys.stdin.readline

n, m = map(int, input().split())
plants = [tuple(map(int, input().split())) for _ in range(n)]

plants.sort(key=lambda x: x[1])

replanted = 0
for i in range(1, m):
    replanted += plants[i-1][1] - plants[i-2][1]

print(replanted)
