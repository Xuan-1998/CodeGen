N = int(input())  # read N from stdin
K = int(input())  # read K from stdin
arr = [[int(x) for x in input().split()] for _ in range(N)]  # read arr[][] from stdin

print(numPaths(arr, N, K))  # print the result to stdout
