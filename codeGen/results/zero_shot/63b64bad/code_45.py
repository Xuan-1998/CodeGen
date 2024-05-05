def simulate_program(a):
    x = 1
    y = 0
    while True:
        # Increase both x and y by a_x simultaneously
        x += a[x]
        y += a[x]
        
        # Increase y by a_x, decrease x by a_x
        y += a[x]
        x -= a[x]
        
        if x < 1 or x > len(a) - 2:
            return y

# Read input from stdin
n = int(input())
a = list(map(int, input().split()))

# Run the simulation for each sequence and print the result
for i in range(2, n):
    result = simulate_program(a[i-1:i])
    if result == -1:  # Program does not terminate
        print(-1)
    else:
        print(result)
