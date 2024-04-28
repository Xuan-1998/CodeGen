import sys

n = int(sys.stdin.readline())

permutation = list(range(1, n+1))
permutation.reverse()

print(' '.join(map(str, permutation)))
