import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

result = solve(n, arr)

print(result)
