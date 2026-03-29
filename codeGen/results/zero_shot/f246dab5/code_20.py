import sys

# Read the number of trips from stdin
n = int(sys.stdin.readline())

# Initialize the fares array with zeros
fares = [0] * n

for i in range(n):
    # Read the time of trip i from stdin
    t_i = int(sys.stdin.readline())
    
    # Calculate the fare for this trip...
    # ...based on the available tickets and the trip's time
    
    # Store the calculated fare in the fares array
    fares[i] = ...

# Print the fares to stdout
for f in fares:
    print(f)
