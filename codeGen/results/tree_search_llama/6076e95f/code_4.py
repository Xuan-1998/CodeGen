def generate_sequence(num1, num2):
    sequence = []
    for i in range(num1, num2 + 1):
        sequence.append(i)
    return sequence

num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))

sequence = generate_sequence(num1, num2)

print(sequence)
