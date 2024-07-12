python
def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    initial_seq = list(map(int, data[1:n+1]))
    k = int(data[n+1])
    final_seq = list(map(int, data[n+2:n+2+k]))
    
    if sum(initial_seq) != sum(final_seq):
        print("NO")
        return
    
    operations = []
    idx = 0
    
    for target in final_seq:
        current_sum = 0
        start_idx = idx
        
        while idx < n and current_sum < target:
            current_sum += initial_seq[idx]
            idx += 1
        
        if current_sum != target:
            print("NO")
            return
        
        for j in range(start_idx, idx - 1):
            if initial_seq[j] > initial_seq[j + 1]:
                operations.append((j + 1, 'R'))
            else:
                operations.append((j + 2, 'L'))
        
        initial_seq[start_idx] = current_sum
        del initial_seq[start_idx + 1:idx]
        n -= (idx - start_idx - 1)
        idx = start_idx + 1
    
    print("YES")
    for op in operations:
        print(op[0], op[1])


