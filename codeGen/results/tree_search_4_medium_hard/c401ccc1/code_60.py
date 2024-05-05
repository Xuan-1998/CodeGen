import sys
from bitarray import bitarray

n = int(sys.stdin.readline())
reach = [False] * (2 ** 30)

def update_reach(reach):
    new_reach = reach.copy()
    for i in range(len(new_reach)):
        if reach[i]:
            for j in range(2 ** 30):
                if ((i | j) & j) == j and not reach[j]:
                    new_reach[j] = True
    return new_reach

for _ in range(n):
    u, v = map(int, sys.stdin.readline().split())
    while True:
        reach = update_reach(reach)
        if reach[v]:
            print("YES")
            break
    else:
        print("NO")
