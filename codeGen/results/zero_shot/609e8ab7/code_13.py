import sys

def min_operations():
    n = int(sys.stdin.readline())
    parents = [int(x) for x in sys.stdin.readline().split()]
    ranges = []
    for _ in range(n):
        l, r = map(int, sys.stdin.readline().split())
        ranges.append((l, r))

    # Sort the vertices by their current value
    sorted_ranges = sorted((r-l, i, (l+r)/2) for i, (l,r) in enumerate(ranges))

    min_ops = 0
    curr_val = 0
    ops_needed = [0] * n

    for _, i, mid in sorted_ranges:
        l, r = ranges[i]
        if curr_val < l:
            # Need to increase the value
            diff = l - curr_val
            min_ops += 1
            ops_needed[i] = 1
            curr_val = l
        elif curr_val > r:
            # Need to decrease the value
            diff = curr_val - r
            min_ops += 1
            ops_needed[i] = -1
            curr_val = r
        else:
            # Value is already within range, no operation needed
            curr_val = mid

    return min_ops + sum(abs(x) for x in ops_needed)

print(min_operations())
