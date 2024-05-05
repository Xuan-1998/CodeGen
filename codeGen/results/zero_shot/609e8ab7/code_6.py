def min_ops(p, r):
    ans = 0
    for i in range(2, n+1):
        # Calculate the difference between the range end and the current vertex value
        diff = r[i-1][1] - r[i-1][0]
        
        # If the vertex is not a leaf node (i.e., it has children)
        if p[i] != 0:
            # Add the minimum of the parent's range and the current vertex's range to the difference
            diff += min(r[p[i]][1], r[i-1][1]) - r[i-1][0]
        
        # Add the difference to the total number of operations
        ans += diff
    
    return ans

T = int(input())
for _ in range(T):
    n = int(input())
    p = [0] + [int(x) for x in input().split()]
    r = [[int(x) for x in input().split()] for _ in range(n)]
    
    ans = min_ops(p, r)
    print(ans)
