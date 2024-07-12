def transform_sequence(n, initial_seq, k, final_seq):
    if sum(initial_seq) != sum(final_seq):
        print("NO")
        return
    
    operations = []
    i, j = 0, 0
    current_sum = 0
    
    while j < k:
        current_sum += initial_seq[i]
        if current_sum == final_seq[j]:
            j += 1
            current_sum = 0
        elif current_sum > final_seq[j]:
            print("NO")
            return
        else:
            if i + 1 < len(initial_seq) and initial_seq[i] < initial_seq[i + 1]:
                operations.append((i + 1, 'R'))
                initial_seq[i + 1] += initial_seq[i]
                initial_seq.pop(i)
            elif i > 0 and initial_seq[i] < initial_seq[i - 1]:
                operations.append((i + 1, 'L'))
                initial_seq[i - 1] += initial_seq[i]
                initial_seq.pop(i)
                i -= 1
            else:
                i += 1
    
    print("YES")
    for op in operations:
        print(op[0], op[1])

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    initial_seq = list(map(int, data[1:n+1]))
    k = int(data[n+1])
    final_seq = list(map(int, data[n+2:n+2+k]))
    
    transform_sequence(n, initial_seq, k, final_seq)

