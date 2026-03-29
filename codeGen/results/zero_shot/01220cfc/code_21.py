def can_reach_last_index(jumps):
    max_reachable = 0
    for i in range(len(jumps) - 1, -1, -1):
        if i <= max_reachable:
            continue
        max_reachable = min(max_reachable, i + jumps[i])
        if max_reachable >= len(jumps) - 1:
            return True
    return False

jumps = list(map(int, input().split()))
print(can_reach_last_index(jumps))
