python
def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    initial_sequence = list(map(int, data[1:n+1]))
    k = int(data[n+1])
    final_sequence = list(map(int, data[n+2:n+2+k]))
    
    # Check if the sum of initial_sequence equals the sum of final_sequence
    if sum(initial_sequence) != sum(final_sequence):
        print("NO")
        return
    
    operations = []
    current_sequence = initial_sequence[:]
    final_index = 0
    
    i = 0
    while i < len(current_sequence) and final_index < len(final_sequence):
        if current_sequence[i] == final_sequence[final_index]:
            final_index += 1
            i += 1
        elif i < len(current_sequence) - 1 and current_sequence[i] < current_sequence[i + 1]:
            operations.append((i + 1, 'R'))
            current_sequence[i + 1] += current_sequence[i]
            current_sequence.pop(i)
        elif i > 0 and current_sequence[i] < current_sequence[i - 1]:
            operations.append((i + 1, 'L'))
            current_sequence[i - 1] += current_sequence[i]
            current_sequence.pop(i)
        else:
            i += 1
    
    if final_index != len(final_sequence):
        print("NO")
    else:
        print("YES")
        for op in operations:
            print(op[0], op[1])


