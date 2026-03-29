def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    a = list(map(int, data[1:n+1]))
    k = int(data[n+1])
    b = list(map(int, data[n+2:n+2+k]))
    
    # Check if the sum of the initial sequence matches the sum of the final sequence
    if sum(a) != sum(b):
        print("NO")
        return
    
    operations = []
    i = 0
    j = 0
    
    while i < n and j < k:
        current_sum = a[i]
        start = i
        while current_sum < b[j] and i < n - 1:
            i += 1
            current_sum += a[i]
        
        if current_sum != b[j]:
            print("NO")
            return
        
        # Merge elements to match b[j]
        for x in range(start, i):
            if a[x] < a[x + 1]:
                operations.append((x + 1, 'R'))
            else:
                operations.append((x + 2, 'L'))
        
        j += 1
        i += 1
    
    if j != k:
        print("NO")
    else:
        print("YES")
        for op in operations:
            print(op[0], op[1])


