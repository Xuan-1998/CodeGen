import sys
from collections import defaultdict

def bitAND(u, v):
    return u & v

def has_path memo):
    if (u, k) in memo:
        return memo[(u, k)]
    
    if k == 0:
        return False
    
    reachable = set()
    for w in range(2**30):
        if bitAND(u, w) == w and not has_path(memo, w, k-1):
            break
        if bitAND(u, w) != w or (w & v) == v:
            continue
        reachable.add(w)
    
    memo[(u, k)] = len(reachable) > 0
    return memo[(u, k)]

def solve():
    q = int(input())
    memo = defaultdict(bool)
    
    for _ in range(q):
        u, v = map(int, input().split())
        print('YES' if has_path(memo, u, 30) and (u & v) == v else 'NO')

if __name__ == '__main__':
    solve()
