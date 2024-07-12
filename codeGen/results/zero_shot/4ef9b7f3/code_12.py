python
def transform_sequence(n, initial_seq, k, final_seq):
    if sum(initial_seq) != sum(final_seq):
        print("NO")
        return
    
    current_seq = initial_seq[:]
    operations = []
    final_index = 0
    i = 0
    
    while i < len(current_seq) and final_index < k:
        target = final_seq[final_index]
        current_sum = 0
        start_index = i
        
        while i < len(current_seq) and current_sum < target:
            current_sum += current_seq[i]
            i += 1
        
        if current_sum != target:
            print("NO")
            return
        
        # Now we have a segment from start_index to i-1 that sums up to target
        for j in range(start_index, i-1):
            if current_seq[j] < current_seq[j+1]:
                operations.append((j+1, 'R'))
            else:
                operations.append((j+2, 'L'))
        
        current_seq = current_seq[:start_index] + [current_sum] + current_seq[i:]
        final_index += 1
        i = start_index + 1
    
    if final_index != k or len(current_seq) != k:
        print("NO")
        return
    
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

