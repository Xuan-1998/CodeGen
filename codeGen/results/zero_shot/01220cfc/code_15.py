def can_reach_last_index(arr):
    last_idx = len(arr) - 1
    curr_idx = 0
    while curr_idx <= last_idx:
        if curr_idx + arr[curr_idx] >= last_idx:
            return True
        curr_idx += 1
    return False

arr = [int(x) for x in input().split()]
print(can_reach_last_index(arr))
