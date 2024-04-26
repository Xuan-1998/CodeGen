import sys

def generate_permutation(n):
    result = list(range(1, n + 1))
    result.reverse()
    
    return ' '.join(map(str, result))

n = int(sys.stdin.readline())
print(generate_permutation(n))
