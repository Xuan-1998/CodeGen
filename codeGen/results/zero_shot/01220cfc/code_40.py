import sys

def can_reach_last_index(jumps):
    n = len(jumps)
    max_reachable_index = 0
    for i in range(n):
        if i > max_reachable_index:
            return False
        max_reachable_index = max(max_reachable_index, min(i + jumps[i], n - 1))
    return True

if __name__ == "__main__":
    jumps = [int(x) for x in sys.stdin.readline().split()]
    print(can_reach_last_index(jumps))
