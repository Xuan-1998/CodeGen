# Read input from stdin
A = int(input())
B = int(input())

# Calculate the minimum possible value of X
X = B

# Check if A - X is a power of 2 (i.e., the sum in binary)
while ((A - X) & ((A - X) - 1)) != 0:
    X += 1

# If we found an X, calculate Y as the XOR of A and X
if X <= A:
    Y = A ^ X
else:
    print(-1)  # No solution found

# Print the solution
print(X, Y)
