python
def solve():
    import sys
    input = sys.stdin.read
    data = input().split()

    n = int(data[0])
    initial_sequence = list(map(int, data[1:n+1]))
    k = int(data[n+1])
    final_sequence = list(map(int, data[n+2:n+2+k]))

    if sum(initial_sequence) != sum(final_sequence):
        print("NO")
        return

    operations = []
    i = 0
    for target in final_sequence:
        current_sum = 0
        start = i
        while i < n and current_sum < target:
            current_sum += initial_sequence[i]
            i += 1

        if current_sum != target:
            print("NO")
            return

        # Now we have a subarray from start to i-1 that sums to target
        while i - start > 1:
            max_index = start
            for j in range(start, i):
                if initial_sequence[j] > initial_sequence[max_index]:
                    max_index = j

            if max_index > start and initial_sequence[max_index] > initial_sequence[max_index - 1]:
                operations.append((max_index + 1, 'L'))
                initial_sequence[max_index] += initial_sequence[max_index - 1]
                del initial_sequence[max_index - 1]
                i -= 1
            elif max_index < i - 1 and initial_sequence[max_index] > initial_sequence[max_index + 1]:
                operations.append((max_index + 1, 'R'))
                initial_sequence[max_index] += initial_sequence[max_index + 1]
                del initial_sequence[max_index + 1]
                i -= 1
            else:
                print("NO")
                return

    print("YES")
    for op in operations:
        print(op[0], op[1])


