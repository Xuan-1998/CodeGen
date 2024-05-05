import sys

n, q = map(int, input().split())
signs = list(input())

sum_signs = [0] * (n + 1)
for i in range(n):
    sum_signs[i + 1] = sum_signs[i] + (-1 if signs[i] == '-' else 1)

for _ in range(q):
    l, r = map(int, input().split())
    sum_range = sum_signs[r] - sum_signs[l]
    
    count = 0
    if sum_range > 0:
        for i in range(l, r + 1):
            if signs[i] == '-':
                count += 1
    elif sum_range < 0:
        for i in range(l, r + 1):
            if signs[i] == '+':
                count += 1
    
    print(count)
