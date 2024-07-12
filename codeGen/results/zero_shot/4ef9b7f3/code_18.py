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
    i = 0
    j = 0
    while i < n and j < k:
        current_sum = 0
        start = i
        while i < n and current_sum < b[j]:
            current_sum += a[i]
            i += 1
        if current_sum != b[j]:
            print("NO")
            return
        if i - start > 1:
            for x in range(start, i - 1):
                if a[x] > a[x + 1]:
                    operations.append((x + 1, 'R'))
                else:
                    operations.append((x + 1, 'L'))
            while i - start > 1:
                if a[start] > a[start + 1]:
                    operations.append((start + 1, 'R'))
                    del a[start + 1]
                else:
                    operations.append((start + 1, 'L'))
                    del a[start]
                i -= 1
        j += 1
    
    if j != k:
        print("NO")
    else:
        print("YES")
        for op in operations:
            print(op[0], op[1])


