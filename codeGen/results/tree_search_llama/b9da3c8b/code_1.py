def untreated_crimes():
    n = int(input())  # Read the number of events from input
    officers_available = 0  # Initialize the count of available police officers
    
    for _ in range(n):  # Iterate over each event
        event_type = int(input())  # Read the type of the event (crime or recruitment)
        
        if event_type == -1:  # If it's a crime, increment the count of crimes that will go untreated
            crimes_uninvestigated += 1  # Increment the count
        else:
            officers_available += event_type  # Update the count of available police officers
            
    print(crimes_uninvestigated)  # Print the final count of crimes that will go untreated

if __name__ == "__main__":
    untreated_crimes()
