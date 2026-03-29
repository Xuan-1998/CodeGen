import sys

def min_operations(n, p, l, r):
    if n == 1:  # base case: only one vertex
        return 0
    
    # recursively find operations for left and right subtrees
    left_ops = min_operations(p[1], p[2:p.index(p[n-1]+1)], [l[i] - l[1] for i in range(1, n-1)], [r[i] - r[1] for i in range(1, n-1)])
    right_ops = min_operations(n-p[1]-1, p[p.index(p[n-1]+1)+1:], [l[n-1]], [r[n-1]])
    
    # adjust values at current vertex to fit its range
    cur_ops = 0
    for i in range(1, n):
        if l[i] > r[1]:  # need to increase values
            cur_ops += (l[i] - r[1]) // 2
        elif l[i] < r[n-1]:  # need to decrease values
            cur_ops += (r[n-1] - l[i]) // 2
    
    return left_ops + right_ops + cur_ops

# read input from stdin
n = int(sys.stdin.readline())
p = list(map(int, sys.stdin.readline().split()))
l = [int(x) for x in sys.stdin.read().split()]
r = [int(x) for x in sys.stdin.read().split()]

# calculate and print the minimum number of operations
print(min_operations(n, p, l, r))
