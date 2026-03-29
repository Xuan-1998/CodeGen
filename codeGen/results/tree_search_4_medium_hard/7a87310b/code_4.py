def is_positive_determinant(trace_value, top_left):
    # Calculate the remaining two elements based on the given trace value
    remaining_elements = [(trace_value - top_left) // 2, (trace_value - top_left) % 2]
    
    # Check if the resulting matrix is invertible and has a positive determinant
    determinant = top_left * remaining_elements[0] - remaining_elements[1] * remaining_elements[1]
    return determinant > 0


def count_invertible_matrices(trace_value):
    memo = {}
    
    def recursive_function(top_left, current_trace=0):
        if (top_left,) in memo:
            return memo[(top_left,)]
        
        if current_trace == trace_value:
            return is_positive_determinant(trace_value, top_left)
        
        results = []
        for remaining_element in range(-1*trace_value//2+1, 2*trace_value//2+1):
            if (current_trace + remaining_element) % 2 != (top_left % 2):
                continue
            next_top_left = (top_left + remaining_element) // 2
            results.append(recursive_function(next_top_left, current_trace + remaining_element))
        
        memo[(top_left,)] = any(results)
        return memo[(top_left,)]
    
    count = recursive_function(0)
    return count


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        total_count = 0
        for trace_value in range(1, N+1):
            total_count += count_invertible_matrices(trace_value)
        print(total_count)


if __name__ == "__main__":
    main()
