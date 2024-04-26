def consecutive_integers():
    first = int(input("Enter the first integer: "))
    second = int(input("Enter the second integer: "))

    if first >= 0 and second >= 0 and second >= first:
        sequence = []
        for i in range(first, second + 1):
            sequence.append(i)
        return sequence
    else:
        print("Invalid input. Please ensure both integers are non-negative and the second integer is greater than or equal to the first.")
        return None

print(consecutive_integers())
