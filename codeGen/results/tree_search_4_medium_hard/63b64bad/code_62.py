import sys

# Initialize memoization cache with None values
memo = {}

def next_state(x, y):
    if (x, y) in memo:
        return memo[(x, y)]
    
    # Calculate the new state based on the transition rules
    x += a[x]
    y += a[x]
    y += a[x]  # Update y by subtracting a[x]
    x -= a[x]

    if x <= 0 or x > n:
        return -1, None  # Terminal state

    memo[(x, y)] = (x, y)  # Cache the result
    return x, y

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
for i in range(n-1):
    x, y = 1, 0
    while True:
        x, y = next_state(x, y)
        if x <= 0 or x > n:
            break
    print(y)
