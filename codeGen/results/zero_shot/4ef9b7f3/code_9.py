def transform_sequence(n, initial_seq, k, final_seq):
    if sum(initial_seq) != sum(final_seq):
        print("NO")
        return

    operations = []
    current_seq = initial_seq[:]
    final_index = 0
    i = 0
    
    while i < len(current_seq) and final_index < k:
        if current_seq[i] == final_seq[final_index]:
            final_index += 1
            i += 1
        elif i < len(current_seq) - 1 and current_seq[i] < current_seq[i + 1]:
            current_seq[i + 1] += current_seq[i]
            operations.append((i + 1, 'L'))
            del current_seq[i]
        elif i < len(current_seq) - 1 and current_seq[i] > current_seq[i + 1]:
            current_seq[i] += current_seq[i + 1]
            operations.append((i + 1, 'R'))
            del current_seq[i + 1]
        else:
            print("NO")
            return

    if final_index != k or current_seq != final_seq:
        print("NO")
    else:
        print("YES")
        for op in operations:
            print(f"{op[0]} {op[1]}")

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    initial_seq = list(map(int, data[1:n+1]))
    k = int(data[n+1])
    final_seq = list(map(int, data[n+2:n+2+k]))
    
    transform_sequence(n, initial_seq, k, final_seq)

