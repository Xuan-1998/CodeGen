# Read the input
n = int(input())
marks = list(map(int, input().split()))

# Initialize the minimum sum of marks below water level
min_sum = float('inf')

for i in range(n):
    # Calculate the marks strictly above water on day i
    above_water = sum(1 for j in range(i+1) if j < marks[i])
    
    # Calculate the marks strictly below water on day i
    below_water = marks[i] - above_water
    
    # Update the minimum sum of marks below water level
    min_sum = min(min_sum, below_water)

# Print the answer
print(min_sum)
