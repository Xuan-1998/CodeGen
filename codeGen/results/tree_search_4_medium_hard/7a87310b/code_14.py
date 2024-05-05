def solve():
    T = int(input())
    
    def dp(trace_value):
        if trace_value == 0:
            return [[1, 0], [0, 1]]  # base case: one matrix with trace 0 and determinant 1
        
        result = []
        
        for first_element in range(1, (trace_value - 1) // 2 + 1):
            if all((i - j)**2 <= N for i in [first_element, trace_value - first_element] for j in [-N, N]):
                second_element = (trace_value - first_element * 2) // 2
                result.append([[first_element, 0], [second_element, trace_value - first_element - second_element]])
        
        if dp(trace_value - 1):
            return result + [[[i, j]] for i in range(N+1) for j in range(N+1)]
    
    total_count = sum(len(dp(i)) for i in range(1, N+1))
    print(total_count)
