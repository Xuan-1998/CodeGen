# Define the function that simulates the program
def simulate_program(a):
    x, y = 1, 0
    while True:
        if x <= 0 or x > len(a) - 1:
            return y
        a[x] += 1
        x, y = x + a[x], y + a[x]

# Read input from stdin
n = int(input())
a = list(map(int, input().split()))

# Initialize the result array with -1's
result = [-1] * (n-1)

# Simulate the program for each sequence and store the results
for i in range(2, n+1):
    result[i-2] = simulate_program(a[:i])

# Print the results to stdout
for y in result:
    print(y)
