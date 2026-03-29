import sys

n_max, k_perms = map(int, sys.stdin.readline().split())
result = solve(n_max, k_perms)
print(*result, sep='\n')
