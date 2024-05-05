# Receive input
n = int(input())
a_values = list(map(int, input().split()))
b_values = list(map(int, input().split()))
c_values = list(map(int, input().split()))

# Calculate maximum total joy
max_total_joy = 0

# Initialize variables to keep track of the hares that have been fed
hunger_left = [True] * n
hunger_right = [True] * n

# Iterate over all possible orderings of feeding the hares
for i in range(n):
    max_single_joy = 0
    for j in range(n):
        # Check if hare j is hungry and its adjacent hares have not been fed yet
        if hunger_left[j] and (j == 0 or hunger_right[j-1]):
            single_joy = a_values[j]
        elif hunger_left[j] and (j > 0 and not hunger_right[j-1]):
            single_joy = b_values[j]
        elif hunger_left[j]:
            single_joy = c_values[j]
        
        # Update maximum single joy
        max_single_joy = max(max_single_joy, single_joy)
        
    # Calculate the total joy for the current ordering
    total_joy = 0
    for j in range(n):
        if hunger_left[j]:
            total_joy += a_values[j] if (j == 0 or not hunger_right[j-1]) else b_values[j] if j > 0 and hunger_right[j-1] else c_values[j]
    
    # Update maximum total joy
    max_total_joy = max(max_total_joy, total_joy)

    # Update the variables to keep track of the hares that have been fed
    for j in range(n):
        if hunger_left[j]:
            hunger_left[j] = False
            hunger_right[j] = True
        else:
            hunger_left[j] = True
            hunger_right[n-j-1] = False

print(max_total_joy)
