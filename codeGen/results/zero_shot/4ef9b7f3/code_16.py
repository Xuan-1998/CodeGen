python
def transform_sequence(n, initial_seq, k, final_seq):
    # Check if transformation is possible
    if k > n:
        print("NO")
        return

    operations = []
    current_sum = 0
    current_index = 0
    final_index = 0

    while current_index < n and final_index < k:
        current_sum += initial_seq[current_index]
        
        if current_sum == final_seq[final_index]:
            current_sum = 0
            final_index += 1
        elif current_sum > final_seq[final_index]:
            print("NO")
            return
        
        current_index += 1

    if final_index != k:
        print("NO")
        return

    # Generate operations
    current_index = 0
    final_index = 0
    current_sum = 0
    while current_index < n and final_index < k:
        current_sum += initial_seq[current_index]
        if current_sum == final_seq[final_index]:
            current_sum = 0
            final_index += 1
        else:
            if current_index + 1 < n:
                if initial_seq[current_index] > initial_seq[current_index + 1]:
                    operations.append((current_index + 1, 'R'))
                else:
                    operations.append((current_index + 2, 'L'))
            current_index += 1

    print("YES")
    for op in operations:
        print(op[0], op[1])

# Read input
import sys
input = sys.stdin.read
data = input().split()

n = int(data[0])
initial_seq = list(map(int, data[1:n+1]))
k = int(data[n+1])
final_seq = list(map(int, data[n+2:n+2+k]))

# Call the function
transform_sequence(n, initial_seq, k, final_seq)

