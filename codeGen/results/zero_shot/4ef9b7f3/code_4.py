def transform_sequence(n, a, k, b):
    if sum(a) != sum(b):
        print("NO")
        return

    operations = []
    i = 0
    j = 0
    current_sum = 0

    while j < k:
        target = b[j]
        current_sum = 0
        start = i

        while i < n and current_sum < target:
            current_sum += a[i]
            i += 1

        if current_sum != target:
            print("NO")
            return

        # Now we need to merge elements from start to i-1
        for merge_point in range(start, i - 1):
            if a[merge_point] > a[merge_point + 1]:
                for m in range(merge_point, i - 1):
                    operations.append((m + 1, 'R'))
            else:
                for m in range(i - 2, merge_point - 1, -1):
                    operations.append((m + 1, 'L'))
        
        j += 1

    print("YES")
    for op in operations:
        print(op[0], op[1])

# Read input
import sys
input = sys.stdin.read
data = input().split()

n = int(data[0])
a = list(map(int, data[1:n + 1]))
k = int(data[n + 1])
b = list(map(int, data[n + 2:n + 2 + k]))

transform_sequence(n, a, k, b)

