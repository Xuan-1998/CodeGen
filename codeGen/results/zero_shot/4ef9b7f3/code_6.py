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
    i, j = 0, 0
    
    while i < n and j < k:
        current_sum = 0
        start = i
        while i < n and current_sum < final_seq[j]:
            current_sum += initial_seq[i]
            i += 1
        
        if current_sum != final_seq[j]:
            print("NO")
            return
        
        # Collect operations
        for x in range(start, i - 1):
            if initial_seq[x] > initial_seq[x + 1]:
                operations.append((x + 1, 'R'))
            else:
                operations.append((x + 2, 'L'))
        
        j += 1
    
    if j != k:
        print("NO")
        return
    
    print("YES")
    for op in operations:
        print(op[0], op[1])


