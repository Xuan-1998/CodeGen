from collections import defaultdict
import sys

def check_path():
    q = int(input())
    graph = defaultdict(dict)
    
    for _ in range(q):
        u, v = map(int, input().split())
        
        if (u & v) == v:
            print("YES")
        else:
            print("NO")

check_path()
