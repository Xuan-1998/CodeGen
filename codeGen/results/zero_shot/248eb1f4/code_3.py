import sys

def process_input():
    T = int(sys.stdin.readline().strip())
    result = []
    
    for _ in range(T):
        M, X = map(int, sys.stdin.readline().split())
        winners = []
        
        for i in range(X + 1):
            if i % (M - 1) == 0:
                winners.append(i)
        
        result.append(' '.join(map(str, winners)))
    
    return '\n'.join(result)

print(process_input())
