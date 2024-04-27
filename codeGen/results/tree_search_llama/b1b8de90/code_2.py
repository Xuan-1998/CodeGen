import math

def generate_permutation(n):
    permutation = list(range(1, n + 1))
    return ' '.join(map(str, permutation))

n = int(input())
print(generate_permutation(n))
