python
import sys

t = int(sys.stdin.readline().strip())

for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())
    res = str(n)
    
    for _ in range(m):
        new_n = ''
        for d in res:
            new_n += str((int(d) + 1) % 10)
        res = new_n
    
    print(len(str(int(res))) % (10**9+7))
