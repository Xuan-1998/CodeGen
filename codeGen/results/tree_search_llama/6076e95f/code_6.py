def generate_integer_sequence():
    start, end = map(int, input().split())
    return list(range(start, end + 1))

print(generate_integer_sequence())
