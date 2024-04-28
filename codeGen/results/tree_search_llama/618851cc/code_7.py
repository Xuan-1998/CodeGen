import sys

# Read input
n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))

# Combine arrays and remove duplicates
elements = sorted(set(A + B))

# Define custom comparison function
class CustomComparison:
    def __init__(self):
        self.in_A = set(A)
        self.in_B = set(B)

    def __call__(a, b):
        if a in self.in_A:
            return -1 if b in self.in_B else -1
        elif b in self.in_B:
            return 1 if a in self.in_A else 1
        else:
            return 0 if a == b else 1 if a < b else -1

# Sort elements using custom comparison function
custom_comparison = CustomComparison()
sorted_elements = sorted(elements, key=custom_comparison)

# Find the first pair (a, b) where a belongs to A and b belongs to B
for i in range(len(sorted_elements) - 1):
    if sorted_elements[i] in A and sorted_elements[i + 1] in B:
        print(f"{sorted_elements[i]} {sorted_elements[i + 1]}")
        break

# If no such pair is found, print "Not Found"
else:
    print("Not Found")

