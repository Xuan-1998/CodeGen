python
def can_transform(initial, final):
    n = len(initial)
    k = len(final)
    
    if sum(initial) != sum(final):
        return "NO"
    
    operations = []
    current_sequence = initial[:]
    final_index = 0
    
    while len(current_sequence) > k:
        merged = False
        for i in range(len(current_sequence) - 1):
            if final_index < k and current_sequence[i] + current_sequence[i + 1] == final[final_index]:
                if current_sequence[i] > current_sequence[i + 1]:
                    operations.append((i + 1, 'R'))
                else:
                    operations.append((i + 2, 'L'))
                current_sequence[i] += current_sequence[i + 1]
                del current_sequence[i + 1]
                final_index += 1
                merged = True
                break
        if not merged:
            return "NO"
    
    if current_sequence != final:
        return "NO"
    
    result = ["YES"]
    for op in operations:
        result.append(f"{op[0]} {op[1]}")
    
    return "\n".join(result)

import sys
input = sys.stdin.read
data = input().split()

n = int(data[0])
initial = list(map(int, data[1:n+1]))
k = int(data[n+1])
final = list(map(int, data[n+2:n+2+k]))

output = can_transform(initial, final)
print(output)

