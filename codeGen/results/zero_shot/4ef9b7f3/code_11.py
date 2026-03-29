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
    target_index = 0
    
    for i in range(n-1, -1, -1):
        if target_index >= k:
            break
        if current_sequence[i] == final_sequence[target_index]:
            target_index += 1
        else:
            if i > 0 and current_sequence[i] > current_sequence[i-1]:
                operations.append((i, 'L'))
                current_sequence[i-1] += current_sequence[i]
                current_sequence.pop(i)
            elif i < len(current_sequence) - 1 and current_sequence[i] > current_sequence[i+1]:
                operations.append((i, 'R'))
                current_sequence[i+1] += current_sequence[i]
                current_sequence.pop(i)
            else:
                print("NO")
                return
    
    if len(current_sequence) != k or current_sequence != final_sequence:
        print("NO")
    else:
        print("YES")
        for op in operations:
            print(op[0] + 1, op[1])

if __name__ == "__main__":
    main()

