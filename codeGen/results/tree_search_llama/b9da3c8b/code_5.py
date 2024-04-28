def untreated_crimes():
    n = int(input())
    events = list(map(int, input().split()))
    
    # Initialize a queue to store the recruitments and their corresponding time
    recruitment_queue = []
    
    # Initialize a variable to keep track of the available police officers at each crime occurrence
    available_officers = 0
    
    # Initialize a variable to count the number of untreated crimes
    untreated_crimes_count = 0
    
    for event in events:
        if event == -1:  # Crime occurrence
            # If there are no available police officers, increment the untreated crimes count
            if not recruitment_queue and available_officers == 0:
                untreated_crimes_count += 1
            else:
                # Decrement the available police officers based on the number of recruits in the queue
                available_officers -= len(recruitment_queue)
                recruitment_queue = []
        else:  # Recruitments
            # Add the recruitments to the queue with their corresponding time
            recruitment_queue.append(event)
    
    print(untreated_crimes_count)

if __name__ == "__main__":
    untreated_crimes()
