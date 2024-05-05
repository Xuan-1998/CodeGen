from collections import defaultdict

def count_matrices(N):
    memo = defaultdict(int)
    for i in range(N+1):
        memo[(0, [])] = 1 if i == 0 else 0
    for trace_value in range(1, N+1):
        for off_diagonal_element in range(-N, N+1):
            for diagonal_element in range(-N, N+1):
                if off_diagonal_element + diagonal_element == trace_value:
                    for prev_trace_value in range(trace_value-2, -1, -1):
                        if memo[(prev_trace_value, [off_diagonal_element, diagonal_element])]:
                            if (trace_value-off_diagonal_element-diagonal_element) >= 0 and trace_value > 0:
                                memo[(trace_value, [off_diagonal_element, diagonal_element])] += memo[(prev_trace_value, [off_diagonal_element, diagonal_element])]
    return sum(memo.values())

T = int(input())
for _ in range(T):
    N = int(input())
    print(count_matrices(N))
