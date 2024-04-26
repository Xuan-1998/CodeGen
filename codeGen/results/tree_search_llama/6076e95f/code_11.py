def generate_sequence():
    first, last = map(int, input().split())
    result = []
    
    def recursive_sequence(start):
        if start > last:
            return
        result.append(start)
        recursive_sequence(start + 1)

    recursive_sequence(first)
    print(*result, sep=' ')

generate_sequence()
