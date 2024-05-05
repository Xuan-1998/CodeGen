def can_reach_last_index(jumps):
    max_reachable = 0
    for i, jump in enumerate(jumps):
        if i > max_reachable:
            return False
        max_reachable = min(max_reachable + jump, len(jumps) - 1)
    return True

if __name__ == "__main__":
    jumps = [int(x) for x in input().split()]
    print(can_reach_last_index(jumps))
