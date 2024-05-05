def count_invertible_matrices(N):
    memo = {}

    def recursive_function(trace_value, matrix_elements):
        if (trace_value, tuple(matrix_elements)) in memo:
            return memo[(trace_value, tuple(matrix_elements))]

        if trace_value < 1 or any(x > N for x in matrix_elements):
            return 0

        if len(matrix_elements) == 4:  # Base case: all elements are given
            if is_invertible_and_positive_determinant(matrix_elements):
                return 1
            else:
                return 0

        result = 0
        for i in range(N + 1):  # Try all possible values for the remaining element
            new_matrix_elements = matrix_elements + [i]
            result += recursive_function(trace_value - i, new_matrix_elements)

        memo[(trace_value, tuple(matrix_elements))] = result
        return result

    def is_invertible_and_positive_determinant(matrix_elements):
        A = [[matrix_elements[0], matrix_elements[1]],
             [matrix_elements[2], matrix_elements[3]]]
        if np.linalg.det(A) > 0 and np.linalg.inv(A).all():
            return True
        else:
            return False

    total_count = 0
    for i in range(1, N + 1):
        total_count += recursive_function(i, [0, 0, 0, 0])

    print(total_count)

# Test the function
T = int(input())
for _ in range(T):
    N = int(input())
    count_invertible_matrices(N)
