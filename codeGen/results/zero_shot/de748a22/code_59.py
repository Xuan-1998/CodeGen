import sys

n, q = map(int, sys.stdin.readline().split())
signs = list(map(lambda x: 1 if x == '+' else -1, sys.stdin.readline()))
prefix_sum = [0]
for sign in signs:
    prefix_sum.append(prefix_sum[-1] + sign)

for _ in range(q):
    l, r = map(int, sys.stdin.readline().split())
    total_signs = prefix_sum[r] - prefix_sum[l-1]
    if total_signs == 0:  
        print(0)
    else:
        removed_elements = abs(total_signs) // 2  
        if total_signs % 2:  
            removed_elements += 1
        print(removed_elements)
