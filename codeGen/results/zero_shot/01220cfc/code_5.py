from sys import stdin

def can_reach_last_index(jumps):
    max_reachable = 0
    for i in range(len(jumps)):
        if i > max_reachable:
            return False
        max_reachable = max(max_reachable, i + jumps[i])
    return True

jumps = [int(x) for x in stdin.readline().split()]
print(can_reach_last_index(jumps))
