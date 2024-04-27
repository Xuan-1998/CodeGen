def generate_sequence():
    a = int(input("Enter the first integer: "))
    b = int(input("Enter the second integer (which is greater than or equal to the first): "))

    sequence = list(range(a, b + 1))
    
    return sequence

sequence = generate_sequence()
print(sequence)
