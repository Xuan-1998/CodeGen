import sys

dp = [0] * (2**30)

q = int(sys.stdin.readline())

for _ in range(q):
    u, v = map(int, sys.stdin.readline().split())
    
    # Mark all vertices reachable from u_i
    for x in range(2**30):
        if (x & u) == u:
            dp[x] = 1
    
    # Check if there's a directed edge from any marked vertex to v_i
    found = False
    for x in range(2**30):
        if dp[x] and (x & v) == v:
            print("YES")
            found = True
            break
    
    if not found:
        print("NO")
