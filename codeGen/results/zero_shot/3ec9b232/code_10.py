import sys

def calculate_permutations(n):
    result = 1
    for i in range(1, n + 1):
        result = (result * i) % (10**9 + 7)
    return result

n = int(sys.stdin.readline().strip())
m = list(map(int, sys.stdin.readline().strip().split()))
print(calculate_permutations(n))
