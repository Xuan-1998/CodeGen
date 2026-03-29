def min_operations(n, p, l, r):
    values = [0] * (n + 1)  # Initialize values array with zeros
    ops = 0

    for i in range(2, n + 1):  # Iterate through vertices in topological order
        if values[i] < l[i]:  # If current value is below lower bound
            diff = l[i] - values[i]
            values[i] += diff  # Update vertex's value and add to ops
            ops += diff

    return ops

n = int(input())
p = list(map(int, input().split()))
l = [int(x) for x in input().split()]
r = [int(x) for x in input().split()]

print(min_operations(n, p, l, r))
