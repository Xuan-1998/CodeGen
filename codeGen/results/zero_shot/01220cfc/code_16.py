def can_reach_last_index(arr):
    n = len(arr)
    max_reachable = 0
    for i in range(n):
        if i <= max_reachable:
            max_reachable = min(max_reachable + arr[i], n - 1)
        else:
            return False
    return True

arr = list(map(int, input().split()))
print(can_reach_last_index(arr))
