python
def transform_sequence(n, initial_sequence, k, final_sequence):
    # Check if sums match
    if sum(initial_sequence) != sum(final_sequence):
        print("NO")
        return
    
    operations = []
    i, j = 0, 0
    current_sum = 0
    
    while i < n and j < k:
        current_sum += initial_sequence[i]
        if current_sum == final_sequence[j]:
            # Move to the next segment
            j += 1
            i += 1
        elif current_sum < final_sequence[j]:
            # We need to merge more elements into the current segment
            if i + 1 < n and initial_sequence[i] > initial_sequence[i + 1]:
                operations.append((i + 1, 'R'))
                initial_sequence[i] += initial_sequence[i + 1]
                initial_sequence.pop(i + 1)
                n -= 1
            elif i + 1 < n and initial_sequence[i] < initial_sequence[i + 1]:
                operations.append((i + 2, 'L'))
                initial_sequence[i + 1] += initial_sequence[i]
                initial_sequence.pop(i)
                n -= 1
            else:
                print("NO")
                return
        else:
            print("NO")
            return
    
    if j == k:
        print("YES")
        for op in operations:
            print(op[0], op[1])
    else:
        print("NO")

# Read input
import sys
input = sys.stdin.read
data = input().split()

n = int(data[0])
initial_sequence = list(map(int, data[1:n + 1]))
k = int(data[n + 1])
final_sequence = list(map(int, data[n + 2:n + 2 + k]))

transform_sequence(n, initial_sequence, k, final_sequence)

