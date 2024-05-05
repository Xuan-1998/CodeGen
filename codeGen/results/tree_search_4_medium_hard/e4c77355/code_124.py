import sys

n = int(sys.stdin.readline())
arr = [int(x) for x in sys.stdin.readline().split()]

print(LIS_length(arr))
