import heapq

# Read the length of the sequence 'n'
n = int(input().strip())

# Read the sequence
seq = list(map(int, input().strip().split()))

# Create a priority queue
pq = []

# Initialize 'sum' and 'max'
sum = 0
max = -1

# Iterate over the sequence
for i in range(n):
    # Add the 'i'th element to the priority queue
    heapq.heappush(pq, seq[i])

    # If the 'i'th element is less than 'max'
    if seq[i] < max:
        # Subtract the difference from 'sum'
        sum -= max - seq[i]
        # Update 'max' to the 'i'th element
        max = seq[i]

    # If the 'i'th element is greater than 'max'
    if seq[i] > max:
        # Update 'max' to the 'i'th element
        max = seq[i]

# Print 'sum'
print(sum)

