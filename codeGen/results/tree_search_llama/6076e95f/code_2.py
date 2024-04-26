def generate_sequence(num1: int, num2: int) -> list[int]:
    return list(range(num1, num2 + 1))

if __name__ == "__main__":
    start = int(input("Enter the starting integer: "))
    end = int(input("Enter the ending integer: "))

    sequence = generate_sequence(start, end)
    print(sequence)
