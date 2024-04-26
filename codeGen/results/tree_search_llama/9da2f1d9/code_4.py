import sys

# Read input from stdin
size = int(input())
arr = list(map(int, input().split()))
pivot = int(input())

# Sort array in descending order
arr.sort(reverse=True)

# Initialize partitions
left = []
middle = []
right = []

for num in arr:
    if num < pivot:
        left.append(num)
    elif num == pivot:
        middle.append(num)
    else:
        right.append(num)

print(" ".join(map(str, left + middle + right)))
