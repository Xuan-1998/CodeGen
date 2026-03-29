def canReachLastIndex(arr):
    max_reachable = 0
    for i in range(len(arr)):
        if i > max_reachable:
            return False
        max_reachable = min(max_reachable + arr[i], len(arr) - 1)
    return True

# Read input from stdin
arr = list(map(int, input().split()))

# Print output to stdout
print(canReachLastIndex(arr))
