# Step 1: Read input A and B from standard input
A = int(input())
B = int(input())

# Step 2: Initialize X and Y with maximum possible value (since they are non-negative)
X = 0
Y = 0

# Step 3: Calculate the maximum possible value of X based on A and B
while True:
    if A == X + Y and B == X ^ Y:
        break
    X += 1
    Y = A - X

code:
