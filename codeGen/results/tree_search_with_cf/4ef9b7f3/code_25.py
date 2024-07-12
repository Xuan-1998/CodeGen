python
def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    initial_seq = list(map(int, data[1:n+1]))
    k = int(data[n+1])
    final_seq = list(map(int, data[n+2:n+2+k]))
    
    i = 0
    j = 0
    operations = []
    
    while i < n and j < k:
        current_sum = 0
        start = i
        while i < n and current_sum < final_seq[j]:
            current_sum += initial_seq[i]
            i += 1
        
        if current_sum != final_seq[j]:
            print("NO")
            return
        
        # Record operations
        while i - start > 1:
            if initial_seq[start] >= initial_seq[start + 1]:
                operations.append((start + 1, 'R'))
                initial_seq[start] += initial_seq[start + 1]
                del initial_seq[start + 1]
            else:
                operations.append((start + 2, 'L'))
                initial_seq[start + 1] += initial_seq[start]
                del initial_seq[start]
            i -= 1
        
        j += 1
    
    if j != k or len(initial_seq) != k:
        print("NO")
    else:
        print("YES")
        for op in operations:
            print(op[0], op[1])


