import sys

n, m = map(int, sys.stdin.readline().split())
table = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

for _ in range(m):
    table = sorted(zip(*table))
    table = [' '.join(map(str, row)) for row in zip(*table)]
    print("Yes" if all(map(lambda x: x.split()[i].isdigit() and int(x.split()[i]) <= int(x.split()[i+1]), table)) else "No")
