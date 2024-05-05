code
def can_reach_last_index(jumps):
    curr_pos = 0
    for i in range(len(jumps)):
        if i > curr_pos:
            return False
        curr_pos = max(curr_pos, i + jumps[i])
    return True

jumps = [int(x) for x in input().split()]
print(can_reach_last_index(jumps))
