def generate_sequence():
    start, end = map(int, input().split())
    sequence = list(range(start, end + 1))
    print(*sequence, sep='\n')

generate_sequence()
