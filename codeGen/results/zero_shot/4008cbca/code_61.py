# Step 1: Read the input strings
board = input()
hand = input()

# Step 2: Initialize an empty stack for the board
stack = []

# Step 3: Iterate over the board string and push balls onto the stack
for ball in board:
    if ball != 'W':  # Ignore white balls
        stack.append(ball)

# Step 4: Pop balls from the top of the stack until it's empty or a ball is found that can't be removed
while len(stack) > 1:
    for i in range(len(stack) - 2):
        if stack[i] == stack[i+1] == stack[i+2]:
            del stack[:i+3]
            break

# Step 5: Calculate the number of balls needed to remove all balls from the board
needed = len(board) - len(stack)

# Step 6: Check if it's possible to remove all balls
if needed > 0:
    for ball in hand:
        if ball == 'W':
            needed -= 1

# Step 7: Print the result
print(needed)
