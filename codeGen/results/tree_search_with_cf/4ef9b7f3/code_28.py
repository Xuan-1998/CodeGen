def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    initial_sequence = list(map(int, data[1:n+1]))
    k = int(data[n+1])
    final_sequence = list(map(int, data[n+2:]))
    
    operations = []
    pos = 0  # Pointer for the initial sequence
    for target in final_sequence:
        current_sum = 0
        start = pos
        while pos < n and current_sum < target:
            current_sum += initial_sequence[pos]
            pos += 1
        
        if current_sum != target:
            print("NO")
            return
        
        # Now we have a subarray initial_sequence[start:pos] that sums to target
        # We need to merge it into one element
        while pos - start > 1:
            # Prefer to merge smaller values into larger values
            if initial_sequence[start] < initial_sequence[start + 1]:
                operations.append((start + 2, 'L'))
                initial_sequence[start + 1] += initial_sequence[start]
                start += 1
            else:
                operations.append((start + 1, 'R'))
                initial_sequence[start] += initial_sequence[start + 1]
                initial_sequence.pop(start + 1)
                pos -= 1
                n -= 1
    
    print("YES")
    for op in operations:
        print(op[0], op[1])


