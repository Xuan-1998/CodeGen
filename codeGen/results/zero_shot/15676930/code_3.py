import sys

# Read the input
n = int(sys.stdin.readline().strip())
a_values = [int(x) for x in sys.stdin.readline().split()]
b_values = [int(x) for x in sys.stdin.readline().split()]

# Initialize variables
total_joy = 0
hunger_state = ['full'] * n

# Calculate the total joy
for i in range(n):
    if hunger_state[i-1] == 'full' and hunger_state[(i+1)%n] == 'full':
        total_joy += c_values[i]
    elif hunger_state[i-1] == 'full' and hunger_state[(i+1)%n] == 'hungry':
        total_joy += b_values[i]
    else:
        total_joy += a_values[i]

# Print the answer
sys.stdout.write(str(total_joy) + '\n')
