import sys

# Read input from stdin
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
pivot = int(sys.stdin.readline())

left = []
right = []

for num in arr:
    if num < pivot:
        left.append(num)
    elif num > pivot:
        right.append(num)

# Print the result to stdout
print(' '.join(map(str, left + [str(pivot)] + right)))
