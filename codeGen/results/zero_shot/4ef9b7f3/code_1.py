python
def main():
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
        if i - start > 1:  # If we have combined elements
            max_val = max(a[start:i])
            max_index = start + a[start:i].index(max_val)
            for index in range(start, max_index):
                operations.append((max_index + 1, 'L'))
            for index in range(max_index + 1, i):
                operations.append((max_index + 1, 'R'))
        j += 1
    
    if j != k:
        print("NO")
    else:
        print("YES")
        for op in operations:
            print(op[0], op[1])

if __name__ == "__main__":
    main()

