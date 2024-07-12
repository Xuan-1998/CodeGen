python
def can_transform(n, initial_seq, k, final_seq):
    if sum(initial_seq) != sum(final_seq):
        return "NO"
    
    operations = []
    current_seq = initial_seq[:]
    
    final_index = 0
    for i in range(n):
        if final_index >= k:
            break
        
        while sum(current_seq[:i+1]) > final_seq[final_index]:
            if i == 0 or current_seq[i-1] >= current_seq[i]:
                current_seq[i-1] += current_seq[i]
                current_seq.pop(i)
                operations.append((i+1, 'L'))
                i -= 1
            else:
                current_seq[i+1] += current_seq[i]
                current_seq.pop(i)
                operations.append((i+1, 'R'))
        
        if sum(current_seq[:i+1]) == final_seq[final_index]:
            final_index += 1
    
    if current_seq == final_seq:
        print("YES")
        for op in operations:
            print(op[0], op[1])
    else:
        print("NO")

import sys
input = sys.stdin.read
data = input().split()
n = int(data[0])
initial_seq = list(map(int, data[1:n+1]))
k = int(data[n+1])
final_seq = list(map(int, data[n+2:n+2+k]))

can_transform(n, initial_seq, k, final_seq)

