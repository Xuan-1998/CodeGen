import sys

n = int(sys.stdin.readline())
sequence = list(map(int, sys.stdin.readline().split()))

result = get_y_value(n, sequence)
print(result)
