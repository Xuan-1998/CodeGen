def can_reach_end(arr):
    max_reachable = 0
    for i in range(len(arr)):
        if i > max_reachable:
            return False
        max_reachable = max(max_reachable, i + arr[i])
    return True

# Read input array from stdin
arr = [int(x) for x in input().split()]

# Call the function and print the result to stdout
print(can_reach_end(arr))
