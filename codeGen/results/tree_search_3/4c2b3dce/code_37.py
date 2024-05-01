from collections import defaultdict

# Read input from stdin
s = input()

# Initialize state dictionaries
A_state = defaultdict(dict)
B_state = defaultdict(dict)

# Populate A_state dictionary with 'A' as the last occurrence of 'A'
for i, c in enumerate(s):
    if c == 'A':
        A_state[c]['state'] = 'A'
        A_state[c]['pos'] = i

# Initialize current state
current_state = A_state['A']['state']

# Iterate over the string
for i, c in enumerate(s):
    # Update current state based on the character seen
    if c == 'A':
        current_state = 'A'
    elif c == 'B':
        current_state = 'B'

    # Check if we have both 'A' and 'B' in the current state
    if (current_state == 'AB'):
        print("YES")
        break

# If we don't find a valid 'AB' or 'BA', output "NO"
else:
    print("NO")
