# Step 1: Read the input
n = int(input())
a = list(map(int, input().split()))

# Step 2: Initialize the results dictionary and simulate for each sequence
results = {}
for i in range(2, n+1):
    x, y = 1, 0
    while True:
        if x <= 0 or x > i:
            break
        x += a[x]
        y += a[x]
        x -= a[x]
    
    # Check if the program terminated
    if x <= 0 or x > i:
        results[i] = y
    else:
        results[i] = -1

# Step 3: Print the results
for key in range(2, n+1):
    print(results.get(key, -1))
