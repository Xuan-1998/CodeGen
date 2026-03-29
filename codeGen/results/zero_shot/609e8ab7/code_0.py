import sys

def min_operations(n, parents, ranges):
    # Create a dictionary to store the updated values of each vertex
    values = {i: 0 for i in range(1, n+1)}

    # Initialize the minimum number of operations needed
    min_ops = 0

    # Start from the leaf nodes and work our way up to the root
    for node in range(n, 0, -1):
        parent = parents[node]
        value_range = ranges[node-1]

        # Try to adjust the value of the node by adding elements from the array
        while values[node] < value_range[0]:
            min_ops += 1
            values[node] += 1

        if values[node] > value_range[1]:
            min_ops += 1
            values[node] -= 1

    return min_ops

def main():
    T = int(input())
    for _ in range(T):
        n = int(input())
        parents = list(map(int, input().split()))
        ranges = []
        for _ in range(n-1):
            l, r = map(int, input().split())
            ranges.append((l, r))

        min_ops = min_operations(n, parents, ranges)
        print(min_ops)

if __name__ == '__main__':
    main()
