def transform_sequence(n, initial_seq, k, final_seq):
    if sum(initial_seq) != sum(final_seq):
        print("NO")
        return
    
    i, j = 0, 0
    operations = []
    
    while i < n and j < k:
        if initial_seq[i] == final_seq[j]:
            i += 1
            j += 1
        elif initial_seq[i] < final_seq[j]:
            if i + 1 < n and initial_seq[i] + initial_seq[i + 1] <= final_seq[j]:
                if initial_seq[i] + initial_seq[i + 1] == final_seq[j]:
                    operations.append((i + 1, 'R'))
                    initial_seq[i + 1] += initial_seq[i]
                    initial_seq.pop(i)
                    n -= 1
                    j += 1
                else:
                    operations.append((i + 1, 'R'))
                    initial_seq[i + 1] += initial_seq[i]
                    initial_seq.pop(i)
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
initial_seq = list(map(int, data[1:n + 1]))
k = int(data[n + 1])
final_seq = list(map(int, data[n + 2:n + 2 + k]))

transform_sequence(n, initial_seq, k, final_seq)

