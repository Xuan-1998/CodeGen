import sys
from math import factorial

n = int(sys.stdin.readline().strip())
m = list(map(int, sys.stdin.readline().strip().split()))
count = 0

def is_valid_permutation(perm):
    # TO DO: implement the logic to check if a permutation is valid
    pass

for p in permutations(m):
    if is_valid_permutation(p):
        count += 1

print(count % (10**9 + 7))
