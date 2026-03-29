import sys

n = int(sys.stdin.readline())
p = list(map(int, sys.stdin.readline().split()))
l = []
r = []

for i in range(n):
    l_i, r_i = map(int, sys.stdin.readline().split())
    l.append(l_i)
    r.append(r_i)

operation_count = 0

for i in range(1, n):
    parent_index = p[i]
    current_value = 0

    while parent_index > 0:
        if l[parent_index] <= l[i]:
            current_value += r[parent_index] - l[parent_index] + 1
        else:
            break

        parent_index = p[parent_index]

    operation_count += current_value

sys.stdout.write(str(operation_count) + '\n')
