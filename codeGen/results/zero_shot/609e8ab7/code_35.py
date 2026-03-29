import sys

def calculate_target_values(n, p, l, r):
    # Initialize the target values array
    target_values = [0] * (n + 1)

    # Calculate the target values for each vertex
    for i in range(2, n + 1):
        target_values[i] = max(l[p[i]], target_values[p[i]] + l[i])

    return target_values

def calculate_operations(n, p, l, r, target_values):
    operations = 0

    # Traverse the tree in postorder
    for i in range(2, n + 1):
        parent_target_value = target_values[p[i]]
        if l[i] > parent_target_value:
            operations += (l[i] - parent_target_value)
        if r[i] < parent_target_value:
            operations += (parent_target_value - r[i])

    return operations

n = int(input())
p = list(map(int, input().split()))
l = [int(x) for x in input().split()]
r = [int(x) for x in input().split()]

target_values = calculate_target_values(n, p, l, r)
operations = calculate_operations(n, p, l, r, target_values)

print(operations)
