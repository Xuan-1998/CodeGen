def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    initial_sequence = list(map(int, data[1:n+1]))
    k = int(data[n+1])
    final_sequence = list(map(int, data[n+2:n+2+k]))
    
    if sum(initial_sequence) != sum(final_sequence):
        print("NO")
        return
    
    operations = []
    current_sequence = initial_sequence[:]
    final_index = 0
    
    i = 0
    while i < len(current_sequence):
        if final_index >= k:
            print("NO")
            return
        
        current_sum = 0
        j = i
        while j < len(current_sequence) and current_sum < final_sequence[final_index]:
            current_sum += current_sequence[j]
            j += 1
        
        if current_sum != final_sequence[final_index]:
            print("NO")
            return
        
        # Now, current_sum == final_sequence[final_index]
        if j - i > 1:
            while j - i > 1:
                if current_sequence[i] > current_sequence[i + 1]:
                    current_sequence[i] += current_sequence.pop(i + 1)
                    operations.append((i + 1, 'R'))
                else:
                    current_sequence[i + 1] += current_sequence.pop(i)
                    operations.append((i + 1, 'L'))
                    i -= 1
                j -= 1
        i += 1
        final_index += 1
    
    if final_index != k or len(current_sequence) != k:
        print("NO")
        return
    
    print("YES")
    for op in operations:
        print(op[0], op[1])


