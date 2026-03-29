def can_transform(n, initial, k, final):
    if sum(initial) != sum(final):
        return False, []

    operations = []
    i, j = 0, 0

    while i < n and j < k:
        current_sum = 0
        start = i
        while i < n and current_sum < final[j]:
            current_sum += initial[i]
            i += 1

        if current_sum != final[j]:
            return False, []

        while i - start > 1:
            if initial[start] < initial[start + 1]:
                operations.append((start + 2, 'L'))
                initial[start + 1] += initial[start]
                del initial[start]
            else:
                operations.append((start + 1, 'R'))
                initial[start] += initial[start + 1]
                del initial[start + 1]
            i -= 1
        j += 1

    return True, operations

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    initial = list(map(int, data[1:n + 1]))
    k = int(data[n + 1])
    final = list(map(int, data[n + 2:n + 2 + k]))
    
    possible, operations = can_transform(n, initial, k, final)
    
    if not possible:
        print("NO")
    else:
        print("YES")
        for op in operations:
            print(op[0], op[1])

if __name__ == "__main__":
    main()

