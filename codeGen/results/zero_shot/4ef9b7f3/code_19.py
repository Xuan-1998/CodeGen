def main():
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
    while i < len(current_sequence) and final_index < k:
        current_sum = 0
        start = i
        while i < len(current_sequence) and current_sum < final_sequence[final_index]:
            current_sum += current_sequence[i]
            i += 1
        
        if current_sum != final_sequence[final_index]:
            print("NO")
            return
        
        for j in range(start, i-1):
            if current_sequence[j] > current_sequence[j+1]:
                operations.append((j+1, 'R'))
            else:
                operations.append((j+2, 'L'))
        
        current_sequence = current_sequence[:start] + [current_sum] + current_sequence[i:]
        final_index += 1
        i = start + 1
    
    if final_index != k or len(current_sequence) != k:
        print("NO")
    else:
        print("YES")
        for op in operations:
            print(op[0], op[1])

if __name__ == "__main__":
    main()

