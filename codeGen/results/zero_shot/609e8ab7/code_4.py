import sys

n = int(input())
p = list(map(int, input().split()))
l = [int(x) for x in input().split()]
r = [int(x) for x in input().split()]

def calculate_min_operations():
    max_lower_diff = 0
    max_upper_diff = 0

    for i in range(1, n):
        if l[i-1] > r[i]:
            lower_diff = l[i-1] - r[i]
            max_lower_diff = max(max_lower_diff, lower_diff)
        else:
            upper_diff = l[i+1] - r[i]
            max_upper_diff = max(max_upper_diff, upper_diff)

    return max_lower_diff + max_upper_diff

print(calculate_min_operations())
