import sys

n = int(sys.stdin.readline())
p = [int(x) for x in sys.stdin.readline().split()]
l = []
r = []

for i in range(n):
    l.append(int(sys.stdin.readline()))
    r.append(int(sys.stdin.readline()))

def update_values(i):
    if p[i] == 0:  # root node, no parent
        return max(l[i], 0)
    
    ancestor_range = r[p[i]] - l[p[i]]
    target_value = (l[i] + r[i]) // 2  # approximate value
    diff = target_value - l[i]
    
    if diff <= ancestor_range:
        return diff
    
    parent_diff = update_values(p[i])
    return max(parent_diff, diff)

operations = 0

for i in range(1, n):
    operations += update_values(i)

print(operations)
