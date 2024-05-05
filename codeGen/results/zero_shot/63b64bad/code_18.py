# Step 1: Read input
n = int(input())
sequence = list(map(int, input().split()))

# Step 2: Define a function to simulate the program
def simulate_program(sequence):
    x, y = 1, 0
    while True:
        if x <= 0 or x > n:
            return -1
        x += sequence[x]
        y += sequence[x]
        x -= sequence[x]

# Step 3: Run the simulation for each sequence and print the result
for i in range(2, n+1):
    result = simulate_program(sequence[:i])
    if result != -1:
        print(result)
    else:
        print(-1)
