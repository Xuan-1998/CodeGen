python
def can_transform(n, initial_seq, k, final_seq):
    if sum(initial_seq) != sum(final_seq):
        print("NO")
        return
    
    operations = []
    i, j = 0, 0
    
    while j < k:
        current_sum = 0
        segment_start = i
        
        while i < n and current_sum < final_seq[j]:
            current_sum += initial_seq[i]
            i += 1
        
        if current_sum != final_seq[j]:
            print("NO")
            return
        
        while i - segment_start > 1:
            if initial_seq[segment_start] < initial_seq[segment_start + 1]:
                operations.append((segment_start + 2, 'L'))
                initial_seq[segment_start + 1] += initial_seq[segment_start]
                initial_seq.pop(segment_start)
                i -= 1
            else:
                operations.append((segment_start + 1, 'R'))
                initial_seq[segment_start] += initial_seq[segment_start + 1]
                initial_seq.pop(segment_start + 1)
                i -= 1
        
        j += 1
    
    print("YES")
    for op in operations:
        print(op[0], op[1])

# Reading input from stdin
import sys
input = sys.stdin.read
data = input().split()

n = int(data[0])
initial_seq = list(map(int, data[1:n+1]))
k = int(data[n+1])
final_seq = list(map(int, data[n+2:n+2+k]))

can_transform(n, initial_seq, k, final_seq)

