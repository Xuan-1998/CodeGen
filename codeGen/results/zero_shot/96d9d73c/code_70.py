import sys

def possible_partitioning(n, k, m, arr):
    # Group elements by their value (mod M)
    groups = {}
    for x in arr:
        group_idx = x % m
        if group_idx not in groups:
            groups[group_idx] = []
        groups[group_idx].append(x)

    # Check if each group has at least K elements and the absolute difference is within M
    for group in groups.values():
        if len(group) < k:
            return False
        group.sort()
        prev_val = group[0]
        for val in group[1:]:
            if abs(val - prev_val) > m:
                return False
            prev_val = val

    return True

n, k, m = map(int, input().split())
arr = list(map(int, input().split()))
print(possible_partitioning(n, k, m, arr))
