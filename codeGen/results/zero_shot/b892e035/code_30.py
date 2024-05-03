import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    probabilities = []
    for _ in range(n):
        P, A, B = map(int, sys.stdin.readline().split())
        probabilities.append((P, A, B))
    
    total_prob = 1
    for P, A, B in probabilities:
        total_prob *= ((1 - P / 100) ** 2) ** (n-1)
    
    print('{:.6f}'.format(total_prob))
