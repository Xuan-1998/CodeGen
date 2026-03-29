def can_reach_end(arr):
    max_reachable = 0
    for i, jump_length in enumerate(arr):
        if i > max_reachable:
            return False
        max_reachable = min(max_reachable + jump_length, len(arr) - 1)
    return True

if __name__ == "__main__":
    arr = [int(x) for x in input().split()]
    print(can_reach_end(arr))
