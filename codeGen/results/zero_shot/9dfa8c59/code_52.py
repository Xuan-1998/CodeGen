import sys

n_max = int(sys.stdin.readline())
k_perms = int(sys.stdin.readline())

result = solve(n_max, k_perms)
print(result[0], result[1], result[2])
