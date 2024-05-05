import sys

def merge(a, b):
    # same as before

def is_valid_permutation(p):
    # same as before

n = int(sys.stdin.readline())
p = list(map(int, sys.stdin.readline().split()))
if is_valid_permutation(p):
    print("YES")
else:
    print("NO")
