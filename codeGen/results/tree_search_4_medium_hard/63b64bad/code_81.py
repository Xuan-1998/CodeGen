def sequenceSimulation(n, sequence):
    # Initialize the state as 0
    current_state = 0
    
    while True:
        # Get the next sequence element
        a_x = sequence[x - 2]
        
        # Check if we've reached the end of the sequence or x <= 0
        if x > n or x <= 0:
            break
        
        # Update the state using the transition rules
        current_state += a_x
        current_state -= a_x
        
    return current_state

# Read the input
n = int(input())
sequence = list(map(int, input().split()))

# Calculate the final value of y for each run of the program on the sequence
for i in range(1, n + 1):
    print(sequenceSimulation(n, sequence))
