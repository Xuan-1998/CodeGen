from collections import defaultdict

def count_matrices(N):
    memo = [[0, False] for _ in range(N+1)]
    
    def is_positive_determinant(trace_value):
        if trace_value == 1:
            return True
        
        for a in range(2, N+1):
            for b in range(2, min(a, N-trace_value+1)):
                c = (a**2 + b**2 - (N-trace_value)**2) // 4
                if c > 0 and is_positive_determinant(N-trace_value-a-b+c):
                    return True
        
        return False
    
    for i in range(3, N+1):
        memo[i][0] = sum(is_positive_determinant(j) for j in range(i))
    
    return memo[N][0]

T = int(input())
for _ in range(T):
    N = int(input())
    print(count_matrices(N))
