def can_reach_last_index(jumps):
    last_index = 0
    for i in range(len(jumps)):
        if i > last_index:
            return False
        last_index = max(last_index, i + jumps[i])
    return True

jumps = [int(i) for i in input().split()]
print(can_reach_last_index(jumps))
