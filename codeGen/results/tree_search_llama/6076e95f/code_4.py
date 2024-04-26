import math

def generate_sequence():
    start, end = map(int, input().split())
    
    # Initialize the sequence
    sequence = []
    
    # Generate the sequence for each range of powers of 2
    power = 0
    while start <= end:
        step = 2 ** power
        sequence.extend(range(start, min(end + 1, start + step)))
        start += step
        power += 1
        
    return sequence

print(*generate_sequence(), sep=' ')
