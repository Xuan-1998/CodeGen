import sys

def can_reach_last_index(jumps):
    last_index = len(jumps) - 1
    for i in range(1, len(jumps)):
        if jumps[i] >= i:
            last_index = min(last_index, i)
    return last_index == 0

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    jumps = list(map(int, sys.stdin.readline().split()))
    print(can_reach_last_index(jumps))
