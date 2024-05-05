import sys

def min_operations(n, p, l, r):
    # Create a dictionary to store the range for each vertex
    ranges = {i: (l[i-1], r[i-1]) for i in range(1, n+1)}

    # Initialize the minimum number of operations
    min_ops = 0

    # Iterate over each vertex
    for i in range(1, n+1):
        # Find the range of values for this vertex
        v_range = ranges[i]

        # Check if the value is within its range
        if v_range[0] <= i <= v_range[1]:
            continue

        # Calculate the minimum number of operations needed to adjust the value
        ops = abs(i - v_range[0]) + abs(i - v_range[1])
        min_ops += ops

    return min_ops

T = int(sys.stdin.readline())

for _ in range(T):
    n = int(sys.stdin.readline())
    p = [int(x) for x in sys.stdin.readline().split()]
    l = [int(x) for x in (sys.stdin.readline() for _ in range(n)).next().split()]
    r = [int(x) for x in (sys.stdin.readline() for _ in range(n)).next().split()]

    print(min_operations(n, p, l, r))
