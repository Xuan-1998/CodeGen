def generate_sequence(start_value, end_value):
    sequence = []
    current_value = start_value
    
    while current_value <= end_value:
        sequence.append(current_value)
        current_value += 1
    
    return sequence

start_value = int(input())
end_value = int(input())

sequence = generate_sequence(start_value, end_value)

print(*sequence, sep=", ")
