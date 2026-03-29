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
    
    i = 0
    j = 0
    operations = []
    
    while i < n and j < k:
        current_sum = 0
        start = i
        while i < n and current_sum < final_sequence[j]:
            current_sum += initial_sequence[i]
            i += 1
        
        if current_sum != final_sequence[j]:
            print("NO")
            return
        
        # Now we have initial_sequence[start:i] which sums to final_sequence[j]
        while i - start > 1:
            for pos in range(start, i - 1):
                if initial_sequence[pos] > initial_sequence[pos + 1]:
                    operations.append((pos + 1, 'R'))
                    initial_sequence[pos] += initial_sequence[pos + 1]
                    del initial_sequence[pos + 1]
                    i -= 1
                    break
            else:
                for pos in range(i - 1, start, -1):
                    if initial_sequence[pos] > initial_sequence[pos - 1]:
                        operations.append((pos + 1, 'L'))
                        initial_sequence[pos] += initial_sequence[pos - 1]
                        del initial_sequence[pos - 1]
                        i -= 1
                        break
        
        j += 1
    
    if len(initial_sequence) != k:
        print("NO")
    else:
        print("YES")
        for op in operations:
            print(op[0], op[1])


