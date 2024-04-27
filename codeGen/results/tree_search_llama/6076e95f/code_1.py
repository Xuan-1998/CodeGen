def generate_sequence():
    a, b = map(int, input().split())  # read the two integers from stdin
    sequence = list(range(a, b + 1))  # generate the sequence
    print(*sequence, sep='\n')  # print the sequence to stdout

generate_sequence()
