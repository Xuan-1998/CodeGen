def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    a = list(map(int, data[1:n+1]))
    k = int(data[n+1])
    b = list(map(int, data[n+2:n+2+k]))
    
    if sum(a) != sum(b):
        print("NO")
        return
    
    operations = []
    i, j = 0, 0
    current_sum = 0
    
    while i < n and j < k:
        current_sum += a[i]
        if current_sum == b[j]:
            current_sum = 0
            j += 1
        elif current_sum > b[j]:
            print("NO")
            return
        i += 1
    
    if j != k:
        print("NO")
        return
    
    i, j = 0, 0
    current_sum = 0
    while i < n and j < k:
        current_sum += a[i]
        if current_sum == b[j]:
            current_sum = 0
            j += 1
        else:
            if i + 1 < n and a[i] > a[i + 1]:
                operations.append((i + 1, 'R'))
                a[i] += a[i + 1]
                a.pop(i + 1)
            else:
                operations.append((i + 1, 'L'))
                a[i + 1] += a[i]
                a.pop(i)
                i -= 1
        i += 1
    
    print("YES")
    for op in operations:
        print(op[0], op[1])


