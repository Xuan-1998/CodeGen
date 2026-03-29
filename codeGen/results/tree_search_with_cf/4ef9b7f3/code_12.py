    i, j = 0, 0
    operations = []
    
    while i < n and j < k:
        current_sum = 0
        start = i
        while i < n and current_sum < final_seq[j]:
            current_sum += initial_seq[i]
            i += 1
        
        if current_sum != final_seq[j]:
            print("NO")
            return
        
        # Record the operations
        while i - start > 1:
            if initial_seq[start] > initial_seq[start + 1]:
                operations.append((start + 1, 'R'))
                initial_seq[start] += initial_seq[start + 1]
                initial_seq.pop(start + 1)
                i -= 1
            else:
                operations.append((start + 2, 'L'))
                initial_seq[start + 1] += initial_seq[start]
                initial_seq.pop(start)
                i -= 1
        
        j += 1
    
    if j == k and i == n:
        print("YES")
        for op in operations:
            print(op[0], op[1])
    else:
        print("NO")

# Read input from stdin
import sys
input = sys.stdin.read
data = input().split()

n = int(data[0])
initial_seq = list(map(int, data[1:n+1]))
k = int(data[n+1])
final_seq = list(map(int, data[n+2:n+2+k]))

transform_sequence(n, initial_seq, k, final_seq)

