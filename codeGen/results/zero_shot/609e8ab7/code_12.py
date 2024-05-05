def min_operations(n, parent, lower_bounds, upper_bounds):
    # Initialize the result array with zeros
    result = [0] * (n + 1)

    for i in range(2, n + 1):
        p = parent[i - 1]
        result[i] = max(result[p], upper_bounds[i - 1] - lower_bounds[i - 1])

    return sum(result[2:])

# Read input from standard input
T = int(input())
for _ in range(T):
    n = int(input())
    parent = list(map(int, input().split()))
    lower_bounds = [int(x) for x in input().split()]
    upper_bounds = [int(x) for x in input().split()]

    # Calculate the minimum number of operations
    min_ops = min_operations(n, parent, lower_bounds, upper_bounds)

    print(min_ops)
