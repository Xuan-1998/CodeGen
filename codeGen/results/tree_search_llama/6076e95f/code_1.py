def generate_sequence():
    start, end = map(int, input().split())
    
    # Initialize an empty list to store the sequence
    sequence = []
    
    for num in range(start, end + 1):
        sequence.append(num)
    
    return sequence

print(*generate_sequence(), sep=" ")

