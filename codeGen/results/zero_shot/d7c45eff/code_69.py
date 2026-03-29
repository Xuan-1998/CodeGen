import sys

n, k = map(int, sys.stdin.readline().split())
original_string = sys.stdin.readline().strip()

result_string = ''
i = n - 1

while len(result_string) < k:
    if i >= 0 and original_string[i] <= original_string[0]:
        result_string += original_string[i]
        i -= 1
    else:
        result_string += original_string[0]

print(result_string)
