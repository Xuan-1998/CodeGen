import sys

def min_operations(n, x):
    operations = 0
    while len(str(x)) < n:
        # Find the longest prefix of str(x) in '09...99'
        for i in range(1, 10 ** (n - len(str(x))) + 1):
            if str(i).startswith(str(x)[:len(str(x))])):
                x *= i
                operations += 1
                break
    return -1 if len(str(x)) != n else operations

# Read input from standard input
n, x = map(int, input().split())

# Print the minimum number of operations to standard output
print(min_operations(n, x))
