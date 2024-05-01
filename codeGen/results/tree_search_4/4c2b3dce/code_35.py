import sys

def solve(s):
    state = not_end_of_AB = True  # Initialize state to not at end of AB
    for c in s:
        if c == 'A':
            not_end_of_AB = True  # Update state if we're not at the end of AB
        elif c == 'B' and not_end_of_AB:  # Check if we've reached the end of AB
            state = end_of_AB = False
        elif c == 'A' and not end_of_AB:  # Check if we've reached the start of BA
            state = not_end_of_BA = True
        elif c == 'B' and not end_of_AB:  # Update state when at the end of BA
            state = end_of_BA = False

    return "YES" if state else "NO"

# Receive input from stdin
s = sys.stdin.readline().strip()

print(solve(s))
