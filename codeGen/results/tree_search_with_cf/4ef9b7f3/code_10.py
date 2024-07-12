python
def solve():
    import sys
    input = sys.stdin.read
    data = input().split()

    n = int(data[0])
    initial_seq = list(map(int, data[1:n+1]))
    k = int(data[n+1])
    final_seq = list(map(int, data[n+2:n+2+k]))

    if sum(initial_seq) != sum(final_seq):
        print("NO")
        return

    operations = []
    index = 0
    for target in final_seq:
        current_sum = 0
        start_index = index
        while index < n and current_sum < target:
            current_sum += initial_seq[index]
            index += 1

        if current_sum != target:
            print("NO")
            return

        # Now we need to perform operations to merge elements from start_index to index-1
        for i in range(start_index, index - 1):
            if initial_seq[i] > initial_seq[i + 1]:
                operations.append((i + 1, 'R'))
            else:
                operations.append((i + 2, 'L'))

        # Update the initial sequence to reflect the merged element
        initial_seq[start_index] = target
        del initial_seq[start_index + 1:index]

        # Adjust n to reflect the new length of the initial sequence
        n -= (index - start_index - 1)
        index = start_index + 1
    
    print("YES")
    for op in operations:
        print(op[0], op[1])


