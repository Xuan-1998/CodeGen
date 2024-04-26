import sys

# Read input
n = int(sys.stdin.readline())
A = [int(x) for x in sys.stdin.readline().split()]
m = int(sys.stdin.readline())
B = [int(x) for x in sys.stdin.readline().split()]

# Combine arrays and sort
arr = A + B
arr.sort()

# Initialize variables
a, b = None, None

# Iterate through the combined array
for i in range(len(arr)):
    if a is None:
        # Check if current element belongs to set A
        if arr[i] in A:
            a = arr[i]
        else:
            # If not, start checking elements from B
            b = arr[i - len(A) + 1]
    elif b is not None:
        # Add the current element (from B) to the noted-down value (a)
        c = a + b
        if c not in A and c not in B:
            print(f"{a} {b}")
            sys.exit(0)

print("No solution found")
