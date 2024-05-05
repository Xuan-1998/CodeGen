import math

def solve(n, m):
    V = set()
    for p in itertools.permutations(m):
        if sorted(p) == list(m):
            V.add(tuple(p))
    return len(V) % (10**9 + 7)

n = int(input())
m = [int(x) for x in input().split()]
print(solve(n, m))
