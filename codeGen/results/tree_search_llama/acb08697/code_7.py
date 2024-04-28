n = int(input())  # Read the number of operations from stdin

stones = 0  # Initialize the number of stones to zero

for op in input():  # Iterate over each operation
    if op == "+":  # If we add a stone
        stones += 1
    else:  # If we remove a stone
        stones -= 1

print(stones)  # Print the minimum possible number of stones in the pile
