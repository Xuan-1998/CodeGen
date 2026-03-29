import sys

def min_operations(parents, ranges):
    n = len(ranges)
    max_ops = [0] * (n + 1)

    def dfs(i, val):
        if i > 0:
            ops = 0
            for j in range(val, ranges[i][1]):
                ops += 1
                if i != 0 and parents[i] != -1:
                    ops += dfs(parents[i], j)
            return ops
        else:
            return 0

    for i in range(1, n + 1):
        max_ops[i] = dfs(i, ranges[i][0])
        for j in range(ranges[i][0], ranges[i][1]):
            max_ops[i] += 1

    return sum(max_ops[1:])

def main():
    T = int(sys.stdin.readline())
    for _ in range(T):
        n = int(sys.stdin.readline())
        parents = [int(x) - 1 for x in sys.stdin.readline().split()]
        ranges = {}
        for i in range(n):
            l, r = map(int, sys.stdin.readline().split())
            ranges[i + 1] = (l, r)

        print(min_operations(parents, ranges))

if __name__ == "__main__":
    main()
