# Read input
n = int(input())
sequence = list(map(int, input().split()))

# Initialize variables
x = 1
y = 0
terminated = False

# Simulate the program
for _ in range(n):
    if x > n:
        terminated = True
        break
    a_x = sequence[x - 1]
    x += a_x
    y += a_x
    x -= a_x
    y += a_x

# Calculate and output final values
for i in range(n - 1):
    if terminated:
        print(-1)
    else:
        print(y)
