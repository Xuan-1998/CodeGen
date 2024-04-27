def generate_sequence():
    # Read input integers from stdin
    start, end = map(int, input().split())
    
    # Generate the sequence and print it to stdout
    for i in range(start, end + 1):
        print(i)

if __name__ == "__main__":
    generate_sequence()
