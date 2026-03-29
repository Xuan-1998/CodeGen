def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    initial = list(map(int, data[1:n+1]))
    k = int(data[n+1])
    final = list(map(int, data[n+2:n+2+k]))
    
    if sum(initial) != sum(final):
        print("NO")
        return
    
    i, j = 0, 0
    operations = []
    
    while i < n and j < k:
        current_sum = 0
        start = i
        while i < n and current_sum < final[j]:
            current_sum += initial[i]
            i += 1
        
        if current_sum != final[j]:
            print("NO")
            return
        
        for pos in range(start, i - 1):
            if initial[pos] < initial[pos + 1]:
                operations.append((pos + 1, 'R'))
                initial[pos + 1] += initial[pos]
            else:
                operations.append((pos + 1, 'L'))
                initial[pos] += initial[pos + 1]
        
        j += 1
    
    if j != k:
        print("NO")
    else:
        print("YES")
        for op in operations:
            print(op[0], op[1])


