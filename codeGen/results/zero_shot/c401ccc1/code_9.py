import sys

def infinite_zoo(u, v):
    # Calculate the bitwise AND of u and v
    and_uv = u & v
    
    # If v has an odd LSB, there is no path from any vertex to v
    if (v & 1) == 1:
        return "NO"
    
    # If u and v have the same LSB, there must be a directed edge from u to v
    if (u & 1) == (and_uv & 1):
        return "YES"
    
    return "NO"

q = int(sys.stdin.readline())
for _ in range(q):
    u, v = map(int, sys.stdin.readline().split())
    print(infinite_zoo(u, v))
