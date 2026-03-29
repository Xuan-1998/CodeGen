import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    b = list(map(int, sys.stdin.readline().split()))
    
    # Check if the cumulative sum of b is possible to reconstruct as a
    cumulative_sum = [0]
    for i in range(n):
        cumulative_sum.append(cumulative_sum[-1] + b[i])
        
    if any(x % y != 0 and x < y for x, y in zip(cumulative_sum[1:], cumulative_sum)):
        print("NO")
    else:
        print("YES")
