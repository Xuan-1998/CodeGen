python
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
    while j < k:
        current_sum = 0
        start = i
        while i < n and current_sum < b[j]:
            current_sum += a[i]
            i += 1
        if current_sum != b[j]:
            print("NO")
            return
        if i - start > 1:
            max_index = start
            for x in range(start, i):
                if a[x] > a[max_index]:
                    max_index = x
            for x in range(max_index - 1, start - 1, -1):
                operations.append((x + 1, 'R'))
            for x in range(max_index + 1, i):
                operations.append((max_index + 1, 'L'))
        j += 1

    print("YES")
    for op in operations:
        print(op[0], op[1])


