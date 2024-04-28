n = int(input())  # Read the number of events from stdin

officers_available = 0  # Initialize the number of available officers
crimes_uninvestigated = 0  # Initialize the count of crimes that won't be investigated

for event in input().split():  # Split the second line into individual integers
    if int(event) == -1:  # If the integer represents a crime (-1)
        if officers_available < 1:  # Check if there are no available officers
            crimes_uninvestigated += 1  # Increment the count of uninvestigated crimes
        else:
            officers_available -= 1  # Decrement the number of available officers

    else:
        officers_available += int(event)  # Update the number of available officers based on the recruitment

print(crimes_uninvestigated)  # Print the final count of uninvestigated crimes to stdout
