def generate_sequence():
    start, end = map(int, input().split())
    return [i for i in range(start, end+1)]

print(generate_sequence())
