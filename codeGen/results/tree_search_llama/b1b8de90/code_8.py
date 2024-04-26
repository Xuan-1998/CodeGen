import sys

def generate_permutation(n):
    # Create a list of integers from 1 to n
    permutation = list(range(1, n+1))
    
    for i in range(n//2 + 1):
        if i != n-i-1:
            permutation[i], permutation[n-i-1] = permutation[n-i-1], permutation[i]
    
    return ' '.join(map(str, permutation))

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    print(generate_permutation(n))
