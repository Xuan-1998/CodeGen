def generate_sequence():
    start = int(input("Enter the starting number: "))
    end = int(input("Enter the ending number: "))

    sequence = list(range(start, end + 1))
    
    for num in sequence:
        print(num)

generate_sequence()
