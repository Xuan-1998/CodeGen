def transform_sequence(n, initial_seq, k, final_seq):
    # Check if the sum of initial and final sequences match
    if sum(initial_seq) != sum(final_seq):
        print("NO")
        return

    operations = []
    i, j = 0, 0

    while i < n and j < k:
        current_sum = 0
        while i < n and current_sum < final_seq[j]:
            current_sum += initial_seq[i]
            i += 1

        if current_sum != final_seq[j]:
            print("NO")
            return

        # Determine the operations to merge elements
        for l in range(i - 1, j, -1):
            if initial_seq[l] > initial_seq[l - 1]:
                operations.append((l + 1, 'L'))
            else:
                operations.append((l, 'R'))

        j += 1

    print("YES")
    for op in operations:
        print(op[0], op[1])

# Read input
import sys
input = sys.stdin.read
data = input().split()

n = int(data[0])
initial_seq = list(map(int, data[1:n + 1]))
k = int(data[n + 1])
final_seq = list(map(int, data[n + 2:n + 2 + k]))

transform_sequence(n, initial_seq, k, final_seq)

