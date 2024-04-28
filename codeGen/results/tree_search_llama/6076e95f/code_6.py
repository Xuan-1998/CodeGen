def generate_sequence():
    first_integer = int(input("Enter the first integer: "))
    second_integer = int(input("Enter the second integer: "))

    average = (first_integer + second_integer) / 2
    sequence = [int(average)]

    for i in range(first_integer, second_integer + 1):
        if i == int(average):
            sequence.append(i)
        else:
            diff = abs(i - int(average))
            if diff < abs(sequence[-1] - int(average)):
                sequence.append(i)

    return sequence

print(*generate_sequence(), sep=' ')
