# BEGIN SOLUTION

def solve(N):
    dp = {(i, False): 0 for i in range(1, N+1)}
    dp[(2, True)] = 1
    dp[(3, True)] = 1
    
    for trace_value in range(4, N+1):
        dp[(trace_value, True)] = sum(
            1 if (i + j == trace_value) and (i > 0 or j > 0) else 0 
            for i in range(trace_value//2 + 1)
            for j in range(i, trace_value//2 + 1)
        )
        
    return dp[(N, True)]

T = int(input())
for _ in range(T):
    N = int(input())
    print(solve(N))
