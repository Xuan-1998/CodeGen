import sys

q = int(sys.stdin.readline())

for _ in range(q):
    u, v = map(int, sys.stdin.readline().split())
    
    # If the bits that are 1 in both u and v are greater than the difference between u and v, 
    # then there's a path from u to v.
    if (u & v) > abs(u - v):
        print("YES")
    else:
        print("NO")
