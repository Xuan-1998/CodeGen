def min_steps_to_color_red(input):
    # Read input from stdin
    text = input.readline().strip()
    n = int(input.readline())
    
    patterns = [input.readline().strip() for _ in range(n)]
    occurrences = {}
    
    # Iterate over each pattern
    for pattern in patterns:
        start_index = 0
        while True:
            start_index = text.find(pattern, start_index)
            if start_index == -1:
                break
            occurrences[start_index] = pattern
            start_index += len(pattern)
    
    steps = 0
    last_end = 0
    for end in sorted(occurrences.keys()):
        if end > last_end:
            steps += 1
            last_end = end
    
    print(steps)
    
    # Print the steps to color all letters in red
    for i, (start, pattern) in enumerate(sorted(occurrences.items())):
        print(f"{i+1} {start} {pattern}")

# Read input from stdin and call the function
input = open("input.txt", "r")
min_steps_to_color_red(input)
