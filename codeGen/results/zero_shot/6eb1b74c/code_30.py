import sys

def color_text(text, strings):
    # Initialize an empty list to store the steps
    steps = []
    
    # Iterate through the text
    for i in range(len(text)):
        colored = False
        
        # Check if any of the given strings match the current substring
        for j, string in enumerate(strings):
            if text[i:i+len(string)] == string:
                # If a match is found, mark it as colored and add it to the steps list
                colored = True
                steps.append((j+1, i))
        
        # If no matches were found, it's impossible to color the entire text
        if not colored:
            return -1
    
    # Return the minimum number of steps (length of steps list) and the steps themselves
    return len(steps), steps

# Read input from stdin
text = sys.stdin.readline().strip()
n = int(sys.stdin.readline())
strings = [sys.stdin.readline().strip() for _ in range(n)]

# Call the function to solve the problem
m, steps = color_text(text, strings)

# Print the result
if m == -1:
    print(m)
else:
    print(m)
    for step in steps:
        print(*step)
