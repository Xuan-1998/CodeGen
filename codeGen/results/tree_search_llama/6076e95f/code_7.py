def generate_sequence(start, end):
    sequence = []
    current = start

    while current <= end:
        sequence.append(current)
        current += 1

    return sequence

# Receive inputs from stdin
start, end = map(int, input().split())

# Print the generated sequence to stdout
print(generate_sequence(start, end))
