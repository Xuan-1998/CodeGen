n = int(input())  # Read the number of events from input

officers = []  # Initialize an empty stack to keep track of available officers

untreated_crimes = 0  # Initialize a counter for untreated crimes

for _ in range(n):
    event = int(input())
    
    if event == -1:  # If it's a crime, pop officers from the stack until we find one who hasn't been assigned
        while officers and len(officers) > event:
            officers.pop()
        
        if not officers:  # If there are no available officers, increment the counter for untreated crimes
            untreated_crimes += 1
    else:  # If it's an officer recruitment, push them onto the stack
        officers.extend([event] * event)

print(untreated_crimes)  # Print the number of untreated crimes
