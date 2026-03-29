def can_reach_last_index(jumps):
    last_position = len(jumps) - 1
    for i in range(len(jumps)):
        if i + jumps[i] >= last_position:
            last_position = i
    return last_position == len(jumps) - 1

jumps = list(map(int, input().split()))
print(can_reach_last_index(jumps))
