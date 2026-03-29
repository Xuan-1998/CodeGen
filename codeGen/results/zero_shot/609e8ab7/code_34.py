import sys

def calculate_min_operations(tree, ranges):
    min_ops = 0
    for i in range(1, len(ranges)):
        max_val = ranges[i][1]
        min_val = ranges[i][0]
        diff = max_val - min_val
        if diff > 0:
            min_ops += (diff // (max_val - min_val + 1))
    return min_ops

def main():
    T = int(sys.stdin.readline())
    for _ in range(T):
        n = int(sys.stdin.readline())
        parents = list(map(int, sys.stdin.readline().split()))
        ranges = []
        for i in range(n):
            l, r = map(int, sys.stdin.readline().split())
            ranges.append((l, r))
        tree = {i: parent for i, parent in enumerate(parents, 1)}
        min_ops = calculate_min_operations(tree, ranges)
        print(min_ops)

if __name__ == '__main__':
    main()
