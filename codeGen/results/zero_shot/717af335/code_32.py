# Read A and B from stdin
A = int(input())
B = int(input())

# Calculate X (X will be the smallest possible value)
X = 0
while True:
    Y = A - X
    if ((X ^ Y) == B):
        print(f"{X} {Y}")
        break
    else:
        X += 1

